# ***行人重识别代码*** <br>
## Base_Line_Extract_Features <br>
基于Pytorch，使用Market行人数据集，训练了一个1*2048的输出Resnet,输入一张图片，输出该图片的特征。
[具体训练代码点击前往](https://github.com/layumi/Person_reID_baseline_pytorch)<br>
[本地训练代码点击前往](file:///home/jade/Desktop/Deep_Association_Learning/)
调用方式如下:

```
person_model = RPersonModel(args)
feature = person_model.extract_features(image)
print(feature.shape)
out:(1,2048)
```
Base_Extract_Features目录下存放的提取的特征，以及识别出不同人在的时间。
# Deep_Extract_Features
[具体训练代码点击前往](https://github.com/layumi/Person_reID_baseline_pytorch)

## 2级标题
### 3级标题
#### 4级标题
**这个是粗体** <br>
*这个是斜体* <br>
***这个是粗体加斜体*** <br>



|列名1|列名2|
|:---|:---|
|列1的内容1|列2的内容1|
|列1的内容2|列2的内容2|

[点击前往谷歌搜索的链接](https://www.google.com.hk/)

![](https://github.com/HeTingwei/ReadmeLearn/blob/master/avatar1.jpg)

<img src="https://github.com/HeTingwei/ReadmeLearn/blob/master/avatar1.jpg" width="150" height="150" alt="描述语言，写什么都不会显示出来"/>

<div align=center><img width="150" height="150" src="https://github.com/HeTingwei/ReadmeLearn/blob/master/avatar1.jpg"/></div>
