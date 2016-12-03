
import re
from ex20 import extract_wikidocs

# 24. Trích xuất các liên kết file
# Trích xuất toàn bộ các liên kết đến các media files trong tài liệu.
# xuat hien dang sau File hoac ファイル

def main():
    docs = extract_wikidocs()
    pattern = re.compile(r'(File|ファイル):([^\|]+)')
    for doc in docs:
        # Find all markups File: or ファイル:
        references = pattern.findall(doc['text'])
        for ref in references:
            print(ref[1])
            
if __name__ == '__main__':
    main()  
