# -*- coding: utf-8 -*-

from PIL import Image
import os
import shutil

MIRROR_FLAGE = True  # 镜像标志位
TRANSPOSE_FLAGE = True  # 旋转图像标志位
work_path = 'image_conver'  # 存放要工作文件夹名
work_dir_name = 'origin_label'  # 存放图像文件的文件夹名
convert_image_dir_name = 'convert_image'  # 存放转化后图片的文件夹名
cwd = os.getcwd()  # 取得当前路径
work_dir_path = cwd + os.sep + work_path + os.sep + work_dir_name  # 得到存放图像文件的文件夹路径
convert_image_dir_path = cwd + os.sep + work_path + os.sep + convert_image_dir_name  # 得到存放转化后的图像文件的文件夹路径

image_number = 0  # 已经转换图片的数量
if os.path.exists(convert_image_dir_path):  # 如果convert_image文件夹存在
    shutil.rmtree(convert_image_dir_path)  # 则递归地删除convert_image文件夹
os.mkdir(convert_image_dir_path)  # 生成convert_image文件夹

image_file_name = os.listdir(work_dir_path)  # 得到每个图像文件的文件名list
image_file_name_path = []  # 保存要转化图像的绝对路径的list
for x in image_file_name:
    image_file_name_path.append(work_dir_path + os.sep + x)  # 得到每个图像文件的绝对路径list

for x in image_file_name_path:
    img = Image.open(x)  # 打开图像，得到Image对象
    
    if MIRROR_FLAGE:  # 对图像进行镜像
        img_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)  # 对图像做镜像，得到图像
        img_mirror.save(convert_image_dir_path + os.sep + 'mirror_' + os.path.basename(x))  # 保存图像
    
    if TRANSPOSE_FLAGE:  # 对图像进行旋转
        img_rotate_30 = img.rotate(45)  # 对图像旋转45度
        img_rotate_negative_30 = img.rotate(-45)  # 对图像旋转负45度
        img_rotate_30.save(convert_image_dir_path + os.sep + 'rotate_45' + os.path.basename(x))  # 保存图像
        img_rotate_negative_30.save(
            convert_image_dir_path + os.sep + 'rotate_negative_45' + os.path.basename(x))  # 保存图像

    image_number += 1
    # 显示处理到第几张,尺寸，图像模式
    print("convert pictures :%s size:%s mode:%s" % (image_number, img.size, img.mode))

#
# from PIL import Image
# import os
# cwd=os.getcwd()
# file_path=cwd+os.sep+'superman.jpg'
# print(os.path.basename(file_path))
# img1=Image.open("superman.jpg")
# img2=img1.transpose(Image.FLIP_LEFT_RIGHT)
##img2=img2.transpose(Image.ROTATE_90)
# img2=img2.rotate(30)
# img2.show()
# img2.save('hh.jpg')
