# in order to extract frames from a long video, this simple code is written to do the job.
import cv2
def get_video_pic(name):
    cap = cv2.VideoCapture(name)
    n = 3 #  unit:s  
    n_frame = n * 16  # the dataset I have has an fps of 16
    frame_count = cap.get(7) # total frame count
    #return print(frame_count)
      
    for i in range(int(frame_count/n_frame)): # 
        cap.set(1, n_frame * i) # get frame
        rval, frame = cap.read() # if rval = false, there is issue with the videl clip
        if rval:
            cv2.imwrite(name[:-4]+'_%d'%(i)+'.jpg',frame)  # save as jpg
        else:
            print('fail')
    cap.release()# close file

start = 4001 # this is for handling multiple files with the same name format
stop = 4018
for j in range(start,stop):
	get_video_pic("video_%d.avi"%j)
