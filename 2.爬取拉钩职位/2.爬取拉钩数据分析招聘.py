'''
爬取拉钩数据分析岗位信息
    网页加载：XHR
    使用post 获取网页
    json.loads 解析数据
    select 查询数据
'''
import requests,json
from lxml import etree
import time
import datetime
from urllib.request import quote

#时间戳
now = datetime.datetime.now()
timeStamp = int(now.timestamp()*1000)
geshi = "%Y%m%d%H%M%S"
time1 = datetime.datetime.strftime(now,geshi)

# 获取和解析网页
w = open(r'H:\OneDrive\工作\编程设计\spyder\2.爬取拉钩职位\Data.csv', 'w', encoding='gbk')
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&district={}&needAddtionalResult=false'\
    .format(quote('北京'),quote('朝阳区'))  #输入城市编码成网络
for i in range(1,31):
    my_data = {'first': 'true','pn': '{}'.format(i),'kd': '会计'} #查询职位
    my_headers = {
        'Cookie': "_ga=GA1.2.387210786.1550136578; user_trace_token=20190214172939-0d0a35d0-303b-11e9-be9c-525400f775ce; LGUID=20190214172939-0d0a39ee-303b-11e9-be9c-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168eed85d133e2-0daeed2e9fe146-57b1a3f-2073600-168eed85d1493f%22%2C%22%24device_id%22%3A%22168eed85d133e2-0daeed2e9fe146-57b1a3f-2073600-168eed85d1493f%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LG_LOGIN_USER_ID=598fd89fc829c6be647de940ba7de28c651225704a559ca6; _gid=GA1.2.824003799.1554790432; LGSID=20190409141352-a5bd8a65-5a8e-11e9-8ce9-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E6%258B%2589%25E9%2592%25A9; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fgongsi%2F147.html; JSESSIONID=ABAAABAAAGGABCB517CC623DFFE546B7F4546983A35AA26; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1553495651,1554790432,1554790443,1554791741; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=d7d2f9b424694fc44571974551d7079d2a9084da55; LGRID={time}-b9a19b46-5a91-11e9-a05c-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6={timeStamp}; SEARCH_ID=013254d7ebbc490e84e1405a789fa67d".format(timeStamp=timeStamp, time=time1)
        ,'Host': 'www.lagou.com'
        ,'Origin': 'https://www.lagou.com'
        ,'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='
        ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36'
    }
    url_data = requests.post(url,data = my_data,headers = my_headers).text
    # print(url_data)
    json_data = json.loads(url_data)
    # print(json_data)
    total_data = json_data['content']['positionResult']['result']
    time.sleep(1)

    # 获取数据
    for data in total_data:
        # print(data)
        # print(type(data))
        # print(len(data))
        # 地域
        district = data['district']  # 城区
        stationname = data['stationname']  # 商圈
        linestaion = data['linestaion'] #地铁
        # 公司
        company = data['companyShortName'] #公司名称
        industryField = data['industryField'].replace(',',';')   #领域
        financeStage = data['financeStage'] #融资
        companySize = data['companySize']  # 规模
        # 职位
        createTime = data['createTime'] #发布时间
        positionName = data['positionName'] #职位名称
        thirdType = data['thirdType'] #职位细分
        secondType = data['secondType'] #分析领域
        positionLables = ';'.join(data['positionLables']) #技能要求
        workYear = data['workYear'] #经验要求
        education = data['education']   #学历要求
        # 待遇
        salary = data['salary']  # 薪酬
        companyLabelList = ';'.join(data['companyLabelList']) #福利 用分号分割字符串
        positionAdvantage = data['positionAdvantage'].replace(',',';').replace('，',';').replace('、',';').replace('/',';')   #优势 替换逗号

        print("{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}--->{}\n"
              .format(district,stationname,linestaion,company,industryField,financeStage,companySize,createTime,positionName,thirdType,secondType
                      ,positionLables,workYear,education,salary,companyLabelList,positionAdvantage))
        w.write("{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{} ,{}\n"
              .format(district,stationname,linestaion,company,industryField,financeStage,companySize,createTime,positionName,thirdType,secondType
                      ,positionLables,workYear,education,salary,companyLabelList,positionAdvantage))
        w.flush()
w.close()


