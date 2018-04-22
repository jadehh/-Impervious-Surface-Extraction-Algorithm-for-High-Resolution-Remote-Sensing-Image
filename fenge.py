# coding=utf-8
import scipy.io as sio

from pylab import *
from PIL import Image


def code_Sort(code,k):
    func = lambda x, y: x if y in x else x + [y]
    codelist = reduce(func, [[], ] + code.tolist())

    for i in range(code.shape[0]):
        for j in range(k):
            if code[i] == codelist[j]:
                code[i] = j
                break
    return code

# 透水面与不透水面分割
def fengge(code, infile_empire, k):
    fanwei = []
    if k == 2 or k == 3:
        fanwei = [0]
    elif k==4:
        fanwei = [0]
    elif k == 5:
        fanwei = [0, 1]
    elif k == 7:
        fanwei = [0, 1, 6]
    elif k == 9:
        fanwei = [0, 1, 5, 8]
    predict_label = code
    im = array(Image.open(infile_empire))
    image_shape = im.shape[:2]
    X = image_shape[0]
    Y = image_shape[1]
    TestData = np.zeros((X * Y, 3))
    # R,G,B分量
    # K = 2 时,从聚类图中可以看出紫色为不透水面, predict_label[run] == 0
    # K = 3 时,从聚类图中可以看出蓝色 predict_label[run] == 2
    # K = 5 时,从聚类图中可以看出黑色,和青色是不透水面 predict_label[run] == 4 or predict_label[run] == 3
    # K = 7 时,从聚类图中可以看出紫色,蓝色黑色是不透水面 (predict_label[run] == 5 or predict_label[run] == 0  or predict_label[run] == 3
    for run in range(X * Y):
        if (predict_label[run] in fanwei):
            TestData[run, 0] = 1
            TestData[run, 1] = 1
            TestData[run, 2] = 1
        else:
            TestData[run, 0] = 0
            TestData[run, 1] = 0
            TestData[run, 2] = 0

    result = np.zeros((X, Y, 3))  # RGB彩色图像
    run = 0
    for i in range(X):
        for j in range(Y):
            result[i, j, 0] = TestData[run, 0]
            result[i, j, 1] = TestData[run, 1]
            result[i, j, 2] = TestData[run, 2]
            run = run + 1
    return result



# 透水面与不透水面分割
def OTSU_fenge(im,m):
    X = im.shape[0]
    Y = im.shape[1]
    TestData = np.zeros((X , Y))
    for i in range(X):
        for j in range(Y):
            if im[i][j] == (len(m)-1) :
                TestData[i,j] = 255
            else:
                TestData[i, j] = 0
    return TestData

# 矩阵转成图像
def MatrixToImage(data):
    data = data * 255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im

if __name__ == '__main__':
    C = 3
    seg_I = sio.loadmat('seg_I.mat')
    seg_I = seg_I['seg_I']
    seg_I_shape = seg_I.shape
    M = seg_I_shape[0]
    N = seg_I_shape[1]
    I = np.zeros((M,N,3))
    for i in range(M):
        for j in range(N):
            if seg_I[i,j] < 2:
                I[i, j, 0] = 0
                I[i, j, 1] = 0
                I[i, j, 2] = 0
            else:
                I[i, j, 0] = 1
                I[i, j, 1] = 1
                I[i, j, 2] = 1

    axis('off')
    imshow(I)
    show()
