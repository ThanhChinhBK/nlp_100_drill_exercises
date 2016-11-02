from nltk.tokenize import word_tokenize
import re

""" 04. Ký tự thành phần
1) Tokenize câu sau: "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
2) Lấy ra ký tự đầu tiên của các từ ở vị trí 1, 5, 6, 7, 8, 9, 15, 16, 19; với các từ còn lại lay ra 2 ký tự đầu tiên.
 Tạo ra một map từ các ký tự này tới vị trí của từ trong câu.
"""
def main():
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = word_tokenize(sentence)
    # loai bo dau cau
    for w in words:
        if re.search(r'[a-zA-Z]',w) == None: words.remove(w)
    key = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    map_word = dict()
    for i in range(len(words)):
        if i in key:
            map_word[words[i][0]] = i
        else:
            map_word[words[i][0:2]] = i

    print(repr(words))
    print(repr(map_word))

if __name__ == '__main__':
    main()
