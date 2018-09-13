
# for test val set
import os
import json
import numpy as np
from sklearn.externals import joblib
import data_norm_single
import csv
import coor_validation as coor

file_name = "name2id.csv"
dict_csv = {}
with open(file_name) as f:
    reader = csv.DictReader(f)
    for row in reader:
        dict_csv[row["filename"]] = row["image_id"]



local_path = "./val_json_result/"
file_ext = ".json"
json_dict = dict() # initial dict
json_dict["result"] = []
old_id = ''
#problem = 0
for i in range(1,6): #scene 1,2,3,4,5i
    nn_model = joblib.load('nn_train_model_scene_%d.m' % (i)) # correspondent nn model
    with open("alphapose-results_scene_%d.json"%(i)) as f: # open an json file for that scene
        alpha = json.load(f)
    for single_object_a in alpha: # each single object regardless of which pic it is from
        file_name = single_object_a.get("image_id")   # get the image id of that object
        # need to add an image_id buffer here
        if old_id != file_name or old_id == '': # new pic
            #json_dict["result"][-1]["object"] = []  append the objects from last pict to it
            temp_dict = dict()
            temp_dict["image_id"] = dict_csv[file_name]
            temp_dict["object"] = []
            json_dict["result"].append(temp_dict)

        old_id = file_name # update file name

        x_test,y_test = single_object_a["keypoints"][0], single_object_a["keypoints"][1]  # get the nose keypoint
        label_name = local_path + file_name.split('.')[0] + file_ext # change jpg to json
        with open(label_name) as ff: # open that specific json file
            label_data = json.load(ff)
        label_data_object = label_data.get("annotation")[0].get("object")  # get all objects from that label file

        for single_object in label_data_object:

            minx, miny, maxx, maxy = single_object["minx"], single_object["miny"], single_object["maxx"], single_object["maxy"]

            if (x_test - minx) >= 0 and (maxx - x_test) >= 0 and (y_test - miny) >= 0 and (maxy - y_test) >= 0:  # object in the labeled one
                x12y2 = [minx, miny, maxx, maxy]
                a12c17 = single_object_a.get("keypoints")
                raw_output = x12y2 + a12c17  # concat two list together
                X_raw = [round(i, 3) for i in raw_output]
                X = [data_norm_single.data_norm(X_raw)] # 51 inputs
                if coor.coor(X[0]):
                    #problem += 1
                    break
                Y_predict_raw = nn_model.predict(X)
                Y_predict = Y_predict_raw[0]
                Y_list = []
                for k in Y_predict:
                    if k == 0:
                        Y_list.append(0)
                    else:
                        Y_list.append(1)
                single_dict = dict()
                single_dict["minx"] = minx
                single_dict["miny"] = miny
                single_dict["maxx"] = maxx
                single_dict["maxy"] = maxy
                single_dict["staff"] = Y_list[1]
                single_dict["customer"] = Y_list[2]
                single_dict["stand"] = Y_list[3]
                single_dict["sit"] = Y_list[4]
                single_dict["play_with_phone"] = Y_list[5]
                single_dict["male"] = Y_list[0]
                single_dict["female"] = 1 - Y_list[0]
                single_dict["confidence"] = 1
                json_dict["result"][-1]["object"].append(single_dict)
                # wright in the json
                break   # find the object label
            else:
                continue


# dump json
#print(json_dict)
result_path = "val_result.json"
with open(result_path,'w') as f:
    json.dump(json_dict,f)
#print(problem)
