基于python 3.8 open cv
图片转字符 升级版，顺便加了个 GUI
下载链接：

- csdn ：https://blog.csdn.net/qq_42733641/article/details/109458964

### 界面及使用
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201103084502258.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNzMzNjQx,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201103084507118.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNzMzNjQx,size_16,color_FFFFFF,t_70#pic_center)
复选框选择对应的转换格式，在下方会出现字符选择器和颜色选择器，点击即可选择
图片转换时，界面会卡顿，表现为按钮按下去不会回弹，正常现象，是因为没有加线程，反正只要几秒钟，不影响
转换完成的图片视频在软件根目录
视频转换请勿使用高分辨率，速度太慢，当然输入分辨率越高，转换后的分辨率也高
参考 ： i5-7200u 实测 500x300 mp4, 每秒只能处理 1.5 帧
### 效果（这里只能上图，视频就不做展示，效果参考图片）
##### - 原图
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201102221539182.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNzMzNjQx,size_16,color_FFFFFF,t_70#pic_center)
###### -图片转 txt
图片转 txt文本
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020110222172739.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNzMzNjQx,size_16,color_FFFFFF,t_70#pic_center)
###### - 图片转指定字符-jpg彩色 
 同一个字符，通过颜色的变换展现出图像
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020110222181414.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNzMzNjQx,size_16,color_FFFFFF,t_70#pic_center)
###### - 图片转字符-jpg彩色
图片转txt 顺便在添加个颜色
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201102221855314.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNzMzNjQx,size_16,color_FFFFFF,t_70#pic_center)
###### - 图片转字符-jpg指定颜色  
不同字符组成的图片，通过指定颜色可以实现，黑白，彩色字符图
绿色貌似不太好，慎用
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201102222308843.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNzMzNjQx,size_16,color_FFFFFF,t_70#pic_center)

### 目录：
- cvimg   图像处理，opencv
- delete  删除的部分代码，总感觉以后有用
- main    GUI 界面
- text       通用文本信息
- util        工具类