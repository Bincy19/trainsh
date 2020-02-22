import cv2

video=cv2.VideoCapture(0)


if(video.isOpened()):
    rval,frame=video.read()
else:
    rval=False

while(rval):
    cv2.imshow("gesture recognisation",frame)
    rval,frame=video.read()
    key=cv2.waitKey(20)
    if(key==27):
        break
cv2.destroyWindow()        


 
