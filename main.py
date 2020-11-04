import threading
import tkinter
from io import BytesIO
from tkinter import filedialog

import requests
from PIL import Image, ImageTk
import windnd
import tkinter.ttk
import util as u
import cvimg
import text as tx
import tkinter.colorchooser as cc  # 给导入的包指定一个别名
from text import color as c
import tkinter.messagebox #这个是消息框，对话框的关键

win = tkinter.Tk()
var = tkinter.StringVar()

# url = 'https://imgebed.oss-cn-zhangjiakou.aliyuncs.com/img/saber.jpg'
# url2 = 'https://imgebed.oss-cn-zhangjiakou.aliyuncs.com/img/color.png'

# 把图片绑定在类属性中，防止运行过程中被gc清理
class iconimg():
    ssabericon = None
    coloricon = None
    def __init__(self):
        # tk只支持 gif,所以需要先使用pil转一下 改代码需放在tk初始化之后，否则会报错
        # 设置条形框,插入图片
        image = Image.open('icon/saber.png')
        image = image.resize((32,32))
        self.sabericon =  ImageTk.PhotoImage(image)

        image = Image.open('icon/color.png')
        image = image.resize((48,48))
        self.coloricon =  ImageTk.PhotoImage(image)  # 用PIL模块的PhotoImage打开
iconimg = iconimg()
coloricon = iconimg.coloricon
sabericon = iconimg.sabericon

def Conversion(path):
    # 获取文件和命令下标
    suf = u.suffix(path)
    index = combobox.current()
    print('suf'+str(suf))
    print('index'+str(index))
     # 获取字符和颜色
    msg = tx.letter[cb.current()]
    color = img.color
     # 图片处理
    if suf == 0:
        # 图片转txt
        if index == 0:
            var.set('图片转txt...')
            cvimg.getTxt(path)
            var.set('图片转txt,转换结束，请在根目录查看，宁也可以选择继续转换')
        # 图片转指定字符画 - 彩色
        elif index == 1:
            msg = tx.letter[cb.current()]
            var.set('图片转指定字符-jpg彩色...')
            cvimg.img_txtimg(path, mode=0, msg=msg)
            var.set('图片转指定字符-jpg彩色,完成，请在根目录查看，宁也可以选择继续转换')
        # 图片转字符画-原彩
        elif index == 2:
            var.set('图片转字符-jpg彩色...')
            cvimg.img_txtimg(path,mode=1)
            var.set('图片转字符-jpg彩色,完成，请在根目录查看，宁也可以选择继续转换')
        # 图片转字符画-指定颜色
        elif index == 3:
            var.set('图片转字符-jpg指定颜色...')
            cvimg.img_txtimg(path, mode=2,color=color)
            var.set('图片转字符-jpg指定颜色,完成,请在根目录查看，宁也可以选择继续转换')
        else:
            var.set('错误选项')
    # 视频处理
    if suf == 1:
        # '视频转指定字符-mp4彩色',
        if index == 4:
            msg = tx.letter[cb.current()]
            var.set('视频转指定字符-mp4彩色...'+msg)
            threading.Thread(target=cvimg.vidio_txtimg,args=(path,0,msg,(255,255,255),var)).start()
        # '视频转字符-mp4彩色',
        elif index == 5:
            var.set('视频转字符-mp4彩色...')
            threading.Thread(target=cvimg.vidio_txtimg, args=(path, 1, msg, (255, 255, 255), var)).start()
            # cvimg.vidio_txtimg(path, mode=1)
        # '视频转字符-mp4指定颜色'
        elif index == 6:
            var.set('视频转字符-mp4指定颜色...')
            threading.Thread(target=cvimg.vidio_txtimg, args=(path, 2, msg, color, var)).start()
            # cvimg.vidio_txtimg(path,mode=2,color=color)
        else:
            var.set('错误选项')
for i in tx.mat:
    tx.labermsg += i
