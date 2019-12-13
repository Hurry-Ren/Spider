
def first(data):
    url = []
    title = []
    keyword = []
    url1 = data.xpath('//div[@class="hotnews"]/ul/li/strong/a/@href').extract()
    title1 = data.xpath('//div[@class="hotnews"]/ul/li/strong/a/text()').extract()
    url.extend(url1)
    title.extend(title1)

    url2 = data.xpath('//ul[@class="ulist focuslistnews"]/li/a/@href').extract()
    title2 = data.xpath('//ul[@class="ulist focuslistnews"]/li/a/text()').extract()
    url.extend(url2)
    title.extend(title2)

    url3 = data.xpath('//ul[@class="hotwords clearfix"]/li/a/@href').extract()
    title3 = data.xpath('//ul[@class="hotwords clearfix"]/li/a/text()').extract()
    url.extend(url3)
    title.extend(title3)

    url4 = data.xpath('//ul[@class="ulist bdlist"]/li/a/@href').extract()
    title4 = data.xpath('//ul[@class="ulist bdlist"]/li/a/text()').extract()
    url.extend(url4)
    title.extend(title4)


    for i in range(len(url)):
        keyword.append('first')

    return keyword,url,title

