# -*- Encoding: utf-8 -*-
import re

food = {}

def parse(content):
    items_ptn = re.compile(ur'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', re.DOTALL)
    items_ret = items_ptn.findall(content)

    value_ptn = re.compile(ur'>([^<]*?)</', re.DOTALL)

    for k, v in items_ret:
        if k.startswith(u'喜欢的菜'):
            ret = value_ptn.findall(v)
            for i in ret:
                if i not in food:
                    food[i] = 0
                food[i] += 1

if __name__ == '__main__':
    import json
    data = None
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    num = 1000
    for item in data[:num]:
        parse(item)

    sort_food = sorted(food.iteritems(), key=lambda i: i[1])
    for k, v in sort_food:
        print k ,v
