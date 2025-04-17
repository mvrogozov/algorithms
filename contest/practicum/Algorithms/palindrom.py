import re


def read_input():
    text = input()
    new_text = re.sub(r'[^\w\s]', '', text)
    words = list(map(str, new_text.strip().split()))
    return words


def is_palindrom(text):
    string = text.lower()
    return string == string[::-1]


if __name__ == '__main__':
    #text = read_input()
    text = "Tratata \n kukaracha upyrka"
    sp = list(range(10))
    print(sp)
    sp [2:5] = [20, 30, 40, 50]
    print(sp)
    second_word = slice(9, 20)
    #print(text[second_word])
    #print(is_palindrom(text))
