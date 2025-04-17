def read_input():
    s = str(input())
    t = str(input())
    return s,t

def find_letter(s,t):
    dict_s = {}
    dict_t = {}
    for letter in s:
        dict_s[letter] = dict_s.get(letter, 0) + 1
    for letter in t:
        dict_t[letter] = dict_t.get(letter, 0) + 1
    for key in dict_t.keys():
        letters_s = dict_s.get(key, -1)
        if letters_s == -1:
            return key
        letters_t = dict_t.get(key)
        if letters_t > letters_s:
            return key

if __name__ == '__main__':
    s,t = read_input()
    print(find_letter(s,t))