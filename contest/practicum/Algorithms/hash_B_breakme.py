def get_poli_hash(alpha, modul, string):
    result = ord(string[0])
    for value in string[1:]:
        result = result * alpha + ord(value) % modul
    return result % modul


def get_equal_hash_string():
    alpha = 1000
    m = 123987123
    table = [None] * m
    for l_text in range(3, 10):
        text = list(char_combine('', l_text).split())
        for item in text:
            hash = get_poli_hash(alpha, m, item)
            if table[hash]:
                print(f'item = {item}, hash = {hash}')
                return f'{table[hash]}, {item}'
            table[hash] = item
    return f'nothing {text[-5:]}'


def char_combine(text, length):
    if len(text) >= length:
        return text
    result = ''
    for index in range(97, 123):
        result += char_combine(text + chr(index), length) + ' '
    return result


def main():
    print(get_equal_hash_string())


if __name__ == '__main__':
    main()
