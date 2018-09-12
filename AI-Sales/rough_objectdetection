from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detect_person = detector.CustomObjects(person=True)

file_path = "./scene_5_val"
file_dict = os.listdir(file_path)
count = 0
bbox = []
for image_name in file_dict:
    name = file_path + "/"+ image_name
    result_path = "./result"
    detections = detector.detectCustomObjectsFromImage(custom_objects=detect_person, minimum_percentage_probability =20, input_image=os.path.join(execution_path, name),
                                                 output_image_path=os.path.join(result_path, image_name))
    for eachObject in detections:
        bbox.append(eachObject["box_points"].tolist())
    count+=1
    if count ==10:
        break
file = open("bbox.txt",'w')
for i in bbox:
    file.write(str(i))
    file.write('\n')
file.close()
