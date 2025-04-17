a = 'aaaaazalll'
b = 'aazzaal'
c = 'azal'

# b = a
# c = a



def get_min_str(a_str: str, b_str: str, c_str: str):
    result = ''
    a_sub = a_str
    b_sub = b_str
    c_sub = c_str
    while a_sub and b_sub and c_sub:
        if a_sub:
            letter = a_sub[0]
        elif b_sub:
            letter = b_sub[0]
        else:
            letter = c_sub[0]
        count_a = count_b = count_c = 0
        if (b_sub and b_sub[0] != letter) or (c_sub and c_sub[0] != letter) or (a_sub and a_sub[0] != letter):
            return 'IMPOSSIBLE'
        while a_sub and a_sub[0] == letter:
            count_a += 1
            a_sub = a_sub[1:]
        while b_sub and b_sub[0] == letter:
            count_b += 1
            b_sub = b_sub[1:]
        while c_sub and c_sub[0] == letter:
            count_c += 1
            c_sub = c_sub[1:]
        
        
        s_max = max(count_a, count_b, count_c)
        s_min = min(count_a, count_b, count_c)
        amount = s_max - s_min
        steeps_to_dif = abs(count_a - amount) + abs(count_b - amount) + abs(count_c - amount)
        steeps_to_max = abs(count_a - s_max) + abs(count_b - s_max) + abs(count_c - s_max)
        steeps_to_min = abs(count_a - s_min) + abs(count_b - s_min) + abs(count_c - s_min)
        steps_to_a = abs(2 * count_a - (abs(count_b) + abs(count_c)))
        steps_to_b = abs(2 * count_b - (abs(count_a) + abs(count_c)))
        steps_to_c = abs(2 * count_c - (abs(count_b) + abs(count_a)))
        cur_min = min(steeps_to_dif, steeps_to_max, steeps_to_min, steps_to_a, steps_to_b, steps_to_c)
        if cur_min == steeps_to_min:
            amount = s_min
        elif cur_min == steeps_to_max:
            amount = s_max
        elif cur_min == steps_to_a:
            amount = count_a
        elif cur_min == steps_to_b:
            amount = count_b
        elif cur_min == steps_to_c:
            amount = count_c
        # if amount == 0:
        #     amount = count_a
        result += letter * amount
    if a_sub or b_sub or c_sub:
        return 'IMPOSSIBLE'
    return result

print(get_min_str(a, b, c))