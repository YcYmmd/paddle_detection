import os


def compare_prefixes(folder1, folder2):
    files1 = get_files_prefixes(folder1)
    files2 = get_files_prefixes(folder2)

    unique_prefixes1 = set(files1) - set(files2)
    unique_prefixes2 = set(files2) - set(files1)

    return (unique_prefixes1, unique_prefixes2)


def get_files_prefixes(folder):
    file_prefixes = set()

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_prefix = os.path.splitext(file)[0].split('.')[0]  # 获取文件名前缀
            file_prefixes.add(file_prefix)

    return file_prefixes


# 指定要比较的两个文件夹路径
folder1 = "/devdata/ycy/datasets/merge_paddle_data_smoke_person_fire/JPEGImages/"
folder2 = "/devdata/ycy/datasets/merge_paddle_data_smoke_person_fire/Annotations//"

# 比较两个文件夹中文件名前缀的差异
diff1, diff2 = compare_prefixes(folder1, folder2)

# 打印前缀差异集合
print("Prefixes unique to folder 1:")
print(diff1)

print("\nPrefixes unique to folder 2:")
print(diff2)