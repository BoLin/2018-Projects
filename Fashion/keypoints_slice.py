import json
import os
#  把keypoint 的 json文件 按照文件名 分割 一个文件下含有一张图上所有的keypoints


keypoints_path = "C:/Users/lsh11941/Documents/Fashion/Fashion/alphapose-results.json"
folder_path = "C:/Users/lsh11941/Documents/Fashion/Fashion/keypoints/"
os.makedirs（folder_path）

with open(keypoints_path) as f:
    data_raw = json.load(f) # all data
old_name = '' # flag
new_slice = dict()
for i in range(len(data_raw)):
    filename = data_raw[i]["image_id"].split("/")[-1].split(".")[0]
    if filename != old_name: # 发现新的图片
        print(filename)
        if old_name != '': # 将旧图片打包dump
            result_path = filename + ".json"
            with open(folder_path + old_name + '.json', 'w') as f:
                json.dump(new_slice, f)
        old_name = filename
        new_slice = dict() # create new slice dict
        new_slice["image_id"] = filename
        new_slice["object"] = []
    new_slice["object"].append(data_raw[i]["keypoints"])

    if i == len(data_raw)-1:

        result_path = filename + ".json"
        with open(folder_path + result_path, 'w') as f:
            json.dump(new_slice, f)
