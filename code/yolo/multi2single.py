<<<<<<< HEAD
import os

# 指定要处理的文件夹路径
folder_path = r'C:\Users\38492\ultralytics\potato_new_binary\labels\val'  # 替换为你的文件夹路径

# 遍历文件夹中的所有txt文件
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)

        # 打开文件以读取内容
        with open(file_path, 'r') as file:
            file_contents = file.read()

        # 替换 "potato" 为 "0"
        file_contents = file_contents.replace('potato', '0')

        # 替换 "weed" 为 "1"
        file_contents = file_contents.replace('weed_long', '1')
        # 替换 "weed" 为 "1"
        file_contents = file_contents.replace('weed_other', '1')

        # 打开文件以写入修改后的内容
        with open(file_path, 'w') as file:
            file.write(file_contents)

print("替换完成。")
=======
import os

# 指定要处理的文件夹路径
folder_path = r'C:\Users\38492\ultralytics\potato_new_binary\labels\val'  # 替换为你的文件夹路径

# 遍历文件夹中的所有txt文件
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)

        # 打开文件以读取内容
        with open(file_path, 'r') as file:
            file_contents = file.read()

        # 替换 "potato" 为 "0"
        file_contents = file_contents.replace('potato', '0')

        # 替换 "weed" 为 "1"
        file_contents = file_contents.replace('weed_long', '1')
        # 替换 "weed" 为 "1"
        file_contents = file_contents.replace('weed_other', '1')

        # 打开文件以写入修改后的内容
        with open(file_path, 'w') as file:
            file.write(file_contents)

print("替换完成。")
>>>>>>> 94c54e4f848ace37bf7c1afad41b08a90af25c23
