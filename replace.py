def replace_backslash(file_path):
    # 打开文本文件并读取内容
    with open(file_path, 'r') as file:
        content = file.read()

    # 使用replace()方法替换`\`为`/`
    updated_content = content.replace('\\', '/')

    # 将更新后的内容写回文本文件
    with open(file_path, 'w') as file:
        file.write(updated_content)

file_path = "/devdata/ycy/datasets/psmoke/val_list.txt"
replace_backslash(file_path)