import urllib.request
import re
def price(book_id):
    price = []
    #拼接价格链接，获取价格信息
    for i in range(0,len(book_id)):
        url = 'https://p.3.cn/prices/mgets?skuIds=J_'+book_id[i]
        targetData = urllib.request.urlopen(url).read().decode('utf-8','ignore')
        # "p":"29.60"
        pat = '"p":"(.*?)"'
        res = re.compile(pat).findall(targetData)
        price.append(res)

    return price
