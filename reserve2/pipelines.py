# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
from scrapy.exceptions import DropItem
import re
regex = r"\d+"


class Reserve2Pipeline(object):
    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    def process_item(self, item, spider):
        key = item['id']
        val = self.redis.get(key)

        if val != None:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.redis.set(key, '1')

     ##   point_str = item.get('point')
     ##   match = re.match(regex,point_str)
     ##   item['point']=match.group(0)

        return item