# import os
# import numpy as np
# import time
# 
# ori_path_lists = ['/devdata/ycy/datasets/MOT17/train/MOT17-02/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-04/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-05/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-09/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-10/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-11/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-13/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-01/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-03/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-06/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-07/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-08/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-12/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-14/img1']
# 
# 
# ori_train_lists = ['/devdata/ycy/datasets/MOT17/train/MOT17-02/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-04/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-05/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-09/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-10/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-11/img1',
#                '/devdata/ycy/datasets/MOT17/train/MOT17-13/img1']
# 
# ori_test_lists = [ '/devdata/ycy/datasets/MOT17/test/MOT17-01/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-03/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-06/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-07/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-08/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-12/img1',
#                '/devdata/ycy/datasets/MOT17/test/MOT17-14/img1']
# 
# voc_img_dir = '/devdata/ycy/datasets/MOT17/voc/JPEGImages'
# voc_imgsets_dir = '/devdata/ycy/datasets/MOT17/voc/ImageSets/Main'
# 
# if not os.path.exists(voc_img_dir):
#     os.makedirs(voc_img_dir)
# if not os.path.exists(voc_imgsets_dir):
#     os.makedirs(voc_imgsets_dir)
# 
# def img_rename_move(ori_path,new_path,fp):
#     filelists = os.listdir(ori_path)                          #获取原路径下的所有图片列表
#     for file in filelists:
#         src = os.path.join(os.path.abspath(ori_path),file)    #读取该文件的信息
#         ori_name = os.path.basename(src)                      #读取该文件的文件名，不包含路径
#         # print(ori_name)
#         new_name = ori_path[-7:-5] + ori_name                 #将原文件名和文件夹名进行部分拼接，得到新的文件名
#         txt_name = new_name[:-4]
#         fp.write(txt_name+'\n')                               #将文件名去除后缀的部分以追加的形式写入txt文件
#         # print(new_name)
#         dst = os.path.join(os.path.abspath(new_path),new_name)
#         os.rename(src,dst)
# 
# txt_train= voc_imgsets_dir + '/train.txt'
# fp_train = open(txt_train,'a+')
# txt_test = voc_imgsets_dir +'/test.txt'
# fp_test = open(txt_test,'a+')
# 
# # img_rename_move(test_dir,test_outdir)
# start_time = time.time()
# 
# for ori_path in ori_train_lists:
#     print('this is processing {}'.format(str(ori_path)))
#     img_rename_move(ori_path,voc_img_dir,fp_train)
# fp_train.close()
# 
# for ori_path in ori_test_lists:
#     print('this is processing {}'.format(str(ori_path)))
#     img_rename_move(ori_path,voc_img_dir,fp_test)
# fp_test.close()
# 
# end_time = time.time()
# print('succeed , total cost {}'.format(end_time-start_time))

import os
import cv2
import codecs
import time


ori_gt_lists = ['/devdata/ycy/datasets/MOT17/train/MOT17-02/gt/gt.txt',
               '/devdata/ycy/datasets/MOT17/train/MOT17-04/gt/gt.txt',
               '/devdata/ycy/datasets/MOT17/train/MOT17-05/gt/gt.txt',
               '/devdata/ycy/datasets/MOT17/train/MOT17-09/gt/gt.txt',
               '/devdata/ycy/datasets/MOT17/train/MOT17-10/gt/gt.txt',
               '/devdata/ycy/datasets/MOT17/train/MOT17-11/gt/gt.txt',
               '/devdata/ycy/datasets/MOT17/train/MOT17-13/gt/gt.txt']

img_dir = '/devdata/ycy/datasets/MOT17/voc/JPEGImages/'
annotation_dir = '/devdata/ycy/datasets/MOT17/voc/Annotations/'

for each_dir in ori_gt_lists:

    start_time = time.time()

    fp = open(each_dir, 'r')
    userlines = fp.readlines()
    fp.close()

    # 寻找gt中的对应的最大frame
    # max_indx = 0
    # for line in userlines:
    #     e_fram = int(line.split(',')[0])
    #     if e_fram > max_index:
    #         max_index = e_fram
    # print(max_index)
    # 寻找gt中的对应的最大frame并存储fram索引列表
    fram_list = []
    for line in userlines:
        e_fram = int(line.split(',')[0])
        fram_list.append(e_fram)
    max_index = max(fram_list)
    print(each_dir + 'max_index：', max_index)

    for i in range(1, max_index):
        clear_name = each_dir[-12:-10] + format(str(i), '0>6s')
        format_name = clear_name + '.jpg'
        detail_dir = img_dir + format_name
        img = cv2.imread(detail_dir)
        shape_img = img.shape
        height = shape_img[0]
        width = shape_img[1]
        depth = shape_img[2]
        #如果采用index的方法去获取索引只会找到想匹配的第一个数据的索引，后面的索引信息无法获取，所以这里
        #采用enumerate方式来获取所有匹配的索引
        each_index = [num for num,x in enumerate(fram_list) if x == (i)]

        with codecs.open(annotation_dir + clear_name + '.xml', 'w') as xml:
            xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            xml.write('<annotation>\n')
            xml.write('\t<folder>' + 'voc' + '</folder>\n')
            xml.write('\t<filename>' + format_name + '</filename>\n')
            # xml.write('\t<path>' + path + "/" + info1 + '</path>\n')
            xml.write('\t<source>\n')
            xml.write('\t\t<database> The MOT17-Det </database>\n')
            xml.write('\t</source>\n')
            xml.write('\t<size>\n')
            xml.write('\t\t<width>' + str(width) + '</width>\n')
            xml.write('\t\t<height>' + str(height) + '</height>\n')
            xml.write('\t\t<depth>' + str(depth) + '</depth>\n')
            xml.write('\t</size>\n')
            xml.write('\t\t<segmented>0</segmented>\n')
            for j in range(len(each_index)):
                num = each_index[j]

                x1 = int(userlines[num].split(',')[2])
                y1 = int(userlines[num].split(',')[3])
                x2 = int(userlines[num].split(',')[4])
                y2 = int(userlines[num].split(',')[5])

                xml.write('\t<object>\n')
                xml.write('\t\t<name>person</name>\n')
                xml.write('\t\t<pose>Unspecified</pose>\n')
                xml.write('\t\t<truncated>0</truncated>\n')
                xml.write('\t\t<difficult>0</difficult>\n')
                xml.write('\t\t<bndbox>\n')
                xml.write('\t\t\t<xmin>' + str(x1) + '</xmin>\n')
                xml.write('\t\t\t<ymin>' + str(y1) + '</ymin>\n')
                xml.write('\t\t\t<xmax>' + str(x1 + x2) + '</xmax>\n')
                xml.write('\t\t\t<ymax>' + str(y1 + y2) + '</ymax>\n')
                xml.write('\t\t</bndbox>\n')
                xml.write('\t</object>\n')

            xml.write('</annotation>')

    end_time = time.time()
    print('process {} cost time:{}s'.format(each_dir,(end_time-start_time)))

print('succeed in processing all gt files')