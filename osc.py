"""
Напишите функцию sum_unique_numbers(), которая принимает список чисел 
и возвращает сумму только уникальных чисел (которые не повторяются).

Пример:
sum_unique_numbers([1, 2, 2, 3, 4, 4, 5]) должен вернуть 9 
(так как только 1, 3 и 5 встречаются один раз)
"""

def sum_unique_num(arr: list[int]) -> int:
    counter = {}
    sum = 0
    for num in arr:
        amount = counter.setdefault(num, 0)
        amount += 1
        counter[num] = amount
    for key, val in counter.items():
        if val > 1:
            continue
        sum += key
    return sum
    
    
a = [1, 2, 2, 3, 4, 4, 5]
res = sum_unique_num(a)
print(res)