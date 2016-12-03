import re
from ex20 import extract_wikidocs

# 22. Trích xuất các tên đề mục (Category name)
# Trích xuất tên đề mục của trong các tài liệu. 
# Trong bài tập này, cần trích xuất chính xác các tên đề mục chứ không phải dòng chứa tên đề mục.

def main():
    docs = extract_wikidocs()
    categories = []
    for doc in docs:
        lines = doc['text'].split('\n')
        for line in lines:
            categories += (re.findall('\[\[Category:(\S+)\]\]', line))
   

    for cat in categories:
        print(cat)

if __name__ == '__main__':
    main()
