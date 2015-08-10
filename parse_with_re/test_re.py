# -*- Encoding: utf-8 -*-
import re

ptn = re.compile(r'>([^.]*?)<')
text = '>abcd1.234>567..2efg<'

ret = ptn.findall(text)

print ret