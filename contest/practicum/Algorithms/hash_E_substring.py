def get_longest_sub_string(text):
    buffer = set()
    print(text)
    buffer_back = set()
    length_back = 0
    length = 0
    substr1 = ''
    substr2 = ''
    max_length = 0
    for index, elem in enumerate(text):
        if elem in buffer:
            print(substr1, ' -1')
            length = 1
            substr1 = elem
            buffer = set(elem)
        else:
            substr1 += elem
            length += 1
            buffer.add(elem)
        if text[-index - 1] in buffer_back:
            print(substr2, ' -2')
            substr2 = (text[-index - 1])
            length_back = 1
            buffer_back = set(text[-index - 1])
        else:
            substr2 += (text[-index - 1])
            length_back += 1
            buffer_back.add(text[-index - 1])
        #max_length = max(max_length, length, length_back)
        if max_length < length:
            max_length = length
            print(f'index = {index}, max = {max_length}')
        if max_length < length_back:
            max_length = length_back
            print(f'index = {index}, max = {max_length}')
    return max_length


def get_max_length(text):
    length = 0
    buffer = set()
    max_length = 0
    for index in range(len(text)):
        for value in text[index:]:
            if value in buffer:
                length = 0
                buffer = set()
                break
            else:
                length += 1
                buffer.add(value)
                if length > max_length:
                    max_length = length
                #max_length = max(max_length, length)
    return max_length


def main():
    #text = 'ojodx'
    #text = 'jgmqxnmdclxoexyswnpvowxojznizqrdjqzqozshigqvrfaekrabnwnvhejhvzozkpgwfjujethblmiscvjtfcqwcwpbdowvstkesvmfacmlejxuutvfjbnicxawcauaplrcrsufeotdhwhcejmuwceyyxnlrbanqognhrliwxtduvyswvlwxgtfvkzxdotkxduzdwtumznszvvyvnjohgmpptrsefodurvqjsztqirwpfrpysaqxkdiqfahcckzeyavtqwgwpdyizvbxdcahkrfplrhaxavomlzwkokilfrmfwlhzxhjbctmuogwzogesjxxirzemueofignbzwunswbhvjsgvhtgiqcacrotucixvxdyeypmubhge'
    #text = 'mfwlhzxhjbctmuogwzogesjxxirzemueofignbzwunswbhvjsg'
    text = input()
    #print(get_longest_sub_string(text))
    print(get_max_length(text))

if __name__ == '__main__':
    main()
