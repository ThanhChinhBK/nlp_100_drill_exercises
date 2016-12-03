import sys
import re
from ex20 import extract_wikidocs

# 28. Xoá các markup trong văn bản
# Thêm vào xử lý ở bài 27. Xoá các markup trong các templates càng nhiều càng tốt và in ra các thông tin cơ bản về quốc gia.

# Return a dictionary object from given an info box in the format
# {{基礎情報 国
#  |略名 =エジプト
#  |日本語国名 =エジプト・アラブ共和国
#  |公式国名 ='''{{lang|ar|جمهورية مصر العربية}}'''
#  |国旗画像 =Flag of Egypt.svg
# }}
# Change
# -------------------------
# 2015/10/09      remove markups as many as possible

def parse_infobox(template):
    box = {}
    lines = template.split('\n')
    pattern = re.compile(r'\|([^=]+) =([^=<]+)')
    it = re.compile(r"''(.+)''")
    bold = re.compile(r"'''(.+)'''")
    both = re.compile(r"'''''(.+)'''''")
    link = re.compile(r'\[\[(\S+)\]\]')
    kuni = re.compile(r'\{\{(\S+)\}\}')
    for line in lines:
        matches = pattern.findall(line)
        for tp in matches:
            key = tp[0]
            key = key.strip()
            val = tp[1]
            val = val.strip()
            val = both.sub('\g<1>', val)
            val = bold.sub('\g<1>', val)
            val = it.sub('\g<1>', val)
            if link.search(val):
                val = link.sub('\g<1>', val)
                fields = val.split('|')
                val = fields.pop()
            if kuni.search(val):
                val = kuni.sub('\g<1>', val)
                l = val.split('|')
                s = ''
                for k in l:
                    s += k + ','
                val = s[0:-1]
            box[key] = val
            
    return box        

def get_infobox():
    docs = extract_wikidocs()
    objs_list = []
    pattern = re.compile(r'{{基礎情報.+?^}}\n', re.M | re.DOTALL)
    for doc in docs:
        matches = pattern.findall(doc['text'])
        for m in matches:
            dict_obj = parse_infobox(m)
            objs_list.append(dict_obj)
            
    return objs_list        

def main():
    infobox_list = get_infobox()
    for obj in infobox_list:
        for k in sorted(obj.keys()):
            print('%s: %s' % (k, obj[k]))
        print    

if __name__ == '__main__':
    main()
