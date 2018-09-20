# 清洗 IOU太高的重复框
import os
import json

box_path = "./json_result_bot_val_gender(0.8)/"
#box_path = "./json_result_bot_val_customer_staff(0.8)/"
box_dir = os.listdir(box_path)
new_bbox_path = "./json_result_bot_val_gender_wash/"
#new_bbox_path = "./json_result_bot_val_customer_staff_wash/"

def IOU(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = (xB - xA + 1) * (yB - yA + 1)

    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou

duplicate = 0
small = 0
for single_json in box_dir:
    with open(box_path + single_json) as bf:
        bboxes_raw = json.load(bf)
    bboxes = bboxes_raw["annotation"][0]["object"]
    # create new bbox json
    new_bbox = dict()
    new_bbox["annotation"] = [{"object": []}]


    for i in range(len(bboxes)):
        boxA = [bboxes[i]["minx"], bboxes[i]["miny"], bboxes[i]["maxx"], bboxes[i]["maxy"]]
        for j in range(len(bboxes)):
            boxB = [bboxes[j]["minx"], bboxes[j]["miny"], bboxes[j]["maxx"], bboxes[j]["maxy"]]
            iou = IOU(boxA, boxB)
            if iou >= 0.9 and j > i: # find IOU too high
                duplicate +=1
                break
        if (boxA[2] - boxA[0]) <= 50 and (boxA[3] - boxA[1]) <= 50:
            small += 1
        else:
            new_bbox["annotation"][0]["object"].append(bboxes[i])
    with open(new_bbox_path + single_json, 'w') as rf:
        json.dump(new_bbox, rf)
        print(single_json)

print("Delete %d duplicate boxes"%(duplicate) )
print("Delete %d small boxes"%(small) )
