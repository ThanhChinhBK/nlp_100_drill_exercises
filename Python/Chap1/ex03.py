from nltk.tokenize import word_tokenize
import re

""" 03. Tokenize và thống kê số lượng ký tự của mỗi từ
1) Tokenize câu sau: "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
2) Đưa ra danh sách gồm số ký tự alphabet trong mỗi từ theo thứ tự xuất hiện của từ đó trong câu.
"""
def char_count(str):
    count = 0
    for c in str:
        if re.search(r'[a-zA-Z]',c):
            count += 1
    return count

def num_chars(list_words):
    num_chars = []
    for word in list_words:
        num_chars.append(char_count(word))
    return num_chars

def main():
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    #simple tokenize
    list_words = sentence.split()
    print(num_chars(list_words))

    #nltk tokenize
    list_words = word_tokenize(sentence)
    print(num_chars(list_words))

if __name__ == '__main__':
    main()
