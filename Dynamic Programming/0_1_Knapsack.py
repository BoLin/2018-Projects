## 4/9/2018 Knapsack Bo Lin
import numpy as np

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

def find_item(max_weight,dp,weight): ## find the item
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

#test
weight = [1,2,2,3,4,5,6,3,5]
value  = [3,5,2,2,4,3,4,9,4]
max_weight = 13
max_value,dp = knapsack_0_1(weight,value,max_weight)
in_pack = find_item(max_weight,dp,weight)

print('The maximum value is ' + max_value)
print(dp)
print('Weight = ' , weight,'actual weight = ',np.sum(weight*in_pack))
print('Value = ',value,'actual value = ',np.sum(value*in_pack))
print('In_pack= ',in_pack)
