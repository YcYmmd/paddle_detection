
import os
import random

def split_voc_xml_annotations(image_directory, annotation_directory, output_directory, train_ratio=0.7, test_ratio=0.2, val_ratio=0.1):
    # 获取图像目录中的所有文件
    image_files = [f for f in os.listdir(image_directory) if f.endswith('.jpg')]

    # 按照指定比例随机打乱文件列表
    random.shuffle(image_files)

    # 计算每个集合中文件的数量
    total_files = len(image_files)
    train_size = int(train_ratio * total_files)
    test_size = int(test_ratio * total_files)
    val_size = total_files - train_size - test_size

    # 分割文件列表
    train_files = image_files[:train_size]
    test_files = image_files[train_size:train_size + test_size]
    val_files = image_files[-val_size:]

    # 写入分割后的文件列表到对应的txt文件中
    write_file_list(train_files, train_ratio, image_directory, annotation_directory, output_directory, 'train_list.txt')
    write_file_list(test_files, test_ratio, image_directory, annotation_directory, output_directory, 'test_list.txt')
    write_file_list(val_files, val_ratio, image_directory, annotation_directory, output_directory, 'val_list.txt')

def write_file_list(file_list, ratio, image_directory, annotation_directory, output_directory, output_file):
    with open(os.path.join(output_directory, output_file), 'w') as f:
        for file in file_list:
            image_path = os.path.join(image_directory, file)
            annotation_path = os.path.join(annotation_directory, file[:-4] + '.xml')
            line = f'{image_path} {annotation_path}\n'
            f.write(line)

# 使用示例
image_directory = '/devdata/ycy/datasets/merge_paddle_data_smoge_fire/JPEGImages/'  # 替换为你的图像目录路径
annotation_directory = '/devdata/ycy/datasets/merge_paddle_data_smoge_fire/Annotations/'  # 替换为你的标注目录路径
output_directory = '/devdata/ycy/datasets/merge_paddle_data_smoge_fire/'  # 替换为你希望生成文件的目录路径
split_voc_xml_annotations(image_directory, annotation_directory, output_directory)

