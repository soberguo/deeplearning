#测试之前请务必统一图片大小，并按照指定要求命名
# 自动选择裁剪大小，并裁剪
#   如果图像分辨率大于1216x1216选择
import matplotlib.pyplot as plt

from time import *
from PIL import Image
import numpy as np
from yolo import YOLO
import os
import math
import shutil

bt = time()


your_want = './imgss/'
shutil.rmtree(your_want, ignore_errors=True)
# 定义待批量裁剪图像的路径地址
IMAGE_INPUT_PATH = './img'
# 定义裁剪后的图像存放地址
IMAGE_OUTPUT_PATH = './imgs'
if not os.path.exists("./imgs"):
    os.makedirs("./imgs")
if not os.path.exists("./qwe"):
    os.makedirs("./qwe")

onephoto = './img'
# 从指定目录中选取一张图片
files = os.listdir(onephoto)
n = len(files)
print('Image number:', n)
ind = np.random.randint(0, n)
img_dir = os.path.join(onephoto, files[ind])
image = Image.open(img_dir)
size = image.size
print('Image size:', size)
size = np.mat(size)
length = size[0, 0]
high = size[0, 1]


if length >= 1216 or high >= 1216:
    # 长选择
    length2 = [length / 1 - 608, length / 2 - 608, length / 3 - 608, length / 4 - 608, length / 5 - 608,
               length / 6 - 608, length / 7 - 608, length / 8 - 608, length / 9 - 608, length / 10 - 608]
    length3 = np.maximum(length2, 0)
    length4 = length3.nonzero()
    imm = length3[length4].min()
    length5 = length2.index(imm)
    length6 = int(length5 + 1)
    length7 = list(range(length6))
    #print(length7)
    length8 = length / (length5 + 1)
    # 宽选择
    high2 = [high / 1 - 608, high / 2 - 608, high / 3 - 608, high / 4 - 608, high / 5 - 608,
             high / 6 - 608, high / 7 - 608, high / 8 - 608, high / 9 - 608, high / 10 - 608]
    high3 = np.maximum(high2, 0)
    high4 = high3.nonzero()
    imm2 = high3[high4].min()
    high5 = high2.index(imm2)
    high6 = int(high5 + 1)
    high7 = list(range(high6))
    #print(high7)
    high8 = high / (high5 + 1)
    for i in length7:
        for j in high7:
            BOX_LEFT, BOX_UP, BOX_RIGHT, BOX_DOWN = length8 * float(i), high8 * float(j), length8, high8
            for each_image in os.listdir(IMAGE_INPUT_PATH):
                # 每个图像全路径
                image_input_fullname = IMAGE_INPUT_PATH + '/' + each_image
                # PIL库打开每一张图像
                img = Image.open(image_input_fullname)

                # 从原始图像返回一个矩形区域，区域是一个4元组定义左上右下像素坐标
                box = (BOX_LEFT, BOX_UP, BOX_RIGHT + BOX_LEFT, BOX_DOWN + BOX_UP)

                roi_area = img.crop(box)

                plt.axis('off')

                image_output_fullname = IMAGE_OUTPUT_PATH + "/" + str(math.ceil(i + 1)) + str(
                    math.ceil(j + 1)) + each_image

                roi_area.save(image_output_fullname)


    # huafen
    """
    打开图片文件夹，获取文件夹中图片的名字，如果图片名字中包含某个字符串，把这个图片的完整名字存在一个.txt文本中
    """


    # 存放原始图片地址
    onephoto = './img'  # 读取裁剪前图片文件夹
    files = os.listdir(onephoto)
    n = len(files)  # 文件夹内图片数量
    n = int(n)

    data_base_dir = "./imgs"  # 含所有裁剪后图片的文件夹
    file_list = []  # 建立列表，用于保存图片信息
    # 读取图片文件，并将图片地址、图片名和标签写到txt文件中
    for j in range(n):
        if not os.path.exists("./qwe/a"):
            os.makedirs("./qwe/a")
        write_file_name = './qwe/a/photo%d.txt' % j  # 自己手动创建一个.txt文本
        write_file = open(write_file_name, "w")  # 以只写方式打开write_file_name文件

        for file in os.listdir(data_base_dir):  # file为current_dir当前目录下图片名

            if file.find("x%dx" % j) > 0:  # 需要找带有什么名字的字符串
                write_name = file  # 图片路径 + 图片名 + 标签
                file_list.append(write_name)  # 将write_name添加到file_list列表最后

        number_of_lines = len(file_list)  # 列表中元素个数
        for current_line in range(number_of_lines):
            write_file.write(file_list[current_line] + '\n')
        write_file.close()
        file_list = []

    if not os.path.exists("./qwe/b"):
        os.makedirs("./qwe/b")


    def a():
        path1 = "./qwe/b/"  # 创建的文件的位置
        for j in range(n):  # 创建名为0-n的文件夹
            k = "%d" % j
            file_name = path1 + str(k)
            os.makedirs(file_name)


    a()

    for i in range(n):
        f1 = open('./qwe/a/photo%d.txt' % i, 'r')  # txt文件所在路径
        for line2 in f1.readlines():
            line3 = line2[:-5]  # 读取每行去掉后四位的数
            im = Image.open('./imgs/{}.jpg'.format(line3))  # 打开全部裁剪后图片的路径
            im.save('./qwe/b/%d/{}.jpg'.format(line3) % i)  # 把文件夹中指定的文件名称的图片另存到该路径下

            os.remove('./imgs/{}.jpg'.format(line3))  # 删除裁剪后文件夹下所有裁剪图片

        f1.close()
    # 删除无用文件夹
    your_want_rm_path = './qwe/a/'
    shutil.rmtree(your_want_rm_path, ignore_errors=True)
    print('Finish')



    yolo = YOLO()

    onephoto = './img'  # 读取图片文件夹
    files = os.listdir(onephoto)
    n = len(files)  # 文件夹内图片数量

    img = os.listdir('./qwe/b/')
    wjsize = np.size(img)
    print(wjsize)
    s = np.mat([0, 0, 0])

    with open('./qwe/data.txt', 'w') as f:
        print('xxxxx', file=f)

    for j in range(wjsize):
        path = './qwe/b/'
        k = "%d" % j
        fil = path + str(k) + '/'
        m = j + 1

        print('No.%d rice finish' % m)
        imgg = os.listdir(fil)

        for i in imgg:
            path = fil + i

            image = Image.open(path)
            r_image = yolo.detect_image(image)

            if not os.path.exists("./imgss"):
                os.makedirs("./imgss")

            img_path = './imgss/' + str(i)  # 保存预测图片到文件夹
            r_image.save(img_path)
        with open('./qwe/data.txt', 'a+') as f:
            print('xxxxx', file=f)

    list1 = []
    with open(r"./qwe/data.txt", encoding='utf-8') as f:  # 从TXT文件中读出数据
        for line1 in f:
            list1.append(line1)  # 通过for循环一行一行加载
    list1 = [x.strip() for x in list1]
    # print(list1)
    coun = 0
    char = 'xxxxx'
    s = []
    for each_char in list1:
        coun += 1
        if each_char == char:

            s.append(coun - 1)

    e = len(s) - 1
    srate = 0
    for i in range(e):
        list2 = list1[(s[i] + 1):s[i + 1]]
        b = []
        for j in range(len(list2)):
            a = list(eval(list2[j]))
            b = b + a

        full = 0
        empty = 0
        half = 0
        listlen = int(len(b) / 3)

        for h in range(listlen):
            full = full + b[3 * h]
            empty = empty + b[3 * h + 1]
            half = half + b[3 * h + 2]
        half = math.ceil(half / 2)
        m = i + 1
        print('No.%d rice:Full,Empty and Half' % m, full, empty, 2 * half)
        ph = 0.797 * (full / (full + empty)) + 0.1972
        rate = (ph * half + full) / (full + empty + half)
        srate = srate + rate
        print('No.%d Seed setting rate of rice:' % m, rate)

    mrate = srate / e
    print('Mean seed setting rate of rice:', mrate)


else:
    print('No clipping is required. Please select a higher resolution picture')



# 删除无用文件夹
your_want_rm_path1 = './qwe/'
shutil.rmtree(your_want_rm_path1, ignore_errors=True)
your_want_rm_path2 = './imgs/'
shutil.rmtree(your_want_rm_path2, ignore_errors=True)
your_want_rm_path3 = './img/.ipynb_checkpoints/'
shutil.rmtree(your_want_rm_path3, ignore_errors=True)

print('Finish!')

endt = time()
runt = endt - bt
print('run time:', runt)


