x = [1,2,34,5]
for i in x:
    print(i)

c = ['股票期权', '扁平管理', '十五薪', '定期体检']
a = ';'.join(c)
print(a)

from urllib.request import quote
url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(quote('成都站'))

# %E5%8C%97%E4%BA%AC
# %E6%9C%9D%E9%98%B3%E5%8C%BA

print(quote('朝阳区'))