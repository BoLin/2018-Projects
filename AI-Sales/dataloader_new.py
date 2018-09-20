# dataloader for keypoints from Yuchen Not AlphaPose
import os
import json
import numpy as np
import math


# input_value = np.zeros((0, 55))
# output_value = np.zeros((0, 6))
def dataloader():
    keypoints_path = "./train_keypoint_split/"
    label_path = "./label_scene_train/"
    input_value = []
    output_value = []
    file_dict = os.listdir(keypoints_path)
    for filename in file_dict:
        if filename[6] == "5":
            with open(keypoints_path + filename) as fk:
                keypoints_raw = json.load(fk)
            with open(label_path + filename) as fl:
                labels_raw = json.load(fl)
            for labels in labels_raw["annotation"][0]["object"]:
                minx, miny, maxx, maxy = labels["minx"], labels["miny"], labels["maxx"], labels["maxy"]
                mean_coor = [(minx + maxx) / 2, (miny + maxy) / 2]
                coor_dist = 10000
                right_keypoints = []

                for keypoints in keypoints_raw["object"]: # 51 points
                    x_mean, y_mean = 0, 0
                    for i in range(0, len(keypoints), 3):
                        x_mean += keypoints[i]
                        y_mean += keypoints[i + 1]
                    key_mean = [x_mean / 17, y_mean / 17]
                    new_dist = math.sqrt((key_mean[0] - mean_coor[0]) ** 2 + (key_mean[1] - mean_coor[1]) ** 2)
                    #  find the min dist
                    if new_dist < coor_dist:
                        right_keypoints = keypoints
                        coor_dist = new_dist
                x_nose, y_nose = right_keypoints[0], right_keypoints[1]
                if (x_nose - minx) >= 0 and (maxx - x_nose) >= 0 and (y_nose - miny) >= 0 and (maxy - y_nose) >= 0:
                    bbox = [minx, miny, maxx, maxy]
                    bbox.extend(right_keypoints)
                    new_output = [labels["gender"], labels["staff"], labels["customer"],labels["stand"], labels["sit"], labels["play_with_phone"]]
                    #print(bbox)
                    input_value.append(bbox)
                    output_value.append(new_output)
    return input_value,output_value

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
