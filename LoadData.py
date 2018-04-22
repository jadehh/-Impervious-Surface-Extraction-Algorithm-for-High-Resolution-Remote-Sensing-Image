#coding=utf-8
import numpy as np
from PIL import Image
import os
from pylab import *
# np.set_printoptions(threshold=np.inf)
# dataset = []
# def LoadData(directory):
#     files = os.listdir(directory)
#     i = 0
#     for file in files:
#         I = array(Image.open(directory+'/'+file))
#         R = I[:,:,0]
#         G = I[:,:,1]
#         B = I[:,:,2]
#     # %灰度值归一化
#         R=double(R)/(255)
#         G=double(G)/(255)
#         B=double(B)/(255)
#         M = shape(R)[0]
#         N = shape(R)[1]
#         R = reshape(R, [1, M * N])
#         G = reshape(G, [1, M * N])
#         B = reshape(B, [1, M * N])
#     # %初始化输入矢量P和输出矢量T
#         P=[]
#         T=[]
#         P = np.row_stack((R,G,B))
#         if i==0:
#             dataset = P
#         else:
#             dataset = np.column_stack((dataset, P))
#         i = i+1
#     dataset = np.transpose(dataset)
#     return dataset

#提取颜色特征

def LoadData(kinds,filename,rengong_filename):
    I = array(Image.open(rengong_filename))
    orignal_Image = array(Image.open(filename))
    M = orignal_Image.shape[0]
    N = orignal_Image.shape[1]
    dataset = []
    run = 0
    for i in range(M):
        for j in range(N):
            R = I[i,j,0]
            G = I[i,j,1]
            B = I[i,j,2]
            if kinds == 0:
                if (R==0) & (G == 0) & (B == 0) or (R==255) & (G == 165) & (B == 0) or (R==0) & (G == 255) & (B == 0):   #黑色黄色绿色表示水面
                    feature_R = double(orignal_Image[i,j,0]) / 255.0
                    feature_G = double(orignal_Image[i,j,1]) / 255.0
                    feature_B = double(orignal_Image[i,j,2]) / 255.0
                    if feature_B != 0:
                        P = np.row_stack((feature_R,feature_G,feature_B))
                        if run == 0:
                            dataset = P
                        else:
                            dataset = np.column_stack((dataset,P))
                        run = run + 1
            else:
                if (R==0) & (G == 0) & (B == 255) or (R==255) & (G == 255) & (B == 255):   #蓝色和白色为不透水面
                    feature_R = double(orignal_Image[i,j,0]) / 255.0
                    feature_G = double(orignal_Image[i,j,1]) / 255.0
                    feature_B = double(orignal_Image[i,j,2]) / 255.0
                    if feature_B != 1:
                        P = np.row_stack((feature_R,feature_G,feature_B))
                        if run == 0:
                            dataset = P
                        else:
                            dataset = np.column_stack((dataset,P))
                        run = run + 1

    dataset = np.transpose(dataset)
    return dataset




if __name__ == '__main__':
    filename = r'C:\Users\Administrator\Desktop\yanshan.tif'
    rengong_filename = r'C:\Users\Administrator\Desktop\yanshan_rengong.tif'
    features = LoadData(0,filename,rengong_filename)
    print features.shape