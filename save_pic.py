# -*- Encoding: utf-8 -*-
from httplib2 import Http

url = 'http://static.jackon.me/images/kunth.jpg'

rsp, content = Http().request(url)

with open('kunth.jpg', 'wb') as f:
    f.write(content)
