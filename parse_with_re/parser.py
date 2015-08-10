# -*- Encoding: utf-8 -*-
import re


def parse(content):
    print '-------------------------------------------------'
    print content

    items_ptn = re.compile(ur'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', re.DOTALL)
    items_ret = items_ptn.findall(content)

    value_ptn = re.compile(ur'>([^>]*?)</', re.DOTALL)

    for k, v in items_ret:
        print '0'*30
        ret = value_ptn.findall(v)
        for i in ret:
            print k[:-1], i

'''
    items_ptn = re.compile(ur'<dt>(.*?)：</dt>\s*<dd>(.*?)</dd>')
    items_ret = items_ptn.search(content)


    key_ptn = re.compile(ur'<dt>(.*?)：</dt>')
    key_ret = key_ptn.findall(content)


    value_ptns = [
        re.compile(ur'<a href.*?target="_blank">(.*?)</a>'),
        re.compile(ur'<span class="item">(.*?)</span>')
        ]

    rets = []
    for value_ptn in value_ptns:
        rets.extend(value_ptn.findall(content))


    print(','.join(key_ret))
    print(','.join(rets))
'''
if __name__ == '__main__':
    import json
    data = None
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    num = 10
    for item in data[:num]:
        parse(item)
