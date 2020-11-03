import time
import cv2
import util as u
from PIL import Image, ImageDraw, ImageFont

# 图片转字符文本
def getTxt(src):
    txt = ""
    path = u.getTime() + '-txt.txt'
    file = open(path, 'w')
    img = cv2.imread(src)
    # 调整图片大小
    img = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 8.5)))
    # 遍历像素
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r, g, b = img[i, j]
            txt += u.getchar(r,g,b)
        txt += "\n"
    file.write(txt)
    file.close()
    return txt,img.shape[1],img.shape[0]

#     图片转字符图片 两种模式
#  mode 0/固定字符/str
#       1/彩色
#       2/指定颜色/color
def img_txtimg(src, msg='o', mode=0, color = '#000000', outpath=None, isvedio=False):
    start = time.time()
    img = cv2.imread(src)
    if outpath == None:
        outpath = u.getTime() + '-color.jpg'
    # 字符间隔
    if isvedio:
        coe = 10
        font = ImageFont.truetype("‪C:\\Windows\\Fonts\\AdobeHeitiStd-Regular.otf", coe + 5)  # 设置字体
    else:
        coe = 25
        font = ImageFont.truetype("‪C:\\Windows\\Fonts\\AdobeHeitiStd-Regular.otf", coe+10)  # 设置字体
    img = cv2.resize(img, (int(img.shape[1] * 0.2), int(img.shape[0] * 0.2)))
    H = img.shape[0]*coe
    W = img.shape[1]*coe
    # 创建画布
    im_txt = Image.new("RGB", (W, H), (220, 220, 220))
    dr = ImageDraw.Draw(im_txt)
    x=y = 0
    # 设置字体

    # font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\Gill Sans\\GILSANUB.TTF", coe)  # 设置字体

    # 遍历像素 转成字符
    index = 0
    buf = 0
    first = time.time()
    for i in range(0, img.shape[0]):
            two = time.time()
            for j in range(0, img.shape[1]):
                r, g, b = img[i, j]
                # 指定字符
                if mode == 0:
                    # 指定字符绘制
                    dr.text([x, y], msg, (r, g, b), font)
                if mode == 1:
                    msg = u.getchar(r, g, b)
                    dr.text([x, y], msg, (r, g, b,), font)  # 彩色
                if mode == 2:
                    msg = u.getchar(r, g, b)
                    dr.text([x, y], msg, color, font)  # 指定颜色
                x += coe
                index+=1
            buf = index
            index = 0
            three = time.time()
            y += coe
            x = 0
    fore = time.time()
    #     保存字符图片
    im_txt.save(outpath,encoding='utf-8')
    three = time.time()
    print("1=" + str(first - start) + '--> '+str(buf)+'次=' + str(three - two) + '--> 3=' + str(three - two))
#     视频转字符 mode
# 0: '视频转指定字符mp4-原彩'
# 1: '视频转字符jpg-原彩'
# 2: '图片转字符jpg-指定颜色'
def vidio_txtimg(src,mode,msg='o',color=(255,255,255),var=None):
    # 清空文件夹
    u.clearFile('image')
    vidio = cv2.VideoCapture(src)
    # 获取原视频帧率
    fps = vidio.get(5)
    c = 0
    while True:
        start = time.time()
        check, frame = vidio.read()
        if check:

            src = 'image/'+str(c)+'.jpg'
            # 视频抽帧 转换
            cv2.imwrite(src,frame)
            # '视频转指定字符mp4-原彩'
            if mode == 0:
                img_txtimg(src, mode=0, msg=msg, outpath=src, isvedio=True)

            #  '视频转字符mp4-原彩'
            if mode == 1:
                img_txtimg(src,mode=1,outpath=src,isvedio=True)

            #  '图片转字符mp4-指定颜色'
            if mode == 2:
                img_txtimg(src,mode=2,color=color,outpath=src,isvedio=True)

            # 实时播放
            # img = cv2.imread(src)
            # cv2.imshow("frame",cv2.imread(src))
            c += 1
            var.set('正在处理第'+str(c)+'帧')
        else:
            break
        cv2.waitKey(1)
        end = time.time()
        print('帧率：'+str(1/(end-start)))
    print('帧数：' + str(c))
    vidio.release()
    u.createVidio(fps,var)

if __name__ == '__main__':
    img_txtimg('icon/color.png', mode=2)