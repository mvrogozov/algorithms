def is_sub_seq(arr_to_find, arr):
    if len(arr_to_find) == 0:
        return True
    if len(arr_to_find) >= len(arr):
        return arr_to_find == arr
    sub_seq_index = 0
    for value in arr:
        if arr_to_find[sub_seq_index] == value:
            if sub_seq_index == len(arr_to_find) - 1:
                return True
            sub_seq_index += 1
    return False


def main():
    
    arr_to_find = input()
    arr = input()
    print(is_sub_seq(arr_to_find, arr))


def try_main():
    arr_to_find = ''
    arr = 'agbfdvvvvvvvvvvccccccc'
    print(is_sub_seq(arr_to_find, arr))



if __name__ == '__main__':
    #try_main()
    main()
