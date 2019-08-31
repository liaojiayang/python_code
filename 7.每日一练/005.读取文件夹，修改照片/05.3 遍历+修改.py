import os # os.listdir函数用于遍历文件
import matplotlib.pyplot as plt # matplotlib.pyplot用于显示和保存图片
import matplotlib.image as opimg # matplotlib.image用于读取图片
import scipy.misc # scipy.misc.imresize修改图片尺寸

im_list = os.listdir('D:\OneDrive\图片\屏幕快照')

for im in im_list:
    # 创建文件完整路径，创建新文件路径
    im_path = os.path.join('D:\OneDrive\图片\屏幕快照',im)
    im_path_new = os.path.join('D:\OneDrive\图片\屏幕快照','new'+im)

    # 打开图片
    im_old = opimg.imread(im_path)
    # 修改图片
    im_new = scipy.misc.imresize(im_old,(500,500))
    plt.imshow(im_new)
    # 关闭坐标
    plt.axis('off')
    # 保存图片
    plt.savefig(im_path_new,dpi=300,bbox_inches='tight')


