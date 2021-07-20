import cv2
import numpy as np
cap=cv2.VideoCapture(0)

#defining empty functoion
def empty(self):
    pass

#creating hsv bars
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("hue_min","HSV",0,180,empty)
cv2.createTrackbar("hue_max","HSV",180,180,empty)
cv2.createTrackbar("sat_min","HSV",0,255,empty)
cv2.createTrackbar("sat_max","HSV",255,255,empty)
cv2.createTrackbar("val_min","HSV",0,255,empty)
cv2.createTrackbar("val_max","HSV",255,255,empty)

#video capture
while True:
    success,video=cap.read()

    HSV_conv=cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
    hue_min=cv2.getTrackbarPos("hue_min","HSV")
    hue_max=cv2.getTrackbarPos("hue_max","HSV")
    sat_min=cv2.getTrackbarPos("sat_min","HSV")
    sat_max=cv2.getTrackbarPos("sat_max","HSV")
    val_min=cv2.getTrackbarPos("val_min","HSV")
    val_max=cv2.getTrackbarPos("val_max","HSV")
    #creating upper and lower
    lower=np.array([hue_min,sat_min,val_min])
    upper=np.array([hue_max,sat_max,val_max])
    #creating mask
    mask=cv2.inRange(HSV_conv,lower,upper)
    color_det=cv2.bitwise_and(video,video,mask=mask)
    #cv2.imshow("video",video)
    #cv2.imshow("hsv",HSV_conv)
    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hstack=np.hstack([video,mask])

    cv2.imshow("coldet",color_det)
    cv2.imshow("stack",hstack)
    cv2.resizeWindow("coldet",450,450)
    #cv2.imshow("mask",mask)
    if cv2.waitKey(1)==ord("s"):
        break

cap.release()
cv2.destroyAllWindows()
