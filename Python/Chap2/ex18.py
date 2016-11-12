
# 18. Sắp xếp các hàng theo thứ tự giảm dần của giá trị (numeric value) của cột thứ 3
# Viết chương trình thực hiện nhiệm vụ trên.
# Dùng lệnh sort để xác nhận 
# (trong bài tập này, kết quả của chương trình của bạn với lệnh sort có thể khác nhau do có thể có các giá trị giống nhau trong cột thứ 3).

# Confirm with sort command
# % sort -r -n -k 3 ../../data/hightemp.txt

def sort_by_column(file_name, num_col):
    f = open(file_name)
    strdict = {}
    for line in f:
        line = line.rstrip()
        cols = line.split()
        col = float(cols[num_col - 1])
        strdict[col] = line

    for key in sorted(strdict.keys(), reverse = True):
        print(strdict[key])

def main():
    sort_by_column('../../data/hightemp.txt', 3)

if __name__ == '__main__':
    main()
