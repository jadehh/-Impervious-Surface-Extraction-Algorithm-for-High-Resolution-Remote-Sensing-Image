#coding=utf-8
from LoadData import  *
import numpy as np
import os
from svmutil import *
from PIL import Image
import scipy.io as sio
from pylab import *
from Extract_features import  *
import datetime
import os
starttime = datetime.datetime.now()
P = []
T = []


def LibSVMClassIfy(filename):
    rengong_filename = r'C:\Users\Administrator\Desktop\yanshan_rengong1.tif'
    # butoushui_P = LoadData(1,filename,rengong_filename)
    butoushui_P = sio.loadmat('../JadeLibSVM/'+'butoushui_P.mat')['butoushui_P']
    # sio.savemat('butoushui_P.mat',{'butoushui_P':butoushui_P})
    butoushui_P  = butoushui_P.tolist()
    M = len(butoushui_P)
    P = butoushui_P
    T = [1]*M



    # toushui_P = LoadData(0, filename, rengong_filename)
    toushui_P = sio.loadmat('../JadeLibSVM/'+'toushui_P.mat')['toushui_P']
    sio.savemat('toushui_P.mat', {'toushui_P': toushui_P})
    toushui_P = toushui_P.tolist()
    M = len(toushui_P)
    P.extend(toushui_P)
    toushui_P = [0] * M
    T.extend(toushui_P)
    print M

    #训练SVM模型
    model = svm_train(T,P,'-s 0 -t 2 -c 0.1 -g 1 -h 0')

    p_test = extract_Yanshan('')

    M = len(p_test)

    p_label = [0]*M

    #预测
    predict_label = svm_predict(p_label,p_test,model)




    predict_label =  predict_label[0]
    #
    sio.savemat(r'C:\Users\Administrator\Desktop\predict_label.mat',{'predictlabel':predict_label})


    #存储数组
    # predict_label = sio.loadmat(r'C:\Users\Administrator\Desktop\predict_label.mat')  # 读取mat文件
    # predict_label =  predict_label['predictlabel'][0]


    pic = array(Image.open(filename))

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
        if(predict_label[k]== 1):
            Test_data[k,0] = 1
            Test_data[k,1] = 1
            Test_data[k,2] = 1   #白色
        elif (predict_label[k] == 0):
            Test_data[k,0] = 0
            Test_data[k,1] = 0
            Test_data[k,2] = 0  #%黑色
    k = 0;
    a = array(Image.open(r'C:\Windows\BP_Net_duo.png'))
    for i in range(X):
        for j in range(Y):
            if a[i, j, 0] == 0:
                result[i, j, 0] = 0
                result[i, j, 1] = 0
                result[i, j, 2] = 0
            else:
                result[i, j, 0] = 1
                result[i, j, 1] = 1
                result[i, j, 2] = 1
            k = k+1

    return result




if __name__ == '__main__':
    filename = r'C:\Users\Administrator\Desktop\yanshan.tif'
    LibSVMClassIfy(filename)
