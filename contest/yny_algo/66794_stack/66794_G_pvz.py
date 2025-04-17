import random
import time


def get_sum_time(n: int, b: int, data: list[int]):
    deque = [None] * n
    ans = 0
    deq_pos = 0
    deq_start = 0
    for i in range(n):
        this_minute_may_serve = b
        deque[deq_pos] = [data[i], i]
        while deq_start < n and deque[deq_start]:
            if this_minute_may_serve >= deque[deq_start][0]:
                this_minute_may_serve -= deque[deq_start][0]
                ans += deque[deq_start][0] * (i + 1 - deque[deq_start][1])
                deq_start += 1
                continue
            else:
                deque[deq_start][0] -= this_minute_may_serve
                ans += this_minute_may_serve * (i + 1 - deque[deq_start][1])
                break
        deq_pos += 1
    for item in deque[deq_start:]:
        ans += item[0] * (n + 1 - item[1])

    return ans

# n, b = (map(int, input().split()))
# data = list(map(int, input().split()))
# print(get_sum_time(n, b, data))


n, b = 3, 4
data = [1, 5, 9]
print(get_sum_time(n, b, data))
print()

n, b = 1, 4
data = [1]
print(get_sum_time(n, b, data))
print()

n, b = 6, 40
data = [92, 64, 25, 75, 51, 57]
print(get_sum_time(n, b, data))
print()

n, b = 99999, 40
data = [random.randint(1, 99) for _ in range(100000)]
start_time = time.time()
print(get_sum_time(n, b, data))
print(f'DONE for {time.time() - start_time}')
print()