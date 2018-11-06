import os
import shutil
import xml.etree.ElementTree as ET

image_path = './JPEGImages/'
annotation_path = './2.0/label_all/'
bin_path = "./bin/"


def parse_rec(filename):
    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)
    a = tree.findall('object')
    if a == []:
        return True
    else:
        return False


image_dir = os.listdir(image_path)

count = 0
for image_name in image_dir:
    #print(image_name)
    xml_name = annotation_path + image_name.split('.')[0] + ".xml"
    if parse_rec(xml_name): # 如果没有找到，需要移除加删除
        count += 1
        print("delete " + image_name)


        # 先备份再删除

        shutil.copyfile(xml_name,bin_path + xml_name.split("/")[-1])
        shutil.copyfile(image_path + image_name,bin_path + image_name)
        os.remove(xml_name)
        os.remove(image_path + image_name)




print(count)







