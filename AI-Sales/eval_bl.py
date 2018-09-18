#!/usr/bin/python
# -*- coding: utf-8 -*-
# evaluation program
import os

def Calculation(label_coordinate, forecast_coordinate):
    # 标注矩形左上角坐标为(lx0, ly0)，右下角坐标为(rx0, ry0)，宽为w0，高为h0，
    # 预测矩形左上角坐标为(lx1, ly1)，右下角坐标为(rx1, ry1)，宽为w1，高为h1
    lx0, ly0, rx0, ry0 = label_coordinate
    lx1, ly1, rx1, ry1 = forecast_coordinate
    dlx = abs(lx0 - lx1) / float(rx0 - lx0)
    dly = abs(ly0 - ly1) / float(ry0 - ly0)
    drx = abs(rx0 - rx1) / float(rx0 - lx0)
    dry = abs(ry0 - ry1) / float(ry0 - ly0)
    e = dlx + dly + drx + dry

    return e


if __name__ == "__main__":

    #with open('filename_id.csv', 'r') as ff:
    #    lines_id = ff.read().splitlines()

    with open('val_result_gender_918.json', 'r') as Jf:
        val_json = Jf.read()
    val_json = eval(val_json)

    train_root = './label_scene_train/'
    P0 = 0
    p1 = 0
    n = 0  # n为(标注)对象总数，理解为框
    summ = 0
    N = 0  # N为图片总数
    Ti = 0
    T = 0
    Di = 0
    flag = 0
    objects = 0

    for dirpath,dirnames,filenames in os.walk(train_root):
        for filename in filenames:
            if filename == ".DS_Store":
                pass
            else:
                with open(os.path.join(dirpath, filename), 'r') as jf:
                    train_json = jf.read()
                train_json = eval(train_json)
                # print(train_json)
                image_id = train_json["annotation"][0]["image_id"]  # id_7741好像有问题
                #print(image_id)
                for image_dict in val_json["results"]: # 遍历val 匹配
                    if image_id == image_dict["image_id"]:
                        T = 0  # 如果找到才开始
                        Ti = 0
                        n += len(image_dict["object"]) # 直接加上 标注的object个数
                        # print("find it！")
                        # print(train_json["annotation"][0]["filename"])
                        flag = 1  # 示意已经在val_json 中找到文件可以停止循环
                        if train_json["annotation"][0]["object"] == []: # 如果图上没人 ex.scene_4_00626.jpg
                            print("error label")
                            break
                        for single_object in train_json["annotation"][0]["object"]:
                            objects +=1 # 统计object数量
                            label_coordinate = (single_object["minx"], single_object["miny"], single_object["maxx"], single_object["maxy"])
                            T += 6  # 每多一个object 多六个T
                            e = list()
                            for forecast_object in image_dict["object"]:
                                forecast_coordinate = (forecast_object["minx"], forecast_object["miny"], forecast_object["maxx"], forecast_object["maxy"])
                                e.append(Calculation(label_coordinate, forecast_coordinate))

                            if min(e) <= 0.25:
                                forecast_object = image_dict["object"][e.index(max(e))]
                                summ += forecast_object["confidence"]

                                if single_object["gender"] == 1:

                                    if (forecast_object["female"] > forecast_object["male"]) and (forecast_object["female"] >= 0.5):
                                        Ti += 2
                                else:  # gender == 0
                                    if (forecast_object["female"] < forecast_object["male"]) and (forecast_object["male"] >= 0.5):
                                        Ti += 2

                                if single_object["staff"] == 1:
                                    if (forecast_object["staff"] > forecast_object["customer"]) and (forecast_object["staff"] >= 0.5):
                                        Ti += 2
                                else:
                                    if (forecast_object["customer"] > forecast_object["staff"]) and (forecast_object["customer"] >= 0.5):
                                        Ti += 2

                                if single_object["stand"] == 1:
                                    if (forecast_object["stand"] > forecast_object["sit"]) and (forecast_object["stand"] >= 0.5):
                                        Ti += 2
                                else:
                                    if (forecast_object["sit"] > forecast_object["stand"]) and (forecast_object["sit"] >= 0.5):
                                        Ti += 2

                                if single_object["play_with_phone"] == 1:
                                    if forecast_object["play_with_phone"] >= 0.5:
                                        Ti += 1
                                else:
                                    if forecast_object["play_with_phone"] < 0.5:
                                        Ti += 1
                                #break # 打分好之后跳出for 循环 此处有问题


                    # if T == 0:
                    #     print(train_json["annotation"][0]["object"])
                    #     print(image_id)
                    if flag == 1:
                        break
                if T != 0:
                    Di += Ti / T #图片i
                    # print([Ti, T, Ti/T])
                if flag == 0:
                    print("mismatch")
                flag = 0 # reset
                N += 1
    print("summ and n is: {}, {}".format(summ, n))
    print("Di and N is: {}, {}".format(Di, N))
    print("Ti and T is: {}, {}".format(Ti, T))
    print("Total objects (bbox): {}".format(objects))
    P0 = summ / n
    P1 = Di / N
    print("P0 is: {}".format(P0))
    print("P1 is: {}".format(P1))
    P = 0.3 * P0 + 0.7 * P1     
    print("The final score of the forcast: {}".format(P))
