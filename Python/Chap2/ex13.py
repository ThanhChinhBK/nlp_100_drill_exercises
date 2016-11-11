# 13. Trộn hai file col1.txt và col2.txt
# Kết hợp nội dung trong 2 file col1.txt và col2.txt để tạo thành một file mới có nội dung giống với cột 1 và cột 2 trong file ban đầu 
# (các cột cách nhau bởi ký tự tab).
# Sử dụng lệnh paste để thực hiện bài tập và xác nhận kết quả của chương trình bạn viết.

# Confirm using paste command
# % paste col1.txt col2.txt

# Paste multiple files into one file
# For variable number of arguments, use tuples with *args
# TODO: paste files with different number of lines
# Output to stdout
def main():
    f1 = open('col1.txt')
    f2 = open('col2.txt')
    col1s = []
    col2s = []
    for line in f1:
        col1s.append(line.strip())
    for line in f2:
        col2s.append(line.strip())
        
    for i in range(len(col1s)):
        print('%s\t%s\n' %(col1s[i], col2s[i]))

if __name__ == '__main__':
    main()
