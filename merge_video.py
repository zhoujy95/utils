import cv2
import numpy as np
 
INPUT_FILE1 = 'source1.avi'
INPUT_FILE2 = 'source2.avi'
OUTPUT_FILE = 'merge.avi'
 
reader1 = cv2.VideoCapture(INPUT_FILE1)
reader2 = cv2.VideoCapture(INPUT_FILE2)
width = int(reader1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(reader1.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter(OUTPUT_FILE,
              cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), # (*"mp4v") for mp4 output
              30, # fps
              (width, height//2)) # resolution
 
print(reader1.isOpened())
print(reader2.isOpened())
have_more_frame = True
c = 0
while have_more_frame:
    have_more_frame, frame1 = reader1.read()
    if have_more_frame:
        have_more_frame, frame2 = reader2.read()
    if have_more_frame:
        frame1 = cv2.resize(frame1, (width//2, height//2))
        frame2 = cv2.resize(frame2, (width//2, height//2))
        img = np.hstack((frame1, frame2))
        cv2.waitKey(1)
        writer.write(img)
        c += 1
        print(str(c) + ' is ok')
 
 
writer.release()
reader1.release()
reader2.release()
cv2.destroyAllWindows()
