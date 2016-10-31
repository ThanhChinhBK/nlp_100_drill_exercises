#-*- encoding:utf-8-*-

'''00. Đảo ngược xâu ký tự
   Hãy đảo ngược xâu ký tự "stressed" (theo thứ tự từ cuối xâu đến đầu xâu ký tự).'''

def string_reverse(s):
    reverse_s = ''
    for i in range(1,len(s) + 1):
        reverse_s += s[-i]
    return reverse_s

def pythonic_reverse_string(s):
    return s[::-1]

def test(s, excepted):
    if s == excepted:
        prefix = 'OK'
    else:
        prefix = 'Failed'

    print('%s got %s excepted %s '%(s, excepted, prefix))

def main():
    s = 'stressed'
    test(string_reverse(s), 'desserts')
    test(pythonic_reverse_string(s), 'desserts')

if __name__ == '__main__':
    main()
