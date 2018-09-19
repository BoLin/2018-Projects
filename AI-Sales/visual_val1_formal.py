# val1 结果可视化
# 包括 bbox + keypoints

import os
import cv2
import json
import csv

img_path = "./val1_pic"
img_path_dict = os.listdir(img_path)
result_path = "./Formal_Result/宝智尊_val1_20180919_1.json" # ===== 只输入提交结果
new_img_path = "./vis_img/"
# ======= id2file ==============
file_name = "name2id.csv"
dict_csv = {}
with open(file_name) as f:
    reader = csv.DictReader(f)
    for row in reader:
        dict_csv[row["image_id"]] = row["filename"]


# =============== plot color============
l_pair = [
            (0, 1), (0, 2), (1, 3), (2, 4),  # Head
            (5, 6), (5, 7), (7, 9), (6, 8), (8, 10),
            (17, 11), (17, 12),  # Body
            (11, 13), (12, 14), (13, 15), (14, 16)
        ]
p_color = [(0, 255, 255), (0, 191, 255),(0, 255, 102),(0, 77, 255), (0, 255, 0), #Nose, LEye, REye, LEar, REar
                    (77,255,255), (77, 255, 204), (77,204,255), (191, 255, 77), (77,191,255), (191, 255, 77), #LShoulder, RShoulder, LElbow, RElbow, LWrist, RWrist
                    (204,77,255), (77,255,204), (191,77,255), (77,255,191), (127,77,255), (77,255,127), (0, 255, 255)] #LHip, RHip, LKnee, Rknee, LAnkle, RAnkle, Neck
line_color = [(0, 215, 255), (0, 255, 204), (0, 134, 255), (0, 255, 50),
                    (77,255,222), (77,196,255), (77,135,255), (191,255,77), (77,255,77),
                    (77,222,255), (255,156,127),
                    (0,127,255), (255,127,77), (0,77,255), (255,77,36)]
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
size = 1
thick = 1

with open(result_path) as f:
    json_whole = json.load(f)

for each_pic in json_whole["results"]:
    filename = dict_csv[each_pic["image_id"]] #   找到图片名
    print(filename)

    img = cv2.imread(img_path + "/" + filename)
    img_copy = img.copy()
    for single_object in each_pic["object"]:

        minx, miny, maxx, maxy = single_object["minx"], single_object["miny"], single_object["maxx"], single_object["maxy"]
        cv2.rectangle(img_copy, (minx, miny), (maxx, maxy), (0, 255, 0), 3)
        if single_object["male"] ==1:
            cv2.putText(img_copy,"male",((minx + 3),(miny + 13)),font,size,(0,0,255),thick)
        else:
            cv2.putText(img_copy, "female", ((minx + 3), (miny + 13)), font, size, (0, 0, 255), thick)

        if single_object["stand"] ==1:
            cv2.putText(img_copy,"stand",((minx + 3),(miny + 33)),font,size,(0,0,255),thick)
        else:
            cv2.putText(img_copy, "sit", ((minx + 3), (miny + 33)), font, size, (0, 0, 255), thick)

        if single_object["staff"] ==1:
            cv2.putText(img_copy,"staff",((minx + 3),(miny + 53)),font,size,(0,0,255),thick)
        else:
            cv2.putText(img_copy, "customer", ((minx + 3), (miny + 53)), font, size, (0, 0, 255), thick)

        if single_object["play_with_phone"] ==1:
            cv2.putText(img_copy,"play",((minx + 3),(miny + 73)),font,size,(0,0,255),thick)
        else:
            cv2.putText(img_copy, "noplay", ((minx + 3), (miny + 73)), font, size, (0, 0, 255), thick)

    # for single_keypoints in keypoints["object"]: # 51 个点
    #     for i in range(0, len(single_keypoints), 3):
    #         if single_keypoints[i+2] <= 0.05:
    #             continue
    #         cor_x = int(single_keypoints[i])
    #         cor_y = int(single_keypoints[i + 1])
    #         cv2.circle(img_copy, (cor_x, cor_y), 2, p_color[int(i/3)], -1)
    #         # transparency = max(0, min(1, kp_scores[n]))
    #         # img = cv2.addWeighted(bg, transparency, img, 1 - transparency, 0)


    cv2.imwrite(new_img_path + filename,img_copy)





