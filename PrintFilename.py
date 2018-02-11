import os

path = input("输入一个路径：")
for root, dirs, files in os.walk(path):
    for name in files:
        print(os.path.join(root, name))
        # 将文件夹下所有文件名字后增加一个字符串_py
        # os.rename(os.path.join(root, name), \
        #     os.path.join(root, fname+'_py'+fext))