### 07. Sinh ra câu từ template
# Viết hàm số nhận vào 3 biến x, y, z và trả về xâu ký tự "y vào lúc x giờ là z"
# Sinh ra kết quả với các giá trị x, y, z sau đây
# x="12"
# y="Nhiệt độ"
# z=22.4

def generate(x, y, z):
    return '%s vào lúc %s giờ là %s' %(str(y), str(x), str(z))

def main():
    print(generate(12,"Nhiệt độ", 22.4))
if __name__ == '__main__':
    main()
