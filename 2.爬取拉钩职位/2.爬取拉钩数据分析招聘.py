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

#时间戳
now = datetime.datetime.now()
timeStamp = int(now.timestamp()*1000)
geshi = "%Y%m%d%H%M%S"
time1 = datetime.datetime.strftime(now,geshi)

# 获取和解析网页
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
my_data = {'first': 'true','pn': '1','kd': '数据分析'}
my_headers = {
'Cookie': "_ga=GA1.2.641139326.1549615964; user_trace_token=20190208165242-e54df11a-2b7e-11e9-90c5-525400f775ce; LGUID=20190208165242-e54df3f1-2b7e-11e9-90c5-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=29; _gid=GA1.2.1060138655.1550056321; WEBTJ-ID=20190214103355-168e9da78c4176-00e4123dd27a01-6313363-1350728-168e9da78c5aa1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549615965,1550056322,1550056350,1550111636; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168cc6123def8-0d96844dac2204-6313363-1350728-168cc6123df895%22%2C%22%24device_id%22%3A%22168cc6123def8-0d96844dac2204-6313363-1350728-168cc6123df895%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpc_baidu_pc%22%7D%7D; JSESSIONID=ABAAABAAAGFABEFB6BF8A72186B89699A8DD699FD29C9B7; TG-TRACK-CODE=index_search; LGSID=20190214112421-05608a47-3008-11e9-81d3-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fsignature%3D18F3C99DD686BC810E3E66E9233BA44E%26service%3Dhttps%25253A%25252F%25252Fwww.lagou.com%25252Fjobs%25252Flist_%252525E6%25252595%252525B0%252525E6%2525258D%252525AE%252525E5%25252588%25252586%252525E6%2525259E%25252590%25253FlabelWords%25253D%252526fromSearch%25253Dtrue%252526suginput%25253D%26action%3Dlogin%26serviceId%3Dlagou%26ts%3D1550114661784; LG_LOGIN_USER_ID=546a57d147a5626dd5f41d8aadf224647ae60f71d235b529; _putrc=6B6E63D26D24114B; login=true; unick=%E5%BB%96%E4%BD%B3%E6%B4%8B; gate_login_token=6b3514aa5b1772ec1f3fff336ade86d42794828cedb143b0; _gat=1; LGRID={time}-18da9e48-3008-11e9-bc82-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6={timeStamp}; SEARCH_ID=f74a3c60e55f45b4860dd38593e912ab".format(timeStamp=timeStamp,time=time1)
,'Host': 'www.lagou.com'
,'Origin': 'https://www.lagou.com'
,'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
url_data = requests.post(url,data = my_data,headers = my_headers).text
# print(url_data)
json_data = json.loads(url_data)
total_data = json_data['content']['positionResult']['result']

# 获取数据
for data in total_data:
    print(data)
    company = data['companyShortName'] #公司名称
    salary = data['salary'] #薪酬
    district = data['district'] #城区
    businessZones = data['businessZones'] #商圈
    time.sleep(1)


