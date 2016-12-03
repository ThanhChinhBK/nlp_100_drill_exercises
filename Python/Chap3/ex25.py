import sys
import re
from ex20 import extract_wikidocs

# 25. Trích xuất templates
# Trích xuất vị trí và tên các folder có template "基礎情報" trong tài liệu.
# Lưu kết quả trong các đối tượng dictionary. Tham khảo về templates tại [đây](https://en.wikipedia.org/wiki/Help:Infobox).

# Return a dictionary object from given an info box in the format
# {{基礎情報 国
#  |略名 =エジプト
#  |日本語国名 =エジプト・アラブ共和国
#  |公式国名 ='''{{lang|ar|جمهورية مصر العربية}}'''
#  |国旗画像 =Flag of Egypt.svg
# }}

def parse_infobox(template):
    box = {}
    lines = template.split('\n')
    pattern = re.compile(r'\|([^=]+) = ([^=]+)')
    for line in lines:
        matches = pattern.findall(line)
        for tp in matches:
            key = tp[0]
            key = key.strip()
            val = tp[1]
            val = val.strip()
            box[key] = val
            
    return box  

def parse_folder():
    docs = extract_wikidocs()
    patern = re.compile('{{基礎情報.+?^}}', re.M|re.DOTALL) # M = mutiline
    dict_list = []
    for doc in docs:
        matchs = patern.findall(doc['text'])
        for match in matchs:
            dict_list.append(parse_infobox(match))

    return dict_list

def main():
    infobox_list = parse_folder()
    for obj in infobox_list:
        for k in sorted(obj.keys()):
            print('%s: %s' % (k, obj[k]))
        print    

if __name__ == '__main__':
    main()

