# import turtle

# def get_pos(x, y):
#     # t = turtle.Turtle()
#     turtle.hideturtle()
#     turtle.pd()
#     turtle.goto(x, y)
#     turtle.dot(5)
#     # t.pd()
#     print("x坐标为：", x)
#     print("y坐标为：", y)

# turtle.onscreenclick(get_pos)
# screen=turtle.Screen()
# screen.bgcolor("red")
# # turtle.onclick(get_pos)
# turtle.mainloop()
import cv2
import numpy as np

# 定义手势识别函数
def recognize_gesture(frame):
    # 将图像转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 应用高斯模糊
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 二值化处理
    _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    # 找到手掌轮廓
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    # 找到最大的轮廓
    if len(contours) > 0:
        max_contour = max(contours, key=cv2.contourArea)
        
        # 判断手势类型
        if cv2.contourArea(max_contour) > 10000:
            hull = cv2.convexHull(max_contour, returnPoints=False)
            defects = cv2.convexityDefects(max_contour, hull)
            if defects is not None:
                count_defects = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(max_contour[s][0])
                    end = tuple(max_contour[e][0])
                    far = tuple(max_contour[f][0])
                    a = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                    b = np.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                    c = np.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                    angle = np.arccos((b**2 + c**2 - a**2) / (2*b*c)) * 180 / np.pi
                    if angle <= 90:
                        count_defects += 1
                if count_defects == 1:
                    return "one"
                elif count_defects == 2:
                    return "two"
                elif count_defects == 3:
                    return "three"
                elif count_defects == 4:
                    return "four"
                elif count_defects == 5:
                    return "five"
    return None

# 打开摄像头
cap = cv2.VideoCapture(0)
cv2.namedWindow('camera', cv2.WINDOW_NORMAL)
cv2.resizeWindow('camera', 240, 180)
while True:
    # 读取一帧图像
    ret, frame = cap.read()
    
    # 调用手势识别函数
    gesture = recognize_gesture(frame)
    
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
# import cv2
# import numpy as np

# # 读取训练好的SVM模型文件
# svm = cv2.ml.SVM_load('palm.xml')

# # 打开摄像头
# cap = cv2.VideoCapture(0)

# while True:
#     # 读取摄像头中的图像
#     ret, frame = cap.read()

#     # 图像处理，将图像转换为灰度图像并进行二值化处理
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)
#     ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#     # 找到并绘制手掌的轮廓
#     contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cnt = max(contours, key=lambda x: cv2.contourArea(x))
#     cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 2)

#     # 提取手势特征并进行分类
#     x, y, w, h = cv2.boundingRect(cnt)
#     if w > 100 and h > 100:
#         roi = thresh[y:y+h, x:x+w]
#         roi = cv2.resize(roi, (64, 64))
#         hog = cv2.HOGDescriptor((64, 64), (16, 16), (8, 8), (8, 8), 9)
#         features = hog.compute(roi)
#         features = features.reshape(1, -1).astype(np.float32)
#         _, result = svm.predict(features)

#         # 显示识别结果
#         cv2.putText(frame, chr(result[0][0]), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

#     # 显示图像
#     cv2.imshow('frame', frame)

#     # 按下q键退出程序
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import pygame
# from pygame.locals import *
# from sys import exit

# # 初始化pygame
# pygame.init()
# screen = pygame.display.set_mode((640,480), 0, 32)

# # 加载背景图
# background = pygame.image.load('background.jpg').convert()

# # 加载外星人图
# alien = pygame.image.load('alien.png').convert_alpha()

# # 初始化OpenCV
# cap = cv2.VideoCapture(0)

# # 加载SVM模型
# svm = cv2.ml.SVM_load("svm_model.xml")

# # 手势标签
# labels = ['fist', 'palm', 'thumb']

# while True:
#     # 读取摄像头图像
#     ret, frame = cap.read()

#     # 翻转图像
#     frame = cv2.flip(frame, 1)

#     # 转换为灰度图
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # 调整图像大小
#     gray = cv2.resize(gray, (320, 240))

#     # 二值化处理
#     ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

#     # 寻找轮廓
#     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     # 如果存在轮廓
#     if contours:
#         # 寻找最大轮廓
#         max_contour = max(contours, key=cv2.contourArea)

#         # 计算轮廓的凸包
#         hull = cv2.convexHull(max_contour)

#         # 绘制轮廓和凸包
#         cv2.drawContours(frame, [max_contour], -1, (0,255,0), 2)
#         cv2.drawContours(frame, [hull], -1, (255,0,0), 2)

#         # 计算手势特征
#         hand_features = np.zeros((1, 7), dtype=np.float32)
#         hand_features[0, 0] = cv2.contourArea(max_contour)
#         hand_features[0, 1] = cv2.arcLength(max_contour, True)
#         hand_features[0, 2] = hand_features[0, 0] / hand_features[0, 1]
#         (x, y, w, h) = cv2.boundingRect(max_contour)
#         hand_features[0, 3] = w / h
#         hand_features[0, 4] = cv2.mean(thresh[y:y+h, x:x+w])[0]
#         hand_features[0, 5] = cv2.mean(gray[y:y+h, x:x+w])[0]
#         hand_features[0, 6] = cv2.mean(frame[y:y+h, x:x+w])[0]

#         # 预测手势标签
#         label, result = svm.predict(hand_features)

#         # 在屏幕上显示手势标签
#         text = labels[int(label[0])]
#         font = pygame.font.SysFont(None, 48)
#         text_surface = font.render(text, True, (255, 0, 0))
#         screen.blit(text_surface, (320, 240))

#     # 显示摄像头图像
#     cv2.imshow('frame', frame)

#     # 处理pygame事件
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()

#     # 每秒钟刷新30次屏幕
#     pygame.display.update()
#     pygame.time.delay(33)

#     # 按下q键退出程序
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # 释放摄像头和窗口资源
# cap.release()
# cv2.destroyAllWindows()
