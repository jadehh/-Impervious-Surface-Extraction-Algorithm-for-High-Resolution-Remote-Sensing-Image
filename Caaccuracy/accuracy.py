#coding=utf-8

import numpy as np
from PIL import Image
from pylab import *
import matplotlib.pyplot as plt
from cacl import *

def calaccuracy(filename,bntTitle):
    a_biaozhu = [0, 1, 2, 1.5]
    acc = []
    image = array(Image.open(filename))
    M = image.shape[0]
    N = image.shape[1]
    #判断Image
    if image.size== 1073037 :
        image2 = np.zeros((M, N, 3));
        for i in range(M):
            for j in range(N):
                if image[i, j] == 255:
                    image2[i, j, 0] = 255
                    image2[i, j, 1] = 255
                    image2[i, j, 2] = 255
                else:
                    image2[i, j, 0] = 0
                    image2[i, j, 1] = 0
                    image2[i, j, 2] = 0

        image = image2
    I2 = np.zeros((256,256,3))
    for l in range(4):
        I = array(Image.open('../'+'yanshan'+str(l)+'.png'))
        for i in range(int(256*a_biaozhu[l]),int(256*(a_biaozhu[l]+1))):
            for j in range(int(256*a_biaozhu[l]),int(256*(a_biaozhu[l]+1))):
                I2[i - int(256 * a_biaozhu[l]), j - int(256 * a_biaozhu[l]), 0] = int(image[i, j, 0]);
                I2[i - int(256 * a_biaozhu[l]), j - int(256 * a_biaozhu[l]), 1] = int(image[i, j, 1]);
                I2[i - int(256 * a_biaozhu[l]), j - int(256 * a_biaozhu[l]), 2] = int(image[i, j, 2]);
        print caculate(I, I2, bntTitle)
        acc.append(caculate(I,I2,bntTitle))
    return acc


if __name__ == '__main__':
    calaccuracy(r'C:\Users\Administrator\Desktop/multiksw3.png','BP_Net')