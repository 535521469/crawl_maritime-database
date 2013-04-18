# encoding:utf8
'''
Created on 2013-4-15
@author: Administrator
'''
from scrapy.item import Item, Field

class MaritimeItem(Item):
    
    Maritime_url = Field()
    Company = Field()
    Activity = Field()
    Address = Field()
    State = Field()
    Zipcode = Field()
    Town = Field()
    Country = Field()
    Phone = Field()
    Fax = Field()
    Contact = Field()
    Website = Field()
    AOH_phone = Field()
    url = Field()
    source = Field()

class ItemConst(object):
    
    AOH_phone = u'AOH_phone'
    url = u'url'
    source = u'source'
    Company = u'Company'
    Activity = u'Activity'
    Address = u'Address'
    State = u'State'
    Zipcode = u'Zipcode'
    Town = u'Town'
    Country = u'Country'
    Phone = u'Phone'
    Fax = u'Fax'
    Contact = u'Contact'
    Website = u'Website'
    
    
    
