import requests,bs4

url = 'http://www.xiachufang.com/explore/'
html = requests.get(url).text
bs_data = bs4.BeautifulSoup(html,'html.parser')
name_list = bs_data.find_all("p",{"class":"name"})
caipin_list = bs_data.find_all("p",{"class":"ing ellipsis"})
caidan = []
for i in range(len(name_list)):
    name = name_list[i].text.split()[0]
    href = "http://www.xiachufang.com{}".format(name_list[i].find('a')['href'])
    caipin = caipin_list[i].text
    caidan.append([name,caipin,href])
print(caidan)