#coding=utf-8
import numpy as np

def caculate(I1,I2,btntiltle):
    #I1,人工标注的图像，I2自动提取出来的图像
    ca_butou = 0;
    ca_tou = 0;
    rengong_butou =0;
    rengong_tou = 0;
    for i in range(256):
        for j in range(256):
            if (I1[i,j,0] == 0) & (I1[i, j, 1] == 0) &( I1[i,j,2] == 255):
                rengong_butou = rengong_butou+1
            else:
                rengong_tou = rengong_tou + 1
            if (int(I2[i,j,0]) == 255) & (int(I2[i,j,1]) == 255 )& (int(I2[i,j,2]) == 255):
                ca_butou = ca_butou+1;
            else:
                ca_tou = ca_tou + 1;
    acc = [rengong_butou,rengong_tou,ca_butou,ca_tou]

    return acc