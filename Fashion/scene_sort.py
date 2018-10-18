# Sorting the raw data into several different scenes includes Runway Pic, Single/Multi-Person Snapshots and Features.
import json
import os
import shutil
def keypointsValid(keypoints):# 洗框
    x,y,c = [],[],[]
    for i in range(0,len(keypoints),3):
        x.append(keypoints[i])
        y.append(keypoints[i+1])
        c.append(keypoints[i+2])
    c_mean = sum(c) / len(c)
    height = max(y)-min(y) # the height of the body
    #print(height)
    #width = max(x)-min(x)
    #c.pop(int(c.index(min(c))))
    return height > 350 and c_mean > 0.3

def keypointsWash(keypoints):
    new = []
    for temp in keypoints:
        if keypointsValid(temp):
            new.append(temp)
    return new

def keypointsTshow(keypoints):
    confidence_thres = 0.6
    if keypoints ==[]:
        return 4 # 4 for no big person, parts of body

    if len(keypoints)>1: # if more than 1 big person in the scene
        #这里还要分一下
        return 3 # 3 for many big person

# single person check
    x,y,c = [],[],[]
    for i in range(0,len(keypoints[0]),3):
        x.append(keypoints[0][i])
        y.append(keypoints[0][i+1])
        c.append(keypoints[0][i+2])
    x_mean = sum(x[0:5])/5
    x_knee_mean = sum(x[13:16])/4
    y_mean = sum(y[0:5])/5
    #c_mean = sum(c[0:5])/5
    c_mean = sum(c) / len(c)
    c_foot_mean = sum(c[15:16]) / 2
    head_thres = 36
    head_y_thres = 135
    c_mean_thres = 0.63
    knee_thres = 60
    foot_thres = 0.1
    if abs(x_mean - 180) <head_thres and y_mean < head_y_thres and c_mean > c_mean_thres and abs(x_knee_mean - 180) <knee_thres and c_foot_mean > foot_thres:# 头部定位
        return 1 # tshow
    else:
        return 2 # single person not tshow

keypoints_path = "../Fashion/Fashion/keypoints/"
img_path = "../Fashion/Miu-Miu/"
keypoints_dir = os.listdir(keypoints_path)
img_dir = os.listdir(img_path)
pic_w = 360
pic_h = 540
result_dict = {}
confidence_thres = 0.6 # keypoints confident threshold

for pic_name in img_dir:
    json_name = pic_name.split("/")[-1].split(".")[0] + ".json"
    if json_name in keypoints_dir:
        with open(keypoints_path + json_name) as f:
            raw_data = json.load(f)
        keypoints_all = raw_data["object"] # all keypoints sets in a pic
        #print(keypoints_all)
        keypoints_all = keypointsWash(keypoints_all)
        #print(keypoints_all)
        result_dict[json_name] = keypointsTshow(keypoints_all)
    else:
        # pic does not have human, not tshow pic
        result_dict[json_name] = 4 # 5 for parts no human

for i in range(4):
    os.mkdir(img_path + str(i+1))

for pic_name in img_dir:
    json_name = pic_name.split("/")[-1].split(".")[0]+ ".json"
    newpath = img_path + str(result_dict[json_name]) + "/"+pic_name
    shutil.copyfile(img_path + pic_name,newpath)





