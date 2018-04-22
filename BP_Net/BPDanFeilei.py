# -*- coding: utf-8 -*-
import numpy as np
from LoadData import  *
from PIL import Image
import scipy.io as sio
from BP import *
import random as RD
from Extract_features import  *
import datetime


def BPNet_dan(file_name):
    rengong_filename = r'C:\Users\Administrator\Desktop\yanshan_rengong1.tif'
    P = []
    T = []
    # butoushui_P = LoadData(1,file_name,rengong_filename)
    # butoushui_P = RD.sample(butoushui_P,2000)
    butoushui_P = sio.loadmat('../JadeLibSVM/' + 'butoushui_P.mat')['butoushui_P']
    M = len(butoushui_P)
    P = butoushui_P.tolist()
    T = [1]*M
    print M



    # toushui_P = LoadData(0,file_name,rengong_filename)
    # toushui_P = RD.sample(toushui_P, 2000)
    toushui_P = sio.loadmat('../JadeLibSVM/' + 'toushui_P.mat')['toushui_P']
    M = len(toushui_P)
    P.extend(toushui_P)
    toushui_P = [0]*M
    T.extend(toushui_P)
    print M


    nn = NeuralNetwork([3,2,1], 'tanh')
    nn.fit(P, T, 0.01, 5000)
    print ('**************训练结束****************')
    p_test = extract_Yanshan('')
    predict_label = []
    for i in p_test:
        predict_label.append(nn.predict(i)[0])
    pic = array(Image.open(file_name))
    X = pic.shape[0]
    Y = pic.shape[1]
    P = pic.shape[2]
    Test_data = np.zeros((X*Y,3),dtype='double');
    k = 0;
    for i in range(X):
        for j in range(Y):
            Test_data[k,0] = pic[i,j,0]
            Test_data[k,1] = pic[i,j,1]
            Test_data[k,2] = pic[i,j,2]
            k = k+1
    result = np.zeros((X,Y,3)) #RGB彩图
    for k in range(X*Y): #  R分量         G分量       B分量
        if(predict_label[k] >= 0.5):
            Test_data[k,0] = 1
            Test_data[k,1] = 1
            Test_data[k,2] = 1   #白色
        elif (predict_label[k] < 0.5):
            Test_data[k,0] = 0
            Test_data[k,1] = 0
            Test_data[k,2] = 0  #%黑色
    k = 0;
    a = array(Image.open(r'C:/Windows/LibSVM_duo.png'))
    for i in range(X):
        for j in range(Y):
            if a[i,j,0] == 0:
                result[i,j,0] = 0
                result[i,j,1] = 0
                result[i,j,2] = 0
            else:
                result[i,j,0] = 1
                result[i,j,1] = 1
                result[i,j,2] = 1
            k = k+1
    return result


if __name__ == '__main__':
    filename = r'C:\Users\Administrator\Desktop\yanshan.tif'