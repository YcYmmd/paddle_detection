import os

def remove_extra_xml_files(image_directory, annotation_directory):
    # 获取 Annotation 文件夹中的所有 XML 文件名（不包含扩展名）
    xml_files = [os.path.splitext(f)[0] for f in os.listdir(annotation_directory) if f.endswith('.xml')]

    # 获取 JPEGImages 文件夹中的所有图像文件名（不包含扩展名）
    image_files = [os.path.splitext(f)[0] for f in os.listdir(image_directory) if f.endswith('.jpg') or f.endswith(".png") or f.endswith(".JPG")]

    # 计算不在 XML 文件列表中的图像文件名
    extra_xml_files = [f for f in xml_files if f not in image_files]

    # 删除多余的图像文件
    for file in extra_xml_files:
        xml_path = os.path.join(annotation_directory, file + '.xml')
        os.remove(xml_path)
        print(f'Removed: {xml_path}')

def remove_extra_image_files(image_directory, annotation_directory):
    # 获取 Annotation 文件夹中的所有 XML 文件名（不包含扩展名）
    xml_files = [os.path.splitext(f)[0] for f in os.listdir(annotation_directory) if f.endswith('.xml')]

    # 获取 JPEGImages 文件夹中的所有图像文件名（不包含扩展名）
    image_files = [os.path.splitext(f)[0] for f in os.listdir(image_directory) if f.endswith('.jpg') or f.endswith(".png") or f.endswith(".JPG")]

    # 计算不在 XML 文件列表中的图像文件名
    extra_image_files = [f for f in image_files if f not in xml_files]

    # 删除多余的图像文件
    for file in extra_image_files:
        image_path = os.path.join(image_directory, file + '.jpg')
        os.remove(image_path)
        print(f'Removed: {image_path}')

# 使用示例
image_directory = '/devdata/ycy/datasets/merge_person/JPEGImages'  # 替换为你的图像目录路径
annotation_directory = '/devdata/ycy/datasets/merge_person/Annotations'  # 替换为你的标注目录路径
remove_extra_image_files(image_directory, annotation_directory)
