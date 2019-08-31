# 导入random模块，random.choice可随机查询1个字符，sample可随机生成一串字符
import random

list = []
# 大写字母
for i in range(65,91):
    list.append(chr(i))
# 小写字母
for i_2 in range(97,123):
    list.append(chr(i_2))
# 0-9全部数字
for i_3 in range(48,58):
    list.append(chr(i_3))

'''
# 使用random.sample随机生成一串字符，生成字符为list
code = random.sample(list,16)
print(code)
'''

# 使用random.choice随机生成1个字符，并将字符合并
def code_got():
    code_list = ""
    for x in range(0,16):
        code = random.choice(list)
        code_list = code_list + str(code)
    print(code_list)

# 运行200次
for x_2 in range(0,200):
    code_got()


