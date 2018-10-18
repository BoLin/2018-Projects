import cv2
import os
import shutil

# load data dir
dir = '../Fashion/dir.txt'
f = open(dir,'r')
data_dir = f.read().split("\n")

new_dir = '../Fashion/All/'
# 待定的命名
# old_path = ./Maison-Martin-Margiela/2018-aw-RTW/_ARC0100h.jpg.360X540
# new_path = ./MMM_18awR_ARC0100h.jpg
# read data
error = 0
for each_pic in data_dir:
    img = cv2.imread(each_pic)
    #print(pic)
    cv2.namedWindow("Image")
    try:
        cv2.imshow("Image", img)
    except cv2.error:
        error +=1
        print("fail to load")
    else:
        cv2.waitKey(10)
        cv2.destroyAllWindows()

        brand = each_pic.split("/")[5].split("\\")[1]
        season = each_pic.split("/")[5].split("\\")[2]
        name = each_pic.split("/")[5].split("\\")[3].split(".")[0]

        shutil.copyfile(each_pic, new_dir + brand + season + name + ".jpg")
print(error)
