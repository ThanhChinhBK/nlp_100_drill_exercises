# 10. Đếm số dòng trong file
# Đếm số dòng trong file. Xác nhận kết quả bằng lệnh wc trong unix

# use command wc -l for confirmation
# % wc -l ../../data/hightemp.txt

def count_line(file_name):
    n = 0
    data = open(file_name)
    for _ in data:
        n += 1
    return n

def main():
    filename = '../../data/hightemp.txt'
    print("number of lines in %s: %s" %(filename, count_line(filename)))

if __name__ == '__main__':
    main()
