#coding=utf-8
import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5)  # 从list中随机获取5个元素，作为一个片断返回
print slice
print list  # 原有序列并没有改变