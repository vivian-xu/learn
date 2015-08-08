# -*- Encoding: utf-8 -*-


def parse(content):
    print '-------------------------------------------------'
    print content


if __name__ == '__main__':
    import json
    data = None
    with open('data.json', 'r') as fp:
        data = json.load(fp)

    num = 10
    for item in data[:num]:
        parse(item)
