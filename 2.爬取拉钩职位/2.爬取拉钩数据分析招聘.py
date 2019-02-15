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
    my_data = {'first': 'true','pn': '{}'.format(i),'kd': '数据分析'} #查询职位
    my_headers = {
    'Cookie': "_ga=GA1.2.387210786.1550136578; _gid=GA1.2.1394432396.1550136578; user_trace_token=20190214172939-0d0a35d0-303b-11e9-be9c-525400f775ce; LGUID=20190214172939-0d0a39ee-303b-11e9-be9c-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20190215094941-168eed855e3498-0e8ac79ee51a4c-57b1a3f-2073600-168eed855e55b4; LGSID=20190215094943-f70ccf8e-30c3-11e9-8025-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fword%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26tn%3D25017023_10_pg%26lm%3D-1%26ssl_s%3D1%26ssl_c%3Dssl1_168eed84d9c; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550136578,1550136697,1550195382; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168eed85d133e2-0daeed2e9fe146-57b1a3f-2073600-168eed85d1493f%22%2C%22%24device_id%22%3A%22168eed85d133e2-0daeed2e9fe146-57b1a3f-2073600-168eed85d1493f%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; JSESSIONID=ABAAABAAAIAACBI1CC5D06F795927CD2CD461C0816AB3CE; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=67; TG-TRACK-CODE=index_search; login=false; unick=""; _putrc=""; LG_LOGIN_USER_ID=""; LGRID={time}-187ab853-30c4-11e9-8025-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6={timeStamp}; SEARCH_ID=3e440d6ecf8a47bc8248262837b98719".format(timeStamp=timeStamp,time=time1)
    ,'Host': 'www.lagou.com'
    ,'Origin': 'https://www.lagou.com'
    ,'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='
    ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
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


