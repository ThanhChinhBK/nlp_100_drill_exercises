### 19. Sắp xếp theo tần suất xuất hiện
# Đưa ra tần suất xuất hiện của các giá trị trong cột 1; 
# sắp xếp các giá trị trong cột 1 theo thứ tự từ cao đến thấp của tần suất xuất hiện.
# Chỉ dùng lệnh cut, uniq, sort để thực hiện nhiệm vụ.

def sort_by_freq(file_name):
    f = open(file_name)
    freq_dict = {}
    for line in f:
        line = line.strip()
        key = line.split()[0]
        if key not in freq_dict:
            freq_dict[key] = 0
        else:
            freq_dict[key] += 1

    for key in sorted(freq_dict, key=freq_dict.get, reverse=True):
        print('%s:%d' %(key, freq_dict[key]))

def main():
    sort_by_freq('../../data/hightemp.txt')

if __name__ == '__main__':
    main()
