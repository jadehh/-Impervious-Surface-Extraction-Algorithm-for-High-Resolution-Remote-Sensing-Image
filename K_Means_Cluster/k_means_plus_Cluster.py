#coding=utf-8
from pylab import *
from scipy.cluster.vq import *
import scipy.io as sio
from PIL import Image
from Extract_features import *
import k_means_plus
from fenge import *
#添加中文字体支持

from matplotlib.font_manager import FontProperties

def K_means_plus_Cluster(k,filename):
    features = extract_features(filename)
    centroids,variance = k_means_plus.lloyd(features,k) #分成多少类
    code,distance = vq(features,centroids)
    code = code_Sort(code,k)
    result = EX_Fenge(code,filename,k)


    return result
