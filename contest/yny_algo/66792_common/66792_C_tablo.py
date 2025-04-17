# I, O, C, L, H, P
# n = int(input())
# data = []
# for row in range(n):
#     data.append(list(input()))


def compress(data: list) -> list:
    if not data:
        return None
    ans = [data[0]]
    for row in data[1:]:
        if row != ans[-1]:
            ans.append(row)
    if set(ans[0]) == {'.'}:
        ans.pop(0)
    if ans and set(ans[-1]) == {'.'}:
        ans.pop()
    return ans

def transpone_matrix(data: list) -> list:
    if not data:
        return None
    ans = []
    for _ in range(len(data[0])):
        ans.append([])
    for row_num in range(len(data)):
        for ch_pos, ch in enumerate(data[row_num]):
            ans[ch_pos].append(ch)
    return ans


def matcher(n: int, data: list):
    result = compress(data)
    result = transpone_matrix(result)
    result = compress(result)
    result = transpone_matrix(result)
    if result == [
        ['#', '#', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
    ]:
        print('O')

    elif result == [
        ['#'],
    ]:
        print('I')

    elif result == [
        ['#', '#', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
        ['#', '.', '.'],
    ]:
        print('P')

    elif result == [
        ['#', '.', '#'],
        ['#', '#', '#'],
        ['#', '.', '#'],
    ]:
        print('H')

    elif result == [
        ['#', '#'],
        ['#', '.'],
        ['#', '#'],
    ]:
        print('C')

    elif result == [
        ['#', '.'],
        ['#', '#'],
    ]:
        print('L')

    else:
        print('X')

def matcher2(n: int, data: list):
    result = ''
    if is_i(n, data):
        result += 'I'
    if is_o(n, data):
        result += 'O'
    if result:
        return(result)
    else:
        return('X')

def is_i(n: int, data: list) -> str:
    detected = False
    start_string = 0
    pause_detected = False
    blank_string_detected = False
    symbol_positions = []
    for str_num, string in enumerate(data):
        for pos, symbol in enumerate(string):
            if symbol == '#': # and not detected:
                if not detected:
                    detected = True
                    start_string = str_num
                    symbol_positions.append(pos)
                    continue
                if detected and start_string == str_num:
                    symbol_positions.append(pos)
                    continue ##################################
                if detected and blank_string_detected:
                    return False
                if pos not in symbol_positions:
                    return False
            if symbol == '.' and detected:
                if str_num == 0:
                    pause_detected = True
                    continue #########################
                if pos in symbol_positions:
                    for inner_item in string[pos:]:
                        if inner_item != '.':
                            return False
                    blank_string_detected = True
                    #return False
            if str_num == 0:
                if symbol == '#' and pause_detected:
                    return False
    return detected


# def get_letter(n: int, data: list):
#     top_left = []
#     horizontal = []
#     vertical = []
#     for row_num, row in enumerate(data):
#         for pos, symbol in enumerate(row):
#             if symbol == '#':
#                 if not top_left:
#                     top_left = [row_num, pos]
#                     edge_row = row
#                     opened = True
#                     # check all cols from left side
#                     for lrow in data[row_num + 1:]:
#                         if not is_dots_only(lrow[:pos]):
#                             return False

def is_dots_only(row: list):
    for item in row:
        if item != '.':
            return False
    return True


def is_o(n: int, data: list) -> str:
    top_left = []
    top_right = []
    edge_row = []
    middle_row = []
    bottom_left = []
    bottom_right = []
    inner_top_left = []
    inner_top_right = []
    inner_bottom_left = []
    inner_bottom_right = []
    left_start_scan = 0
    opened = False
    middle_started = False
    closed = False
    for row_num, row in enumerate(data):
        if is_dots_only(row):
            if opened and not closed:
                return False
            continue
        if row == edge_row:
            if opened:
                if middle_started:
                    closed = True
            continue
        if row == middle_row:
            if opened:
                middle_started = True
            else:
                return False
            if closed:
                return False
        if opened and middle_started:
            if row != edge_row or row != middle_row:
                return False

        first_h_found = False
        second_h_found = False
        pause_in_mid_found = False
        for pos, symbol in enumerate(row):
            if symbol == '#':
                if not top_left:
                    top_left = [row_num, pos]
                    edge_row = row
                    opened = True
                    # check all cols from left side
                    for lrow in data[row_num + 1:]:
                        if not is_dots_only(lrow[:pos]):
                            return False
                if pos == n - 1:
                    if not top_right:
                        top_right = [row_num, pos]
                if row_num != top_left[0]: # not first row
                    if pause_in_mid_found:
                        # if not pos == n - 1:
                        #     if not is_dots_only(row[pos + 1]):
                        #         return False
                        second_h_found = True
                        middle_row = row
                        middle_started = True
                    first_h_found = True

            if symbol == '.':
                if top_left and row_num == top_left[0]: # if top edge row
                    if not top_right:
                        top_right = [row_num, pos - 1]

                        # check all cols from right side
                        if not pos == n - 1:
                            for rrow in data[row_num:]:
                                if not is_dots_only(rrow[top_right[1] + 1:]):
                                    return False
                    continue
                if first_h_found:
                    pause_in_mid_found = True
                if second_h_found and pos != n - 1:
                    if not is_dots_only(row[pos + 1:]):
                        return False
                    top_right = [row_num, pos - 1]
    return closed
                    
# n = 4
# test_data = [
#     ['.', '#', '#', '#'],
#     ['.', '#', '.', '#'],
#     ['.', '#', '#', '#'],
#     ['.', '.', '.', '.'],
# ]
# print(matcher(n, test_data))

n = 10
test_data = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '#', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '#', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
]

test_data = [
    ['.', '.'],
    ['.', '.']
]
print(matcher(n, test_data))


n = 5
test_data = [
    ['.', '#', '#', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
]
# print(matcher(n, test_data))





# row = ['.', '.']
# print(is_dots_only(row))

# row = ['.', '#']
# print(is_dots_only(row))



# n = 4
# test_data = [
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '.', '.', '.'],
# ]
# print('\n', matcher(n, test_data))
# assert matcher(n, test_data) == 'I'

# n = 4
# test_data = [
#     ['.', '.', '.', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '.', '.', '.'],
# ]
# print('\n', matcher(n, test_data))
# assert matcher(n, test_data) == 'I'

# n = 4
# test_data = [
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '#'],
#     ['.', '.', '.', '.'],
# ]
# print('\n', matcher(n, test_data))
# assert matcher(n, test_data) == 'X'

# n = 4
# test_data = [
#     ['#', '#', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '.', '.', '.'],
# ]
# print('\n', matcher(n, test_data))
# assert matcher(n, test_data) == 'X'

# n = 4
# test_data = [
#     ['.', '.', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '.', '.', '.'],
# ]
# print('\n', matcher(n, test_data))
# assert matcher(n, test_data) == 'X'

# n = 4
# test_data = [
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '.'],
#     ['.', '#', '#', '.'],
# ]
# print('\n', matcher(n, test_data))
# assert matcher(n, test_data) == 'I'

# n = 1
# test_data = [
#     ['#'],
# ]
# print('\n', matcher(n, test_data))
# assert matcher(n, test_data) == 'I'

# n = 1
# test_data = [
#     ['.'],
# ]
# print('\n', matcher(n, test_data))
# assert matcher(n, test_data) == 'X'
