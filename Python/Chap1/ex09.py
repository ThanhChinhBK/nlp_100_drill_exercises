import random

### 09. [Typoglycemia](https://en.wikipedia.org/wiki/Typoglycemia)
# Cho đầu vào là một câu tiếng Anh bao gồm các word ngăn cách nhau bằng ký tự space. Viết chương trình thực hiện việc sau:
# - Với mỗi word, giữ nguyên ký tự đầu và ký tự cuối, 
# đảo thứ tự một cách ngẫu nhiên các ký tự còn lại của (tất nhiên các word có ít hơn 4 ký tự thì không cần làm gì)
# - Cho trước một câu tiếng Anh hợp lệ, 
# ví dụ "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .", 
# chạy chương trình đã viết để đưa ra kết quả.

def typoglycemia_word(word):
    if len(word) < 4:
        return word
    tmp = word[1:len(word) - 1]
    new = ''
    for i in range(len(tmp)):
        new += tmp[-i]
    return word[0] + new + word[len(word) - 1]

def typoglycemia_sentence(s):
    words = s.split()
    new_s = []
    for word in words:
        new_s.append(typoglycemia_word(word))
    return ' '.join(new_s)

def main():
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia_sentence(s))

if __name__ == '__main__':
    main()
