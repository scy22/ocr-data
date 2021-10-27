#导入库
import json
import numpy as np
import json
import cv2
import matplotlib.pyplot as plt

path = 'img/6.json' #json文件路径
with open(path,'r') as f: 
    data = json.load(f)
#print(data)
#print(data['bbox'])
# print(data['bbox'][0][0])
#data中每个元素都是嵌套的字典
img = cv2.imread('img/6.jpg') #读入图像
copyimg=img.copy()#拷贝一份，不拷贝容易出错
list = []
list = list + data['bbox']
for i in range(len(list)): 
    pts = np.array([[list[i][0],list[i][1]],[list[i][2],list[i][3]],[list[i][4],list[i][5]],[list[i][6],list[i][7]]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(copyimg,[pts],True,(0,0,255))
# 图片保存
#参数1是路径，要包括保存的名字和格式，参数2是来源图片
cv2.imwrite('img/q.jpg',copyimg)




