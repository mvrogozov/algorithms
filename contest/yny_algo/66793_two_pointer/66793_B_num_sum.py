

# def count_sums(n: int, k: int, data: list[int]) -> int:
#     cntr = 0
#     pref_sum = [0]
#     last_pos = 0
#     for pos, value in enumerate(data):
#         cur_sum = pref_sum[pos] + value
#         if cur_sum == k:
#             cntr += 1
#             pref_sum.append(value)
#             last_pos = pos + 1
#             continue
#         if cur_sum > k:
#             for pref_val in reversed(pref_sum[last_pos : pos]):
#                 if pref_sum[pos] - pref_val + value == k:
#                     cntr += 1
#                     last_pos = pos + 1
#                     break
#             pref_sum.append(value)
#             continue
#         pref_sum.append(cur_sum)
#     print(pref_sum)
#     return cntr


def count_sums(n: int, k: int, data: list[int]) -> int:
    cntr = 0
    pref_sum = [0]
    pairs = set()
    last_index = len(data) - 1
    suf_sum = [0]
    last_pos = 0
    last_pos_back = last_index
    for pos, value in enumerate(data):
        back_value = data[last_index - pos]
        cur_sum = pref_sum[pos] + value
        cur_sum_back = suf_sum[pos] + back_value
        if cur_sum < k:
            pref_sum.append(cur_sum)
        if cur_sum_back < k:
            suf_sum.append(cur_sum_back)

        if cur_sum == k:
            pairs.add((last_pos, pos + 1))
            pref_sum.append(value)
            last_pos = pos

        if cur_sum_back == k:
            pairs.add((last_index - pos, last_pos_back + 1))
            suf_sum.append(back_value)
            last_pos_back = last_index - pos

        if cur_sum > k:
            pref_sum.append(value)
            last_pos = pos

        if cur_sum_back > k:
            suf_sum.append(back_value)
            last_pos_back = last_index - pos
    #return len(pairs)
        
        
    print(pref_sum)
    print(pairs)
    return cntr


def sliding_sum(n: int, k: int, data: list[int]) -> int:
    cnt = 0
    start = 0
    cur_sum = 0
    for pos in range(len(data)):
        cur_sum += data[pos]
        while cur_sum > k and start < pos:
            cur_sum -= data[start]
            start += 1
        if cur_sum == k:
            cnt += 1
            cur_sum -= data[start]
            start += 1
            continue
    return cnt

def get_prefix_sum(data: list) -> list:
    result = []
    for pos, item in enumerate(data):
        if pos == 0:
            result.append(item)
            continue
        result.append(result[pos - 1] + item)
    return result

def count_pref_sums(n: int, k: int, data: list[int]) -> int:
    cntr = 0
    pref_sum = get_prefix_sum(data)
    last_pos = 0
    for pos in range(len(pref_sum) - 1, -1,  -1):
        if pref_sum[pos] == k:
            cntr += 1
            break
        if pref_sum[pos] < k:
            break
        for i in range(pos, -1, -1):
            if pref_sum[pos] - pref_sum[i] == k:
                cntr += 1
                break
    return cntr



# n, k = list(map(int, input().split()))
# data = list(map(int, input().split()))
# print(count_pref_sums(n, k, data))

n = 10 
k = 5
data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print(data)
print(sliding_sum(n, k, data))
#print(count_sums(n, k, data))
print()


n = 5
k = 17
data = [17, 7, 10, 7, 10]
print(data)
print(sliding_sum(n, k, data))
print()

n = 5
k = 10
data = [1, 2, 3, 4, 1]
print(data)
print(sliding_sum(n, k, data))
#sprint(count_pref_sums(n, k, data))
print()

n = 5
k = 107
data = [17, 3, 4, 100, 3, 4, 10, 7]
print(data)
print(sliding_sum(n, k, data))
#print(count_pref_sums(n, k, data))
print()