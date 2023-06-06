# import cv2
# import sys

# img=cv2.imread("C:\\Users\\lenovo\\Desktop\\py\\PornHub-Downloader\\turtle\\cv\\guge.png")

# if img is None:
#     sys.exit('could find this img')

# cv2.imshow('display this img',img)
# k=cv2.waitKey(0)

# if k==ord('s'):
#     cv2.imwrite('zhuzhu.jpg',img)
import cv2

def gesture_recognition(frame):
    # 缩放图像以适应屏幕
    frame = cv2.resize(frame, (640, 480))
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 对图像进行高斯模糊处理
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # 对图像进行二值化处理
    ret, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # 寻找轮廓
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 寻找最大轮廓
    if len(contours) > 0:
        max_contour = max(contours, key=cv2.contourArea)
        # 计算轮廓的凸包
        hull = cv2.convexHull(max_contour)
        # 计算轮廓的缺陷
        defects = cv2.convexityDefects(max_contour, cv2.convexHull(max_contour, returnPoints=False))
        # 计算缺陷的数量
        count_defects = 0
        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(max_contour[s][0])
                end = tuple(max_contour[e][0])
                far = tuple(max_contour[f][0])
                # 计算缺陷的角度
                angle = cv2.fastAtan2(float(far[1] - start[1]), float(far[0] - start[0]))
                # 计算缺陷的深度
                depth = d / 256.0
                # 判断缺陷是否是手指
                if angle < 90 and depth > 30:
                    count_defects += 1
            # 根据手指数量判断手势
            if count_defects == 0:
                return "rock"
            elif count_defects == 1:
                return "scissors"
            elif count_defects == 2:
                return "paper"
    return None
cap = cv2.VideoCapture(0)
cv2.namedWindow('camera', cv2.WINDOW_NORMAL)
cv2.resizeWindow('camera', 480, 320)
while True:
    # 读取一帧图像
    ret, frame = cap.read()
    
    # 调用手势识别函数
    gesture = gesture_recognition(frame)
    
    # 在图像上显示识别结果
    if gesture is not None:
        cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # if gesture=="one":
        #     print('fuck you mother')
    
    # 显示图像
    cv2.imshow('camera', frame)
    
    # 按下q键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()