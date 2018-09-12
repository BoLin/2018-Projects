# scene detect and sorting based on Dhash hamming distance

import os
from PIL import Image
import DHash

hash_lib = []  # create an empty set to store hash
hash_lib_dict = dict()
k = 35  # hash distance tolerance
file_path = "./Test/Scene_detect/"
file_dict = os.listdir(file_path)

for file_name in file_dict:
    img = Image.open(file_path + file_name)
    hash_new = DHash.calculate_hash(img) # new hash
    img_c = img.copy()
    if not hash_lib:  # empty lib

        hash_lib.append(hash_new)
        folder_name = file_name.split(".")[-2]
        os.mkdir("./" + folder_name)
        img_c.save( "./" + folder_name + "/" + file_name )  #file_path + folder_name + "/"+
        hash_lib_dict[hash_new] = folder_name # new dict added
    else:  # hashes in lib
        flag = 0
        for hash_old in hash_lib: # compare it to every hash
            if DHash.hamming_distance(hash_old, hash_new) < k:
                img_c.save("./" + hash_lib_dict[hash_old] + "/" + file_name)  #file_path +
                flag = 1
                break
        if flag == 0: # unique scene
            folder_name = file_name.split(".")[-2]
            os.mkdir("./" + folder_name)
            img_c.save("./" + folder_name + "/" + file_name)  #file_path +
            hash_lib_dict[hash_new] = folder_name  # new dict added
print(hash_lib_dict)
