import os
import cv2

def check_images_with_opencv(image_directory, min_size_kb=10):
    # 获取图像目录中的所有文件
    image_files = [f for f in os.listdir(image_directory) if f.endswith('.jpg') or f.endswith('.png')]

    # 存储有问题的图像文件名
    problematic_images = []

    # 遍历图像文件
    for image_file in image_files:
        image_path = os.path.join(image_directory, image_file)
        try:
            # 检查文件大小
            file_size_kb = os.path.getsize(image_path) / 1024
            if file_size_kb < min_size_kb:
                print(f'Small file size found: {image_path} ({file_size_kb} KB)')
                problematic_images.append(image_file)
                continue

            # 尝试使用 OpenCV 打开图像文件
            img = cv2.imread(image_path)
            if img is None:
                print(f'Problematic image found: {image_path} (cannot be read with OpenCV)')
                problematic_images.append(image_file)

        except Exception as e:
            print(f'Problematic image found: {image_path} ({e})')
            problematic_images.append(image_file)

    # 删除有问题的图像文件
    for image_file in problematic_images:
        image_path = os.path.join(image_directory, image_file)
        os.remove(image_path)
        print(f'Removed: {image_path}')

    return len(problematic_images)

# 使用示例
image_directory = '/devdata/ycy/datasets/smoke_large/JPEGImages/'
num_removed = check_images_with_opencv(image_directory)
print(f"Total {num_removed} problematic images removed.")





# from PIL import Image
# import os
#
# def check_images_in_directory(directory):
#     # 遍历目录中的文件
#     for file_name in os.listdir(directory):
#         # 构建文件的完整路径
#         file_path = os.path.join(directory, file_name)
#         try:
#             # 打开图像文件
#             image = Image.open(file_path)
#             # 对图像进行其他处理操作，例如：
#             image.thumbnail((300, 300))  # 缩略图
#             # image.rotate(90)  # 旋转图像
#             # ...
#             # 进行其他操作
#         except Exception as e:
#             print("无法处理图像: ", file_name)
#
# # 调用函数并提供包含图片文件的目录路径
# image_directory = '/devdata/ycy/datasets/smoke_large/smoke/JPEGImages/'
# check_images_in_directory(image_directory)