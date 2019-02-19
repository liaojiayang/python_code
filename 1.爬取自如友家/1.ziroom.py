'''
自如友家租房：http://www.ziroom.com/z/nl/z2.html?qwd=
    requests.get获取网页.text
    from lxml import etree 导入 etree.HTML解析网页
    xpath查询数据
获取数据
    标题
    面积
    层数
    居室
    地铁距离
    标签1
    标签2
    价格
'''

#-*- coding:utf-8 -*-
import requests,bs4
from lxml import etree
import time

url = 'http://www.ziroom.com/z/nl/z2.html?qwd=&p=1'
headers = {'Referer': 'http://www.ziroom.com/'
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
,'X-Requested-With': 'XMLHttpRequest'}
get_data = requests.get(url,headers=headers).text
bs_data = bs4.BeautifulSoup(get_data,'html.parser')
for i_2 in range(2,19):
    name = bs_data.select('#houseList > li:nth-child({}) > div.txt > h3 > a'.format(i_2))[0].text
    biaoqian1 = bs_data.select('#houseList > li:nth-child({}) > div.txt > h4'.format(i_2))[0].text.strip() # strip() 删除空格
    href = "http:{}".format(bs_data.select('#houseList > li:nth-child({}) > div.txt > h3 > a'.format(i_2))[0].attrs['href'])  # attrs['href'] 获取属性为'href'的数据

    print(name)
    print(biaoqian1)
    print(href)
    time.sleep(1)
'''完成房源信息查询
价格需要进入下一级页面获取'''