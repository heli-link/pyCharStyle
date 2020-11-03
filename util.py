import os
from datetime import datetime
import cv2
import shutil

def clearFile(file):
    shutil.rmtree(file)
    os.mkdir(file)
# 返回当前时间
def getTime():
    return datetime.now().strftime("%Y%m%d_%H%M%S")
# rgb 转 字符
def getchar(r,g,b):
    # 我们定义的不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号
    ascii_char = list("MNHQ$OC67)oa+>!:+. ")
    length = len(ascii_char)
    unit = (256.0 + 1) / length
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return ascii_char[int(gray / unit)]
# 合成视频
def createVidio(fps,var):
    img = cv2.imread('image/1.jpg')  # 读取第一张图片
    outpath = getTime()+'-color.mp4'
    imgInfo = img.shape
    size = (imgInfo[1], imgInfo[0])  # 获取图片宽高度信息
    print(size)
    #     设置视频格式 MP4
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    videoWrite = cv2.VideoWriter(outpath, fourcc, fps, size)  # 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））
    # videoWrite = cv2.VideoWriter('0.mp4',fourcc,fps,(1920,1080))
    files = os.listdir('image/')
    # 获取图片数量
    out_num = len(files)
    for i in range(0, out_num):
        fileName = 'image/' + str(i) + '.jpg'  # 循环读取所有的图片,假设以数字顺序命名
        img = cv2.imread(fileName)
        videoWrite.write(img)  # 将图片写入所创建的视频对象
        # 进度条
        per = int((i / out_num)*100)
        print('进度:'+str(per)+'%')
        var.set('正在生成视频,进度:'+str(per)+'%')
    videoWrite.release()
    var.set('完成，请在根目录中查看,帧率：'+str(fps))
    # 清除痕迹
    clearFile('image')
def suffix(path):
  suf =  path.split('.')[-1]
  if suf == 'jpg' or suf == 'png' or suf == 'jpeg':
      return 0
  if suf == 'mp4':
      return 1
  else:
      return 2
if __name__ == '__main__':
    print(str(suffix('D:\python\python.exe D:/code/Python/风格转换/main.mp4')))