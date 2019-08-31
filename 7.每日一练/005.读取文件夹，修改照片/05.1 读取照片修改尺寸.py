import os #遍历文件夹
import matplotlib.pyplot as plt #plt用于显示图片
import matplotlib.image as mpimg #mpimg用于读取照片
import numpy as np

# 读取照片
lena = mpimg.imread('D:\OneDrive\图片\屏幕快照/2019-03-29.png')

# 导入scipy模块修改图片
import scipy.misc
lena_new_sz = scipy.misc.imresize(lena,0.5)
#`imresize` is deprecated in SciPy 1.0.0, and will be removed in 1.3.0.Use Pillow instead: ``numpy.array(Image.fromarray(arr).resize())``.

plt.imshow(lena_new_sz) # 显示图片
plt.axis('off') # 不显示坐标轴
# 在窗口打开图片
# plt.show()
# 保存图片，打开和保存不能同时进行
plt.savefig('D:\OneDrive\图片\屏幕快照/lena_new_sz.png')

