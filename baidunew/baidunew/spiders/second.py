import urllib.request
from lxml import etree

def second():
    url = []
    title = []
    keyword = []
    word = ['civilnews', 'InternationalNews', 'EnterNews', 'SportNews',
               'FinanceNews', 'TechNews', 'MilitaryNews', 'InternetNews',
               'DiscoveryNews', 'LadyNews', 'HealthNews', 'PicWall']

    for i in range(0, len(word)):
        targetUrl = 'http://news.baidu.com/widget?id=' + word[i]
        data = urllib.request.urlopen(targetUrl).read().decode('utf-8','ignore')
        targetData = etree.HTML(data)
        #获取url
        answerUrl = targetData.xpath('//ul[@class="ulist focuslistnews"]/li/a/@href')#已经是xml数据，无需extract()
        for k in range(0,len(answerUrl)):
            keyword.append(word[k])
            url.append(answerUrl[k])    #二维变一维
        #获取标题
        answerTitle = targetData.xpath('//ul[@class="ulist focuslistnews"]/li/a/text()')
        for j in range(0, len(answerTitle)):
            title.append(answerTitle[j])  #二维变一维

    return keyword,url,title


