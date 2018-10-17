#

import os

# importing data
rootdir = "../Fashion/root"
count = 0

with open('../Fashion/dir.txt', 'w', encoding='utf-8') as f:

    for dirpath,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            fullfilename = os.path.join(dirpath,filename)
            print(fullfilename)
            f.write(fullfilename + '\n')
            count +=1
print("Data Count =" + str(count))

count_demo = 0
demo_number = 100
flag = 0
with open('../Fashion/dir_demo.txt', 'w', encoding='utf-8') as f:

    for dirpath,dirnames,filenames in os.walk(rootdir):
        if flag == 1:
            break
        for filename in filenames:
            fullfilename = os.path.join(dirpath,filename)
            print(fullfilename)
            f.write(fullfilename + '\n')
            count_demo +=1
            if count_demo == 100:
                flag = 1
                break
