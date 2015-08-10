# -*- Encoding: utf-8 -*-
import re

filename = '14718679.html'

text = ''
with open(filename, 'r') as f:
    text = ''.join(f.readlines())

# print text


foods_tptn = re.compile(ur'<p class="recommend-name".*?>(.*?)</p>',re.DOTALL)
foods_tret = foods_tptn.findall(text)

#print (','.join(foods_tret))

item_ptn = re.compile(ur'>([^>]*?)\s*<em class="count">\((.*?)\)</em>',re.DOTALL)
for item in foods_tret:
    item_ret = item_ptn.findall(item)
    for k, v in item_ret:
        print k, v