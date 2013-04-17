# encoding:utf8
'''
Created on 2013-4-15
@author: Administrator
'''
from items import ItemConst, MaritimeItem
from scrapy import log
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import itertools
import os

class MaritimeSpider(BaseSpider):
    
    name = u'MaritimeSpider'
    
    home_page = u"http://www.maritime-database.com/"
    index_page = u'%s/index.php' % home_page

    def get_next_proxy(self, cookies):
        return cookies[u'proxies'].next()

class ShippingSpider(MaritimeSpider):
    
    name = u'ShippingSpider'
#    DOWNLOAD_DELAY = 1
    
    def start_requests(self):
        cookies = build_cookies(self)
#        yield self.make_requests_from_url()
        
        file_dir = os.getcwd()
        
        sub_dir = os.sep.join(['ship', 'shipping'])
        
        for fn_item in os.walk(sub_dir):
            for fn in fn_item[2]:
                file_path = os.sep.join([file_dir, sub_dir, fn])
                response = Response(file_path, body=''.join(open(file_path, u'r').readlines()))
                response.body_as_unicode = lambda :response.body
                hxs = HtmlXPathSelector(response)
                a_tags = hxs.select('//table[@class="text2"]//a')
                print len(a_tags)
#                for a_tag in a_tags:
#                    print a_tag.select('@href').extract()[0], a_tag.select('text()').extract()[0]
            break
                
#        yield Request('%s?page=%s' % (self.index_page, page_no),
#                      self.parse, cookies=cookies,
#                      meta={u'proxy':cookies[u'proxies'].next()},
#                      )

#    def parse(self, response):
#        
#        hxs = HtmlXPathSelector(response)
#        block_a_tags = hxs.select('//div[@class="index_container"]//div[@class="index_item index_item_ie"]/a')
#        
#        cookies = response.request.cookies
#        
#        try:
#            with open(u'fetched.txt', u'r') as f:
#                fetched_urls = map(str.strip, f.readlines())
#        except Exception:
#            fetched_urls = []
#        
#        for a_tag in block_a_tags:
#            href = a_tag.select('@href')
#            with open(u'detail.txt', u'a') as f:
#                f.write('%s@@@@@%s\n' % (self.home_page + href.extract()[0], response.url))
#            if self.home_page + href.extract()[0] in fetched_urls:
#                continue
#            yield Request(self.home_page + href.extract()[0],
#                          ChannelOneDetailSpider().parse,
#                          dont_filter=True,
#                          meta={u'proxy':cookies[u'proxies'].next()},
#                          cookies=cookies
#                          )
#        page_div_tag = hxs.select('//div[@class="pagination"]')
#        current_page = page_div_tag.select('span[@class="current"]/text()').extract()[0]
#        
#        next_page = '%s?page=%s' % (self.index_page, int(current_page) + 1)
#        
#        self.log(u"add next page %s " % next_page, log.INFO)
#        
#        yield Request(next_page, self.parse,
#                      meta={u'proxy':cookies[u'proxies'].next()},
#                      cookies=cookies)
        

class ChannelOneDetailSpider(MaritimeSpider):
    def parse(self, response):
        with open(u'fetched.txt', u'a') as f:
            f.write(response.url + u'\n')
        hxs = HtmlXPathSelector(response)
        mi = MaritimeItem()
        url = response.url
        mi[ItemConst.url] = url
        title = hxs.select('//div[@class="stage_navigation movie_navigation"]//a/text()').extract()[0]
        main_div_tag = hxs.select('//div[@class="movie_info"]')
        tr_tags = main_div_tag.select('//table/tr')
        
        
#        try:
#            desc = main_div_tag.select('//table/tr[1]//p/text()').extract()[0].strip().replace(u'\n', u'').replace(u'\r', u'')
#            mi[ItemConst.desc] = desc
#        except Exception:
#            self.log(u'desc wrong %s' % url, log.CRITICAL)
#        try:
#            img = main_div_tag.select('//div[@class="movie_thumb"]/img/@src').extract()[0]
#            mi[ItemConst.img] = img
#        except Exception :
#            self.log(u'img wrong %s' % url, log.CRITICAL)
#        try:
#            imdb = main_div_tag.select('//div[@class="mlink_imdb"]/a/@href').extract()[0]
#            mi[ItemConst.imdb] = imdb
#        except Exception :
#            pass
#        for strong_tag in tr_tags.select('//strong'):
#            try:
#                strong_val = strong_tag.select('text()').extract()[0]
#            except Exception:
#                continue
#            if strong_val == u'Released:':
#                td_val = strong_tag.select(u'parent::td/parent::tr/td[2]/text()').extract()[0]
#                mi[ItemConst.released_date] = td_val
#            elif strong_val == u'Runtime:':
#                td_val = strong_tag.select(u'parent::td/parent::tr/td[2]/text()').extract()[0]
#                mi[ItemConst.runtime] = td_val
#            elif strong_val == u'Genres:':
#                td_val = strong_tag.select(u'parent::td/parent::tr/td[2]//a/text()').extract()
#                if len(td_val):
#                    mi[ItemConst.category1] = td_val[0]
#                if len(td_val) > 1:
#                    mi[ItemConst.category2] = td_val[1]
#                mi[ItemConst.genres] = u','.join(td_val)
#            elif strong_val == u'Countries:':
#                td_val = strong_tag.select(u'parent::td/parent::tr/td[2]//a/text()').extract()
#                mi[ItemConst.conuntries] = u','.join(td_val)
#            elif strong_val == u'Director:':
#                td_val = strong_tag.select(u'parent::td/parent::tr/td[2]//a/text()').extract()
#                mi[ItemConst.director] = u','.join(td_val)
#            elif strong_val == u'Actors:':
#                td_val = strong_tag.select(u'parent::td/parent::tr/td[2]//a/text()').extract()
#                mi[ItemConst.actors] = u','.join(td_val)
        
        self.log(u"add %s" % url, log.INFO)
        yield mi
        
def build_cookies(self):
    ipproxies = self.settings[u'proxies']
    ipproxy_generator = itertools.cycle(ipproxies)
    cookies = {
               u'proxies':ipproxy_generator
               }
    return cookies
