import sys

# 15. Trích xuất ra N hàng cuối cùng của file
# Viết chương trình trích xuất ra N hàng cuối cùng của file. 
# Chương trình nhận đầu vào từ dòng lệnh là số tự nhiên N.
# Sử dụng lệnh tail trong unix để thực hiện công việc.

# Confirm the result
# % python ex15.py 2
# % tail -n 2 ../../data/hightemp.txt

# Read n lines from the end of a file
# This solution cannot work if the size of a file does not fit the memory

def tail_n(file_name, n):
    f = open(file_name)
    lines =  f.readlines()
    size = len(lines)
    for i in range(n):
        print(lines[size - 1 - n].strip())

def main():
    if len(sys.argv) < 3:
        return
    file_name = sys.argv[1]
    n = int(sys.argv[2])
    tail_n(file_name, n)

if __name__ == '__main__':
    main()
