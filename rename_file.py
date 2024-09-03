import os


def add_prefix_to_files(directory, prefix):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 构造原文件路径
        old_filepath = os.path.join(directory, filename)

        # 确保这是一个文件，而不是一个目录
        if os.path.isfile(old_filepath):
            # 构造新文件名和路径
            new_filename = prefix + filename
            new_filepath = os.path.join(directory, new_filename)

            # 重命名文件
            os.rename(old_filepath, new_filepath)
            print(f'Renamed: {old_filepath} to {new_filepath}')
c

# 使用示例
directory = '/devdata/ycy/datasets/Smoke/Images'  # 替换为你的目录路径
prefix = 'smog_'  # 替换为你想要添加的前缀
add_prefix_to_files(directory, prefix)
