# 12. Lưu dòng 1 vào file col1.txt, dòng 2 vào file col2.txt
# Trích xuất nội dung trong cột 1, cột 2 và lưu vào các file tương ứng: col1.txt và col2.txt.
# Thử thực hiện công việc chỉ dùng lệnh cut trong unix.

# Confirm by command cut
# % cut -f 1 ../../data/hightemp.txt > col1.txt
# % cut -f 2 ../../data/hightemp.txt > col2.txt

# Extract column n from given text file src and write to file dest
def write_to_file(file_in, file_out, n):
    fi = open(file_in)
    fo = open(file_out, 'w')
    for line in fi:
        line.strip()
        cols = line.split()
        fo.write(cols[n-1] + '\n')
    
    fi.close()
    fo.close()

def main():
    fi = '../../data/hightemp.txt'
    fo1 = 'col1.txt'
    fo2 = 'col2.txt'
    write_to_file(fi, fo1, 1)
    write_to_file(fi, fo2, 2)

if __name__ == '__main__':
    main()
