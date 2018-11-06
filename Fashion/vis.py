import os
import os.path
import numpy as np

from PIL import Image, ImageDraw,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


txt_name = './results/comp4_451b4e81-ad35-4092-ab23-94d589201825_det_test_round_neck.txt'
file_path_img = './JPEGImages'
save_file_path = './detect_results'


source_file = open(txt_name)

img_names = []
for line in source_file:
    staff = line.split()
    img_name = staff[0]
    img_names.append(img_name)

name_dict = {}
for i in img_names:
    if img_names.count(i)>0:
        name_dict[i] = img_names.count(i) 

source_file.close()

source_file = open(txt_name)
for idx in name_dict:
    img = Image.open(os.path.join(file_path_img, idx + '.jpg')) 
    draw = ImageDraw.Draw(img)
    print(idx)
    for i in range(name_dict[idx]):
        line = source_file.readline()
        staff = line.split()
        score = staff[1]
        box = staff[2:6]
        draw.rectangle([int(np.round(float(box[0]))), int(np.round(float(box[1]))), 
                    int(np.round(float(box[2]))), int(np.round(float(box[3])))], outline=(255, 0, 0))
    img.save(os.path.join(save_file_path, idx + '.jpg'))  

source_file.close()
