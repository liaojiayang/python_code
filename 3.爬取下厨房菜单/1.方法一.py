import requests,bs4

url = 'http://www.xiachufang.com/explore/'
html = requests.get(url).text
bs_data = bs4.BeautifulSoup(html,'html.parser')
total_data = bs_data.find_all(class_="info pure-u")
for data in total_data:
    # name = data.find(class_="name").text.split()[0]
    name = data.find('a').text.split()[0]
    shicai = data.find(class_="ing ellipsis").text.split()[0]
    href = "http://www.xiachufang.com{}".format(data.find('a')['href'])
    # href = "http://www.xiachufang.com{}".format(data.select('p.name > a')[0]['href'])
    print(name)
    print(shicai)
    print(href)