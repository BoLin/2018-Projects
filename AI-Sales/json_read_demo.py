# a demo code to read json file from LabelImg or Labelme
import json
with open("demo (10).json") as f: # read demo (10)
    result = json.load(f)
for i in range(len(result.get('shapes'))): # read each label from Labelme
    print(result.get('shapes')[i])
    
#print(result.get('annotation').get('object')[1].get('bndbox')) # labelImg file
