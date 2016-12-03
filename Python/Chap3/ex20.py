import gzip
import sys
import json
import codecs
import re

# 20. Đọc vào dữ liệu JSON
# Đọc dữ liệu từ file JSON chứa các tài liệu Wikipedia, trích xuất & hiển thị nội dung của tài liệu có liên quan đến "イギリス" 
# (có nghĩa là nước Anh). Sử dụng các nội dung của tài liệu được trích xuất này để thực thi các nhiệm vụ trong các bài tập từ 21-29.
def extract_wikidocs():
    filename = '../../data/jawiki-country.json'
    f = open(filename)
    docs = []
    for line in f:
        doc = json.loads(line.strip(), 'utf-8')
        if re.search(r'イギリス', doc['text']):
            docs.append(doc)
    return docs

def main():
    wiki_docs = extract_wikidocs()
    print('# Wikipedia articles related to イギリス: %s' % len(wiki_docs))
    for doc in wiki_docs:
        print(doc['title'])
        print(doc['text'])

if __name__ == '__main__':
    main()
