import sys
import string

# 16. Chia file thành N phần
# Chia file thành N phần (đơn vị là các hàng trong file). Chương trình nhận đầu vào từ dòng lệnh là số tự nhiên N.
# Sử dụng lệnh split để thực hiện công việc.
# Sau đó, cải tiến chương trình để chia thành thành N phần bằng nhau (thay vì N lines mỗi file).

# Confirm the result by split
# % split -l 8 ../../data/hightemp.txt
# % python ex16.py 8
# Divide a file into N files
# % python ex16.py --files 3
#  (get the same results as % python ex16.py 8)
# Also try:
# % python ex16.py --files 5
#   (should output 5 file, the first file contains 4 lines,
#    each file of last 4 files contains 5 lines)

def n_lines_each_part(file_name, n):
    f = open(file_name)
    lines = f.readlines()
    part = 0
    length = len(lines)
    for i in range(length):
        if i % n == 0:
            print('part %d :\n' %part)
            part += 1
        print(lines[i].strip())

def n_parts(file_name, n):
    f = open(file_name)
    lines = f.readlines()
    length = len(lines)
    length_part = length // n
    for i in range(n):
        print('part %d:\n' %i)
        for j in range(length_part):
            print(lines[i * length_part + j].strip())
        
    for k in range(i * length_part + j, length):
        print(lines[k].strip())

def main():
    if len(sys.argv) < 2:
        return
    file_name = '../../data/hightemp.txt'
    
    n = int(sys.argv[1])
    n_lines_each_part(file_name, n)
    n_parts(file_name, n)

if __name__ == '__main__':
    main()
