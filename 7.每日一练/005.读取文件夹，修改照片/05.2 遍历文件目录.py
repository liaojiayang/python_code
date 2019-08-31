import os # os模块中 listdir函数可以返回指定文件和文件列表

def gci(filepath):
    # os.listdir返回文件名list
    files = os.listdir(filepath)
    # for循环遍历文件名
    for fi in files:
        # os.path.join用作两个path连接
        fi_d = os.path.join(filepath,fi)
        print(fi_d)

print(gci('D:\OneDrive\图片\屏幕快照'))