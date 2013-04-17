# encoding:utf8
'''
Created on 2013-4-15
@author: Administrator
'''
from items import ItemConst
from scrapy.contrib.exporter import CsvItemExporter

class CSVPipeline(object):

    def process_item(self, item, spider):
        self.csv_exporter.export_item(item)

    def open_spider(self, spider):
        filed_list = [ItemConst.url,
                        ItemConst.Company,
                        ItemConst.Activity,
                        ItemConst.Address,
                        ItemConst.State,
                        ItemConst.Zipcode,
                        ItemConst.Town,
                        ItemConst.Country,
                        ItemConst.Phone,
                        ItemConst.Fax,
                        ItemConst.Contact,
                        ItemConst.Website,
                        ItemConst.AOH_phone,
                        ]
        
        with open(u'output.csv', u'w') :
            pass
        
        self.csv_exporter = CsvItemExporter(file(u'output.csv', u'a'),
                                            fields_to_export=filed_list,
                                            lineterminator=u'\n')

    def close_spider(self, spider):
        pass
        
        
