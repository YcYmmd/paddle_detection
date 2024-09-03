# import os
# import xml.etree.ElementTree as ET
#
# def modify_xml_files_in_directory(directory, filename_prefix, new_path):
#     # 获取目录中的所有 XML 文件
#     xml_files = [f for f in os.listdir(directory) if f.endswith('.xml')]
#
#     for xml_file in xml_files:
#         xml_path = os.path.join(directory, xml_file)
#         modify_xml(xml_path, filename_prefix, new_path, xml_file)
#         print(f'Modified: {xml_path}')
#
# def modify_xml(xml_file, filename_prefix, new_path_prefix, xml_file_name):
#     # 解析 XML 文件
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#
#     # 修改 filename 节点
#     filename_node = root.find('filename')
#     if filename_node is not None:
#         original_filename = filename_node.text
#         new_filename = filename_prefix + original_filename
#         filename_node.text = new_filename
#
#     if filename_node is not None:
#         filename_node.text = xml_file_name.replace('.xml', '.jpg')
#
#     # 修改 path 节点
#     # path_node = root.find('path')
#     # if path_node is not None:
#     #     # 获取原始文件的基本名
#     #     # original_basename = os.path.basename(path_node.text)
#     #     # 创建新的路径
#     #     new_full_path = new_path_prefix + filename_node.text
#     #     path_node.text = new_full_path
#
#     # 保存修改后的 XML 文件
#     tree.write(xml_file)
#
# # 使用示例
# directory = '/devdata/ycy/datasets/Smoke/Annotations'  # 替换为你的目录路径
# filename_prefix = 'fire_'  # 替换为你想要添加的前缀
# # new_path = '/devdata/ycy/datasets/fireData/JPEGImages/'  # 替换为你想要的路径
#
# modify_xml_files_in_directory(directory, filename_prefix, new_path)
import os
import xml.etree.ElementTree as ET


def update_name_in_xml(xml_file, new_name):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for name in root.iter('name'):
        name.text = new_name

    tree.write(xml_file)


def update_name_in_folder(folder_path, new_name):
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            xml_file = os.path.join(folder_path, filename)
            update_name_in_xml(xml_file, new_name)


if __name__ == "__main__":
    folder_path = '/devdata/ycy/datasets/Smoke/Annotations'  # 修改为你的文件夹路径
    new_name = 'smog'  # 修改为你想要的新值
    update_name_in_folder(folder_path, new_name)
    print(f"Updated <name> to '{new_name}' in all XML files in {folder_path}")
