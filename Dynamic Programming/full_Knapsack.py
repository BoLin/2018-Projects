## 4/14/2018 full_Knapsack Bo Lin
import numpy as np
import math

def knapsack_0_1(weight,value,max_weight):
    num = len(weight) ## get the number of distinct items
    dp = np.zeros((num,max_weight+1)) ## initialize dp matrix


    ## transfer function dp[i][j]=max(f[i-1][j],f[i-1][j-weight[i]]+value[i])。

    for i in range(num):
        for j in range(max_weight+1):
            if weight[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] =  max(dp[i-1][j],dp[i-1][j-weight[i]]+ value[i])

    max_value = np.amax(dp).astype(int).astype(str)

    return max_value,dp

def find_item_full(max_weight,dp,weight): ## find the item
    j = max_weight
    num = len(weight)
    in_pack = np.zeros((1,num))## try to find which one is put in the pack
    for i in reversed(range(num)):
        if i != 0 and (dp[i][j] > dp[i-1][j]):
            in_pack[0][i] = 1
            j = j - weight[i]
        if i == 0 and (dp[i][j] > 0):
            in_pack[0][i] = 1
    return in_pack

def full_data(weight,value):
    weight_new = []## define the new weight matrix
    value_new = []
    temp = []
    for i in range(len(weight)):
        iter = math.floor(max_weight/weight[i])
        temp.append(iter)
        for j in range(iter):
             weight_new.append(weight[i])
             value_new.append(value[i])

    return weight_new,value_new,temp


def bag_check(in_pack,temp):
    num = len(temp)
    in_pack_new = np.zeros((1, num))
    start = 0
    for i in range(num):
        stop = start + temp[i]
        in_pack_new[0][i] = sum(in_pack[0][start:stop])
        start = stop
    return in_pack_new


#test
weight = [5,2,2,3,4,5,6]
value  = [3,5,2,2,4,3,4]
max_weight = 10

weight_new,value_new,temp = full_data(weight,value)
max_value,dp = knapsack_0_1(weight_new,value_new,max_weight)
in_pack = find_item_full(max_weight,dp,weight_new)
in_pack_new = bag_check(in_pack,temp)

print('The maximum value is ' + max_value)
print(dp)
print('Weight = ' , weight,'actual weight = ',np.sum(weight_new*in_pack))
print('Value = ',value,'actual value = ',np.sum(value_new*in_pack))
print('In_pack_conclusion',in_pack_new)
