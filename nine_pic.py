#从PIL库导入Image模块
from PIL import Image

#导入os库
import os

#打开准备好的图片
img = Image.open('1.jpg')

#根据不同的情况对图片进行处理
if img.height == img.width:
    pass
elif img.height > img.width:
    new_img = Image.new('RGBA', (img.height, img.height), (255, 255, 255))
    new_img.paste(img, (int((img.height - img.width) / 2), 0))
    img = new_img
elif img.height < img.width:
    new_img = Image.new('RGBA', (img.width, img.width), (255, 255, 255))
    new_img.paste(img, (0, int((img.width - img.height) / 2)))
    img = new_img
    
#设置截取图片的长和宽
x = int(0.32 * img.height)

#设置截取图片的间隔
y = int(0.02 * img.height)

#若当前文件夹没有pic文件夹，新建pic文件夹
if not os.path.exists('pic'):
    os.mkdir('pic')

#设置文件名
n = 1

#第一层循环设置top和bottom
for row in range(3):
    top = row * (x + y)
    bottom = (row + 1) * x + row * y
    #第二层循环设置left和right
    for col in range(3):
        left = col * (x + y)
        right = (col + 1) * x + col * y
        img.crop((left, top, right, bottom)).save('pic/{}.png'.format(n), 'png')
        n += 1
 
