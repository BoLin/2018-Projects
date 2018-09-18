import json
import os

file_path = "./label_scene_train"
file_dict = os.listdir(file_path)

file2id = dict()
for single_json in file_dict:
    with open( file_path +"/"+ single_json) as f:
        data = json.load(f)
    filename = data["annotation"][0]["filename"]
    image_id = data["annotation"][0]["image_id"]
    file2id[filename] = image_id

result_path = "file2id.json"
with open(result_path,'w') as f:
    json.dump(file2id,f)
print("===============OVER==============")
