import re
### 08. Xâu mật mã
# Từ các ký tự của một xâu cho trước, cài đặt hàm có tên cipher để mã hoá xâu như sau:
# - Nếu là ký tự tiếng Anh ở dạng thường (lower-case characters) thì chuyển thành ký tự có mã (219 - mã của ký tự hiện tại).
# - Các ký tự khác giữ nguyên.
# Sử dụng hàm đã viết để mã hoá và giải mã các xâu ký tự tiếng Anh.

def cipher(s):
    c = []
    for i in range(len(s)):
        if re.search(r'[a-z]', s[i]):
            new_c = chr(219 - ord(s[i]))
        else:
            new_c = s[i]
        c.append(new_c)

    return ''.join(c)

def decipher(s):
    c = []
    for i in range(len(s)):
        tmp_c = chr(219 - ord(s[i]))
        new_c = s[i]
        if re.search(r'[a-z]', tmp_c):
            new_c = tmp_c
        c.append(new_c)

    return ''.join(c)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '

    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    s = 'aBcDef123'
    z = cipher(s)
    print('Xâu mã hoá của %s là %s' % (s, z))

    orig = decipher(z)
    print('Xâu giải mã của %s là %s' % (z, orig))

if __name__ == '__main__':
    main()
