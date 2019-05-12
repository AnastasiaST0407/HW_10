import json
import collections
from pprint import pprint
import re
import itertools
import xml.etree.ElementTree as ET


def find(texts):
    splitted = list(map(lambda x: re.split('[^a-zA-Zа-яА-Я0-9_]', x), texts))
    words = list(itertools.chain.from_iterable(splitted))
    words_lower = list(map(lambda x: x.lower(), words))
    words6 = list(filter(lambda x: len(x) > 6, words_lower))
    print([x[0] for x in collections.Counter(words6).most_common(10)])


with open('newsafr.json', encoding='utf-8') as f:
    struct = json.load(f)
texts = [i['description'] for i in struct['rss']['channel']['items']]
find(texts)

tree = ET.parse('newsafr.xml')
texts = [item.text for item in tree.findall('channel/item/description')]
find(texts)
pass