import requests,bs4,time

url_1 = 'http://www.dianping.com/langfang' #廊坊为城市名称
headers = {'Cookie': 'td_cookie=2464111219; _lxsdk_cuid=1690e07db3dc8-00119572b83533-57b1a3f-1fa400-1690e07db3ec8; _lxsdk=1690e07db3dc8-00119572b83533-57b1a3f-1fa400-1690e07db3ec8; _hc.v=93b7e7fa-41e7-eaf4-350f-db49d1812089.1550718590; cy=33; cye=langfang; _lxsdk_s=1690e07db3e-487-31e-98f%7C%7C324'
,'Host': 'www.dianping.com'
,'Referer': 'http://www.dianping.com/langfang'
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36'
,'X-Requested-With': 'XMLHttpRequest'
           }

#从主页到热门页方法失败，各部分内容逻辑不同
''' 
html_1 = requests.get(url_1,headers = headers).text
bs_data_1 = bs4.BeautifulSoup(html_1,'html.parser')
#data_1 = bs_data_1.find_all("span",{"class":"span-container"})
data_1 = bs_data_1.find_all("a",{"class":"index-title"})    #查找到分类模块
for url_2_data in data_1:
    url_2 = url_2_data.attrs['href']    #获得每一类网页二级链接

    html_2 = requests.get(url_2,headers = headers).text
    bs_data_2 = bs4.BeautifulSoup(html_2,'html.parser')
    data_2 = bs_data_2.find("ul",{"class":"desc Fix"})  #二级页面排行榜模块，多个排行标准
    #url_3 = data_2.select('li:nth-child(1)')[0]
    print(data_2)
    '''

#直接从排行榜单中获取各个榜单链接



