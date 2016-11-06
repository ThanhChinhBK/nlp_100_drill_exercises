from ex05 import get_char_ngrams

# 1) Sinh ra tập X và Y tương ứng là tập các character bi-gram từ hai xâu ký tự "paraparaparadise" và "paragraph".
# 2) Sinh ra các tập hợp union, intersection và difference của X và Y
# 3) Kiểm tra xem bi-gram 'se' có thuộc tập X (Y) hay không?

def main():
    X = get_char_ngrams("paraparaparadise", 2)
    Y = get_char_ngrams("paragraph", 2)

    X = set(X)
    Y = set(Y)

    union = X.union(Y) # X hop Y
    intersection = X.intersection(Y) # X giao Y
    difference = X.difference(Y) # X - Y

    print('union:\n', union)
    print('intersection:\n', intersection)
    print('difference:\n', difference)

    print('se in X:', 'se' in X)
    print('se in Y:', 'se' in Y)

if __name__ == '__main__':
    main()
