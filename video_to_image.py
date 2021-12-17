# 导入所需要的库
import cv2
import numpy as np


# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型
def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address, image)


# 将视频文件逐帧提取，然后保存在out文件中
# 读取视频文件
videoCapture = cv2.VideoCapture("test.mp4")
# 通过摄像头的方式
# videoCapture=cv2.VideoCapture(1)
# 读帧
success, frame = videoCapture.read()
i = 0
while success:
    i = i + 1
    # 保存每一帧图片
    save_image(frame, './out/image', i)
    if success:
        print('save image:', i)
    if i == 100:
        break
    success, frame = videoCapture.read()