# 获取图片路径，并进行格式判别
class img():
    def __init__(self):
        self.imgfile = ''
        self.color = '#000000'
    def _func(self,ls):
        for i in ls:
            #得到的是一个字节
            i = i.decode("utf8","ignore")
            if u.suffix(i) == 2:
                var.set('不支持的格式')
            else:
                self.imgfile = i
                var.set('已选择:'+self.imgfile)
    def showfile(self,event):
        cur = filedialog.askopenfilenames(filetypes=[('图片视频',tx.mat)])
        for i in cur:
            if u.suffix(i) == 2:
                var.set('不支持的格式')
            else:
                self.imgfile = i
                var.set('已选择:' + self.imgfile)
img = img()

# 全局点击事件
class winOnclick():
    def logoclick(self,event):
        tkinter.messagebox.showinfo(title='Hi', message=tx.info)
        #     图片选择器点击事件
    def colorclick(self,event):
        (rgb, hx) = cc.askcolor()
        img.color = hx
    #         复选框点击事件
    def comboboxclick(self,event):
        index = combobox.current()
        if index == 1 or index == 4:
    #         开启字符选择
            var.set('请选择目标字符，默认为 o ')
            cb.place(x=270, y=90)
        else:
            var.set('')

            cb.place_forget()
        if index == 3 or index == 6:
            var.set('请选择要转换的颜色，默认为黑白 ')
            colorlaber.place(x=370, y=80)
        else:
            colorlaber.place_forget()
    # 开始转换点击事件
    def start(self):
        path = img.imgfile
        print('imgfile:' + path)
        if path == '':
            var.set('没有选择任何文件')
            return
        else:
            Conversion(path)
wc = winOnclick()
def initWindows(w,h):
    win.title("图片视频转字符")
    # 获取屏幕宽高
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    # 计算中心点
    x = (ws - w) / 2
    y = (hs - h) / 3
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # win.configure(bg='#95938a')
    # 可调整大小
    win.resizable(0, 0)
initWindows(450,200)

# 文件拖拽上传区域绘制
canvas = tkinter.Canvas(win, width=500, height=300,bg=c.bg)
canvas.create_rectangle(15, 45, 255, 185, outline = c.frame,fill=c.frame)
x=130
y= 70
line = canvas.create_line(x,y-20,x,y+20,fill = c.line,dash=1)
line2 = canvas.create_line(x-20,y,x+20,y,fill = c.line,dash=1)
canvas.place(x=-3, y=-3)
tkinter.Label(win, text=tx.labermsg,bg=c.frame).place(x=50, y=100)

# 信息提示
# tkinter.Label(win,text='提示:',fg='red').place(x=40,y=10)
info = tkinter.Label(win,textvariable=var,fg=c.info,bg=c.bg)
var.set('点击头像查看说明')
info.place(x=55, y=10)

# 图片选择器 laber没有点击事件 通过通用事件绑定 Button-1表示左键单击事件
colorlaber = tkinter.Label(win, image = coloricon)
colorlaber.bind('<Button-1>', wc.colorclick)

# 个人logo
sabericon = tkinter.Label(win, image = sabericon)
sabericon.bind('<Button-1>', wc.logoclick)
sabericon.place(x=10, y=3)
# tkinter.Label(win,text='UID:4669').place(x=340, y=120)

# 复选框
combobox = tkinter.ttk.Combobox(win)
combobox['value'] = tx.mode
combobox.current(0)
combobox['state'] = 'readonly'
combobox.bind("<<ComboboxSelected>>",wc.comboboxclick)
combobox.place(x = 270,y = 45)

# 字符选择器
cb = tkinter.ttk.Combobox(win, width=4)
cb['value'] = tx.letter
cb.current(78)
cb['state'] = 'readonly'

# 按钮
bt1 = tkinter.Button(win, text='开始',bg=c.bt,width=22, command=wc.start)
bt1.place(x=270, y=150)
# 文件上传
windnd.hook_dropfiles(win,func=img._func)
bt2 = tkinter.Label(win, text='点击上传',bg=c.bt, width=8)
bt2.bind('<Button-1>', img.showfile)
bt2.place(x=181, y=48)


win.mainloop()