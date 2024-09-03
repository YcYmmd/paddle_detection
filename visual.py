from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET

def visualize_and_save_bounding_boxes(image_path, xml_path, output_path):
    # 打开图像文件
    image = Image.open(image_path)

    # 创建用于绘制的Draw对象
    draw = ImageDraw.Draw(image)

    # 解析XML文件
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # 遍历所有'object'元素
    for obj in root.findall('object'):
        # 获取边界框坐标
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        # 在图像上绘制边界框
        draw.rectangle([xmin, ymin, xmax, ymax], outline='red')

    # 保存图像
    image.save(output_path)

# 调用函数并提供图像文件路径、对应的VOC格式XML文件路径和输出路径
image_path = '/devdata/ycy/datasets/fire_large/JPEGImages/000133.jpg'
xml_path = '/devdata/ycy/datasets/fire_large/Annotations/000133.xml'
output_path = './output/output_image.jpg'
visualize_and_save_bounding_boxes(image_path, xml_path, output_path)