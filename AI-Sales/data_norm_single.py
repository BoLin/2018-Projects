def data_norm_coor(x, y, x0, y0, w, h):
    x_norm = (x - x0)/w
    y_norm = (y - y0)/h
    return x_norm, y_norm


def data_norm(single_data):
    width = single_data[2] - single_data[0]
    height = single_data[3] - single_data[1]
    single_data[4], single_data[5] = data_norm_coor(single_data[4], single_data[5], single_data[0], single_data[1], width,height)# 0
    single_data[7], single_data[8] = data_norm_coor(single_data[7], single_data[8], single_data[0], single_data[1], width,height)# 1
    single_data[10], single_data[11] = data_norm_coor(single_data[10], single_data[11], single_data[0], single_data[1], width,height)# 2
    single_data[13], single_data[14] = data_norm_coor(single_data[13], single_data[14], single_data[0], single_data[1], width,height)# 3
    single_data[16], single_data[17] = data_norm_coor(single_data[16], single_data[17], single_data[0], single_data[1], width,height)# 4
    single_data[19], single_data[20] = data_norm_coor(single_data[19], single_data[20], single_data[0], single_data[1], width,height)# 5
    single_data[22], single_data[23] = data_norm_coor(single_data[22], single_data[23], single_data[0], single_data[1], width,height)# 6
    single_data[25], single_data[26] = data_norm_coor(single_data[25], single_data[26], single_data[0], single_data[1], width,height)# 7
    single_data[28], single_data[29] = data_norm_coor(single_data[28], single_data[29], single_data[0], single_data[1], width,height)# 8
    single_data[31], single_data[32] = data_norm_coor(single_data[31], single_data[32], single_data[0], single_data[1], width,height)# 9
    single_data[34], single_data[35] = data_norm_coor(single_data[34], single_data[35], single_data[0], single_data[1], width,height)# 10
    single_data[37], single_data[38] = data_norm_coor(single_data[37], single_data[38], single_data[0], single_data[1], width,height)# 11
    single_data[40], single_data[41] = data_norm_coor(single_data[40], single_data[41], single_data[0], single_data[1], width,height)# 12
    single_data[43], single_data[44] = data_norm_coor(single_data[43], single_data[44], single_data[0], single_data[1], width,height)# 13
    single_data[46], single_data[47] = data_norm_coor(single_data[46], single_data[47], single_data[0], single_data[1], width,height)# 14
    single_data[49], single_data[50] = data_norm_coor(single_data[49], single_data[50], single_data[0], single_data[1], width,height)# 15
    single_data[52], single_data[53] = data_norm_coor(single_data[52], single_data[53], single_data[0], single_data[1], width,height)# 16
    input_value_norm = single_data[4:] # data norm and trim
    # print([single_data[4:]])
    return input_value_norm

