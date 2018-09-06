#import os
import json
#import numpy as np


# input_value = np.zeros((0, 55))
# output_value = np.zeros((0, 6))
def dataloader():
    input_value = []
    output_value = []
    local_path = "./Test_set/label_scene_5_train/"
    file_ext = ".json"

    with open("alphapose-results.json") as f:
        alpha = json.load(f)
    count = 0
    for single_object_a in alpha: # each single object regardless of which pic it is from

        file_name = single_object_a.get("image_id")   # get the image id of that object
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
                raw_output_round = [round(i, 3) for i in raw_output]
                new_input = raw_output_round   # np.array([raw_output_round]) # np array does not round
                new_output = [single_object["gender"], single_object["staff"], single_object["customer"], single_object["stand"], single_object["sit"], single_object["play_with_phone"]]
                input_value.extend([new_input])
                output_value.extend([new_output])
                # print(input_value)
                break   # find the object label
            else:
                continue
        count+=1
        #if count == 10:break
        # print(count)
    return input_value, output_value


def data_norm_coor(x, y, x0, y0, w, h):
    x_norm = (x - x0)/w
    y_norm = (y - y0)/h
    return x_norm, y_norm


def data_norm(input_value):
    input_value_norm = []
    for single_data in input_value:
        width = single_data[2] - single_data[0]
        height = single_data[3] - single_data[1]
        single_data[4], single_data[5] = data_norm_coor(single_data[4], single_data[5], single_data[0], single_data[1], width,height)# 0
        single_data[7], single_data[8] = data_norm_coor(single_data[7], single_data[8], single_data[0], single_data[1], width,height)# 1
        single_data[10], single_data[11] = data_norm_coor(single_data[10], single_data[11], single_data[0], single_data[1], width,height)# 2
        single_data[13], single_data[14] = data_norm_coor(single_data[13], single_data[14], single_data[0], single_data[1], width,height)# 3
        single_data[16], single_data[17] = data_norm_coor(single_data[16], single_data[17], single_data[0], single_data[1], width,height)# 4
        single_data[19], single_data[20] = data_norm_coor(single_data[19], single_data[20], single_data[0], single_data[1], width,height)# 5
        single_data[22], single_data[23] = data_norm_coor(single_data[22], single_data[23], single_data[0], single_data[1], width,height)# 6
        single_data[25], single_data[26] = data_norm_coor(single_data[25], single_data[26], single_data[0], single_data[1], width,height)# 7
        single_data[28], single_data[29] = data_norm_coor(single_data[28], single_data[29], single_data[0], single_data[1], width,height)# 8
        single_data[31], single_data[32] = data_norm_coor(single_data[31], single_data[32], single_data[0], single_data[1], width,height)# 9
        single_data[34], single_data[35] = data_norm_coor(single_data[34], single_data[35], single_data[0], single_data[1], width,height)# 10
        single_data[37], single_data[38] = data_norm_coor(single_data[37], single_data[38], single_data[0], single_data[1], width,height)# 11
        single_data[40], single_data[41] = data_norm_coor(single_data[40], single_data[41], single_data[0], single_data[1], width,height)# 12
        single_data[43], single_data[44] = data_norm_coor(single_data[43], single_data[44], single_data[0], single_data[1], width,height)# 13
        single_data[46], single_data[47] = data_norm_coor(single_data[46], single_data[47], single_data[0], single_data[1], width,height)# 14
        single_data[49], single_data[50] = data_norm_coor(single_data[49], single_data[50], single_data[0], single_data[1], width,height)# 15
        single_data[52], single_data[53] = data_norm_coor(single_data[52], single_data[53], single_data[0], single_data[1], width,height)# 16
        input_value_norm.extend([single_data[4:]]) # data norm and trim
        # print([single_data[4:]])
    return input_value_norm


def test():
    x, y = dataloader()
    x1 = data_norm(x)
    #print("==================")
    #print(x1)
    return x1, y
