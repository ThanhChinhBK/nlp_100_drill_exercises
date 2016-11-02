# -*- coding: utf-8 -*-

""" 02. Kết hợp hai xâu ký tự
Hãy kết hợp hai xâu ký tự "Partrol" và "Car" để tạo thành xâu mới "PatrolCar".
"""

def concat_string(s1, s2):
    return s1 + s2

def main():
    s1 = 'Partrol'
    s2 = 'Car'
    s = concat_string(s1, s2)
    print(s)

if __name__ == '__main__':
    main()
