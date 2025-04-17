from datetime import datetime


def get_poli_hash(alpha, modul, string):
    result = ord(string[0])
    for value in string[1:]:
        result = (result * alpha + ord(value)) % modul
    return result % modul


def slide_hash(alpha, modul, text):
    table = {}
    length = len(text)
    last_letter = text[0]
    for sub_len in range(1, length + 1):
        #print('1st text = ', text[0:sub_len])
        first_hash = get_poli_hash(alpha, modul, text[0:sub_len])
        table[(1, sub_len)] = first_hash

        '''for index in range(1, length - sub_len + 1):
            #print(text[index:sub_len + 1])
            table[(index + 1, index + sub_len)] = (
                (first_hash - ord(last_letter) * alpha ** (sub_len - 1 )) # lastletter?
                * alpha + ord(text[index + sub_len - 1])
            ) % modul'''
    return table


def slide_hash2(alpha, modul, text):
    table = {}
    length = len(text)
    for sub_len in range(1, length + 1):
        #print('1st text = ', text[0:sub_len])
        first_hash = get_poli_hash(alpha, modul, text[0:sub_len])
        table[(1, sub_len)] = first_hash

        for index in range(1, length - sub_len + 1):
            #print(text[index:sub_len + 1])
            first_hash = (
                (first_hash - ord(text[index - 1]) * alpha ** (sub_len - 1 )) # lastletter?
                * alpha + ord(text[index + sub_len - 1])
            ) % modul
            table[(index + 1, index + sub_len)] = first_hash
    return table



def get_substring_hash(alpha, modul, text, indexes):
    table = slide_hash(alpha, modul, text)
    length = indexes[1] - indexes[0] + 1
    last_hash = table[(1, length)]
    for index in range(1, indexes[0]):
        last_hash = (
            (last_hash - ord(text[index - 1]) * alpha ** (length - 1))
            * alpha + ord(text[index + length - 1])
        ) % modul
    return last_hash


def get_hash_table(alpha, modul, text):
    table = {}
    length = len(text)
    for index in range(length):
        for index_in in range(index, len(text)):
            table[(index + 1, index_in + 1)] = get_poli_hash(
                alpha, modul, text[index:index_in + 1]
            )
    return table



def main():
    alpha = int(input())
    modul = int(input())
    text = input() # * 100

    '''time_start = datetime.now()
    table = slide_hash(alpha, modul, text)
    time_stop = datetime.now()
    print('table time1 = ', time_stop - time_start)

    time_start = datetime.now()
    table = get_hash_table(alpha, modul, text)
    time_stop = datetime.now()
    print('table time2 = ', time_stop - time_start)'''
    requests_amount = int(input())
    table = slide_hash2(alpha, modul, text)
    #print(table)
    result = ''
    for index in range(requests_amount):
        table_key = tuple(map(int, input().split()))
        ##print(get_substring_hash(alpha, modul, text, table_key))    
        #result += str(table[table_key]) + '\n'
        #print(table[table_key])
        print(table[table_key])

def main1():
    alpha = 1000
    modul = 1000009
    text = 'xzabcdefgh'
    table = slide_hash(alpha, modul, text) #get_hash_table(alpha, modul, text)
    print(table)
    table = slide_hash2(alpha, modul, text)
    print('t2 =', table)
    print(get_substring_hash(alpha, modul, text, (3, 9)))
    '''for index in range(requests_amount):
        table_key = tuple(map(int, input().split()))
        print(table[table_key])
'''


if __name__ == '__main__':
    main()
