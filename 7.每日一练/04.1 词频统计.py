'''
逻辑：1.整理字符串，将标点符号替换；2.遍历字符在字符串中的相同值，返回个数；3.导入dict中，使key唯一
'''

# 导入string模块，定义text_new()函数，用作替换字符串中的标点符号
import string
def text_new(x):
    for c in string.punctuation:
        x = x.replace(c,"")
    return x
# 解析文本
T = 'Problem 601: Problem As an an independent developer of the Apple Store App, you want to make a limited time ' \
       'promotion, generate an activation code (or coupon) for your app, and how to generate 200 activation codes (or coupons) using Python?'

# 执行text_new()函数，将T中标点符号替换;使用split(),按照空格分隔文本，并返回list
list_text = text_new(T).split()

L = {}
# 依次返回list的字符串
for n in range(len(list_text)):
    words = list_text[n]

    sum = 0
    for i in list_text:
        if i == words:
            sum = sum + 1
    # 将结果导入dict中，生成唯一值
    L[words] = sum
print(L)
