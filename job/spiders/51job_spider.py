import scrapy
from job.items import JobItem
from scrapy.selector import Selector
from scrapy.http import Request
import json

class JobSpider(scrapy.Spider):
    name = 'job'
    # 下载延时
    download_delay = 1
    allowed_domains = ["51job.com"]
    start_urls = ['http://search.51job.com/jobsearch/search_result.php?'
                  'fromJs=1&jobarea=180200%2C010000&keyword=python&'
                  'keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&'
                  'confirmdate=9']

    def parse(self, response):
        selector = Selector(response)
        positions = selector.xpath('//div[@class="dw_table"]/div[@class="el"]')
        for position in positions:
            item = JobItem()
            item['gsname'] = position.xpath('span/a/text()').extract()
            name = position.xpath('p/span/a/text()').extract()
            item['gwname'] = str(name[0]).strip()
            item['gzdd'] = position.xpath('span[@class="t3"]/text()').extract()
            xinzi = position.xpath('span[@class="t4"]/text()').extract()
            if xinzi == []:
                item['xinzi'] = '面议'
            else:
                item['xinzi'] = (xinzi[0].split()[-1])
            item['fbrq'] = position.xpath('span[@class="t5"]/text()').extract()
            item['url'] = position.xpath('p/span/a/@href').extract()
            salary_url = position.xpath('p/span/a/@href').extract()[0]
            salary_url = str(salary_url)
            request = Request(salary_url,callback=self.get_salary_parse)
            request.meta['item'] = item
            yield request
        # 判断是否有下一页
        # next_link = selector.xpath('//li[@class="bk"]/a/@href').extract()
        # if len(next_link) > 1:
        #     next_link = str(next_link[-1])
        #     yield Request(next_link,callback=self.parse)
        # else:
        #     next_link = str(next_link[0])
        #     yield Request(next_link,callback=self.parse)


    def get_salary_parse(self,response):
        selector = Selector(response)
        item = response.meta['item']
        details = selector.xpath('//div[@class="t1"]/span/text()').extract()
        for dt in details:
            if dt.find('大专') != -1:
                item['xueli'] = dt
            elif dt.find('本科') != -1:
                item['xueli'] = dt
            elif dt.find('招聘') != -1:
                item['renshu'] = dt
            elif dt.find('经验') != -1:
                item['jingyan'] = dt
        sbdz = selector.xpath('//div[@class="bmsg inbox"]/p/text()').extract()
        if len(sbdz) ==0:
            item['sbdz'] = "没有"
        else:
            item['sbdz'] = str(sbdz[1]).strip()
        return item