# 914 开动的 为了测试一框一keypoints的可行性 目前的最新正式版本
# for test val set
import os
import json
import numpy as np
from sklearn.externals import joblib
import data_norm_single
import csv
import coor_validation as coor
import math

# file_name = "name2id.csv"
# dict_csv = {}
# with open(file_name) as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         dict_csv[row["filename"]] = row["image_id"]

with open("file2id.json") as f:
    dict_csv = json.load(f)



#local_path = "./val_json_result/" # file path for bbox
local_path = "./bot_train_person_keypoints/bot_train_json_result/" # file path for bbox
#local_path = "./bot_train_gender/json_result/"
file_ext = ".json"
json_dict = dict() # initial dict
json_dict["results"] = []
old_id = ''
problem = 0


json_dict = dict() # initial dict output
json_dict["results"] = []


#keypoints_path = "results_bot_val_new.json"
keypoints_path = "./train_keypoint_split/"
file_dict = os.listdir(local_path)


for single_file in file_dict: # each train bbox
    print(single_file)
    with open(local_path + single_file) as f: # =============================open each pic json with bbox
        object_bbox_raw = json.load(f)
    object_bbox = object_bbox_raw.get("annotation")[0].get("object")
    file_name = object_bbox_raw.get("annotation")[0].get("filename")
    m = int(file_name[6])
    nn_model = joblib.load('nn_train_model_scene_%d.m' % (m))  # correspondent nn model for each pic
    # ======================= initial json for each pic
    temp_dict = dict()
    temp_dict["image_id"] = dict_csv[file_name]
    temp_dict["object"] = []
    json_dict["results"].append(temp_dict)
    for single_object in object_bbox:  #====================== each box
        minx, miny, maxx, maxy = single_object["minx"], single_object["miny"], single_object["maxx"], single_object[
            "maxy"]
        mean_coor = [(minx + maxx) / 2, (miny + maxy) / 2]
        if single_object["name"] == "male":
            gender = 0
        else:
            gender = 1
        coor_dist = 10000
        right_keypoints = []
        # find the one file
        with open(keypoints_path + file_name.split(".")[0] + file_ext) as ff:
            keypoints = json.load(ff)
            keypoints_pure = keypoints["object"]
            # print(keypoints_pure)
            # print('================')
        for points in keypoints_pure:
            # print(points)
            # print('================')
            x_mean, y_mean = 0, 0
            for i in range(0, len(points), 3):
                x_mean += points[i]
                y_mean += points[i + 1]
            key_mean = [x_mean / 17, y_mean / 17]
            new_dist = math.sqrt((key_mean[0] - mean_coor[0])**2 + (key_mean[1] - mean_coor[1])**2)
        #  find the min dist
            if new_dist < coor_dist:
                right_keypoints = points
                coor_dist = new_dist
        # run through all the keypoint sets
        # prepare to norm
        X_raw = [minx, miny, maxx, maxy]
        X_raw.extend(right_keypoints)
        #print(X_raw)
        X = [data_norm_single.data_norm(X_raw)]  # 51 inputs
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
        # single_dict["male"] = 1 - Y_list[0]
        # single_dict["female"] = Y_list[0]
        single_dict["male"] = 1 - gender
        single_dict["female"] = gender
        single_dict["confidence"] = 1
        json_dict["results"][-1]["object"].append(single_dict)
        # wright in the json



# dump json
#print(json_dict)
result_path = "val_result_gender_918.json"
with open(result_path,'w') as f:
    json.dump(json_dict,f)
print("===============OVER==============")

