import cv2
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,360)
# logo = cv2.imread('C:\\Users\\lenovo\\Desktop\\1.jpg')
# cv2.imshow('logo', logo)
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow('video',frame)
    key = cv2.waitKey(1)
    if(key & 0xFF == ord('q')): 
        break
cap.release()
cv2.destroyAllWindows()
