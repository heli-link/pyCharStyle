#     图片转黑白字符图
# def img_txtimg(src,outpath = None):
#     if outpath == None:
#         outpath = u.getTime() + '-imgtxt.jpg'
#     #先转成字符文本，获取字符文本
#     txt,w,h = getTxt(src)
#     # 字符宽高
#     char_w = 12
#     char_h = 35
#     #创建画布
#     im_txt = Image.new("RGB", (w*char_w, h*char_h), (255, 255, 255))
#     dr = ImageDraw.Draw(im_txt)
#     font = ImageFont.truetype("consola.ttf", 30)  # 设置字体
#     #坐标
#     x = y = 0
#     # 遍历文本 进行绘制
#     for str in txt:
#         if str == '\n':
#             # 根据实际情况调整的字符间距
#             y += char_h
#             x = 0
#         dr.text([x,y],str,(0,0,0),font)
#         x += char_w
#     #     保存绘制好的图片
#     im_txt.save(outpath, encoding='utf-8')
#     # cv2.imshow(outpath,cv2.imread(outpath))
#     # cv2.waitKey(0)
