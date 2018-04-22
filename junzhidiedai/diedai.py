#coding=utf-8

import cv2 as cv
import numpy as np
from Otsu.otsu import otsu_fenge
import matplotlib.pylab as plt
def junzhi(filename):
    src = cv.imread(filename)
    B = cv.cvtColor(src, cv.COLOR_BGR2GRAY)   #转换了灰度化
    T=0.5*(float(B.max())+float(B.min()))
    d=False;
    # 通过迭代求最佳阈值
    while ~d:
        g = B >= T;
        Tn = 0.5 * (np.mean(B[g]) + np.mean(B[~g]))
        d = np.abs(T - Tn) < 0.5;
        T=Tn;

    image = otsu_fenge(B,T)
    print '均值迭代法的阈值'
    print T
    return image



