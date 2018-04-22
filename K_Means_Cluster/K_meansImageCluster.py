#coding=utf-8

from pylab import *
from scipy.cluster.vq import *
from PIL import Image
from fenge import *
from Extract_features import *

#添加中文字体支持

def K_means_Cluster(k,filename):
    features = extract_features(filename)
    centroids,variance = kmeans(features,k) #分成多少类
    code,distance = vq(features,centroids)
    code = code_Sort(code,k)
    result = EX_Fenge(code,filename,k)
    return result



