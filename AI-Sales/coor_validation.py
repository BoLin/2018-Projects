def coor(x_input):
    step = 3
    a = []
    for i in range(0, len(x_input), step):
        a.append(x_input[i:i + step])
    for each in a:
        if each[0] < 0 or each[1] < 0 and each[2] >= 0.5:
            return True
    return False

