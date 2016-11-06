# 05. n-gram
# 1) Viết hàm sinh ra tất cả các n-gram từ một dãy cho trước (dãy ký tự hoặc danh sách).
# 2) Sử dụng hàm đã viết, sinh ra word bi-gram và character bi-gram từ câu sau: "I am an NLPer"

def get_ngram(arr, n, delim=''):
    ngram = []
    for i in range(len(arr)):
        _min = i
        _max = i + n - 1
        if _max >= len(arr): break
        ngram.append(delim.join(arr[_min:_max + 1]))
    return ngram

def get_char_ngrams(s, n): # character ngrams
    char = []
    char[:0] = s
    char.insert(0, 'BOS') # begin
    char.append('EOS') # end
    
    return get_ngram(char, n)

def get_word_ngrams(s,n): # word ngrams
    words = s.split()
    words.insert(0,'BOS')
    words.append('EOS')
    
    return get_ngram(words, n, delim='/')

def main():
    s = input('input string:')
    if len(s) == 0: s = 'I am NLPer'
    
    word_bigrams = get_word_ngrams(s, 2)
    char_bigrams = get_char_ngrams(s, 2)

    print('character bigrams:\n', char_bigrams)
    print('word bigrams:\n', word_bigrams)

if __name__ == '__main__':
    main()

