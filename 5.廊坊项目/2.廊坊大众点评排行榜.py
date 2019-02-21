import requests,bs4,time,json

w = open('H:/OneDrive/工作/编程设计/spyder/5.廊坊项目/dianpin.csv','w',encoding='utf-8')
url_1 = 'http://www.dianping.com/shoplist/shopRank/pcChannelRankingV2?rankId=7acb1683f1cc89810888f620c792da28' #廊坊为城市名称
headers = {'Cookie': 'td_cookie=2464111219; _lxsdk_cuid=1690e07db3dc8-00119572b83533-57b1a3f-1fa400-1690e07db3ec8; _lxsdk=1690e07db3dc8-00119572b83533-57b1a3f-1fa400-1690e07db3ec8; _hc.v=93b7e7fa-41e7-eaf4-350f-db49d1812089.1550718590; cy=33; cye=langfang; _lxsdk_s=1690e07db3e-487-31e-98f%7C%7C324'
,'Host': 'www.dianping.com'
,'Referer': 'http://www.dianping.com/langfang'
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36'
,'X-Requested-With': 'XMLHttpRequest'
           }

#直接从排行榜单中获取各个榜单链接

html_1 = requests.get(url_1,headers = headers).text
bs_data_1 = bs4.BeautifulSoup(html_1,'html.parser')
url_2_data = bs_data_1.find(id="rankNavContainer").find_all('a')
for url_2_t in url_2_data[1:]:
    url_2 = "http://www.dianping.com{}".format(url_2_t['href'].replace('/shoplist/shopRank/pcChannelRankingV2?','/mylist/ajax/shoprank?'))
    print(url_2_t.text)
    #print(url_2)
    html_2 = requests.get(url_2,headers = headers).content
    #print(html_2)
    js_data = json.loads(html_2)['shopBeans']

    try:
        num = 0
        for data in js_data:
            num += 1
            name = data['shopName']
            CategoryName = data['mainCategoryName']
            mainRegionName = data['mainRegionName']
            avgPrice = data['avgPrice']

            print("{}--->{}--->{}--->{}--->{}\n".format(num,name,CategoryName,mainRegionName,avgPrice))
            w.write("{} ,{} ,{} ,{} ,{}\n".format(num,name,CategoryName,mainRegionName,avgPrice))
            w.flush()
    except TypeError:
        pass




