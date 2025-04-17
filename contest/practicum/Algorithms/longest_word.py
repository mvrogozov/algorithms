def read_input():
    l = int(input())
    words = list(map(str, input().strip().split()))
    return l,words

def find_longest(l,text):
    longest_word = ''
    max_length = 0

    for word in text:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return longest_word, max_length


if __name__ == '__main__':
    l, text = read_input()
    print('\n'.join(map(str, find_longest(l,text))))