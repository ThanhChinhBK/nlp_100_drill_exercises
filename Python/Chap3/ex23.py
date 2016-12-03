import re
from ex20 import extract_wikidocs

# 23. Cấu trúc của các Section
# Hiển thị tên của các section và level của các section trong các tài liệu Wikipedia 
# (Ví dụ với section == Section Name ==" thì level bằng 1)
def main():
    wiki_docs = extract_wikidocs()

    pattern = re.compile(r'(={2,}) ([^=]+) (={2,})')
    for doc in wiki_docs:
        tuples = pattern.findall(doc['text'])
        for tp in tuples:
            pfx = tp[0]
            sfx = tp[2]
            sec = tp[1]
            orig = pfx + ' ' + sec + ' ' + sfx
            if len(pfx) != len(sfx):
                print('%s %s %s' %(pfx, sec, sfx))
                exit

            level = len(pfx) - 1    
                
            print('%-40s Level %s\t\t%s' %(sec, level, orig))
            
if __name__ == '__main__':
    main()
