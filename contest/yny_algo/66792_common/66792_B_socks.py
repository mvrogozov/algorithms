# bm = int(input())
# rm = int(input())
# bn = int(input())
# rn = int(input())
"""
B. Майки и носки
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Как известно, осенью и зимой светает поздно и так хочется утром ещё хоть немного поспать,
а не идти в школу! Некоторые школьники готовы даже одеваться, не открывая глаз, лишь бы отложить
момент пробуждения. Вот и Саша решил, что майку и носки он вполне может вытащить из шкафа на ощупь
с закрытыми глазами и только потом включить свет и одеться. В шкафу у Саши есть два ящика.
В одном из них лежит 
A
A синих и 
B
B красных маек, в другом — 
C
C синих и 
D
D красных пар носков. Саша хочет, чтобы и майка, и носки были одного цвета. Он вслепую вытаскивает 
M
M маек и 
N
N пар носков. В первое же утро Саша задумался, какое минимальное суммарное количество предметов одежды (
M
+
N
M+N) он должен вытащить, чтобы среди них гарантированно оказались майка и носки одного цвета. 
Какого именно цвета окажутся предметы одежды, для Саши совершенно неважно.

Формат ввода
На вход программе подаются четыре целых неотрицательных числа 
A
A, 
B
B, 
C
C, 
D
D, записанных в отдельных строках: 
A
A — количество синих маек, 
B
B — количество красных маек, 
C
C — количество синих носков, 
D
D — количество красных носков. Все числа не превосходят 
1
0
9
10 
9
 . Гарантируется, что в шкафу есть одноцветный комплект из майки и носков.

Формат вывода
Программа должна вывести два числа: количество маек 
M
M и количество пар носков 
N
N, которые должен взять Саша. Необходимо, чтобы среди 
M
M маек и 
N
N пар носков обязательно нашлась одноцветная пара, при этом сумма 
M
+
N
M+N должна быть минимальной.

Пример
Ввод	Вывод
6
2
7
3
3 4
Примечания
В примере из условия в шкафу лежит 
A
=
6
A=6 синих маек и 
B
=
2
B=2 красных маек. Если взять 3 майки, то среди них обязательно найдётся синяя. В другом ящике лежит 
C
=
7
C=7 пар синих носков и 
D
=
3
D=3 пары красных носков. Если взять 4 пары, то среди них обязательно будет пара синих носков.
Поэтому если взять вслепую 3 майки и 4 пары носков, то среди них обязательно найдётся одноцветный
(синий) комплект из майки и носков.
"""

def get_min_tries2(bm: int, rm: int, bn: int, rn: int) -> int:
    if bm == 0:
        return (1, bn + 1)
    if rm == 0:
        return (1, rn + 1)
    if bn == 0:
        return (bm + 1, 1)
    if rn == 0:
        return (rn + 1, 1)
    if bm == rm:
        if bn == rn:
            if bm >= rn:
                return (1, rn + 1)
            return (bm + 1, 1)
        if bn > rn:
            return (1, rn + 1)
        if bn < rn:
            return (1, bn + 1)
    if bn == rn:
        if bm > rm:
            return (rm + 1, 1)
        if bm < rm:
            return (bm + 1, 1)
    if bm >= rm:
        if bn >= rn:
            return (rm + 1, rn + 1)
        return (rm + 1, bn + 1)
    if bn >= rn:
        return (bm + 1, rn + 1)
    return (bm + 1, bn + 1)


def get_min_tries(bm: int, rm: int, bn: int, rn: int) -> int:
    gbm = rm + 1
    grm = bm + 1
    gbn = rn + 1
    grn = bn + 1
    if bm != 0 and rm != 0 and bn != 0 and rn != 0:
        am = max(bm, rm) + 1
        an = max(bn, rn) + 1
        if am < an:
            if (am < (grm + grn)) and (am < (gbm + gbn)):
                return am, 1
        else:
            if (an < (grm + grn)) and (an < (gbm + gbn)):
                return 1, an

    if bm == rm:
        return gbm, 1
    if bn == rn:
        return 1, gbn

    if ((gbm + gbn) > (grm + grn)) or (bm == 0 or bn == 0):
        # тащим красные
        return grm, grn
    return gbm, gbn

bm, rm, bn, rn = 6, 2, 7, 3
print('\n', bm, rm, bn, rn, ' -> ', *get_min_tries(bm, rm, bn, rn))
assert (get_min_tries(bm, rm, bn, rn)) == (3, 4)

bm, rm, bn, rn = 790, 493, 507, 302
print('\n', bm, rm, bn, rn, ' -> ', *get_min_tries(bm, rm, bn, rn))
assert (get_min_tries(bm, rm, bn, rn)) == (3, 4)


bm, rm, bn, rn = 10, 7, 0, 4
print('\n', bm, rm, bn, rn, ' -> ', *get_min_tries(bm, rm, bn, rn))
assert (get_min_tries(bm, rm, bn, rn)) == (11, 1)


bm, rm, bn, rn = 0, 2, 7, 3
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))
assert (get_min_tries(bm, rm, bn, rn)) == (1, 8)


bm, rm, bn, rn = 1, 1, 1, 1
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))
assert (get_min_tries(bm, rm, bn, rn)) == (2, 1)


bm, rm, bn, rn = 8, 9, 5, 9
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))

bm, rm, bn, rn = 5, 0, 3, 0
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))

bm, rm, bn, rn = 2, 22, 3, 3
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))

bm, rm, bn, rn = 66, 2, 7, 7
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))

bm, rm, bn, rn = 6, 2, 7, 0
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))

bm, rm, bn, rn = 6, 2, 0, 7
assert get_min_tries(bm, rm, bn, rn) == (7, 1)

bm, rm, bn, rn = 2, 6, 0, 7
assert get_min_tries(bm, rm, bn, rn) == (3, 1)

bm, rm, bn, rn = 1, 1, 1, 1
print(get_min_tries(bm, rm, bn, rn))
assert get_min_tries(bm, rm, bn, rn) == (2, 1)

bm, rm, bn, rn = 1, 11, 11, 1
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))
assert get_min_tries(bm, rm, bn, rn) == (12, 1)

bm, rm, bn, rn = 1, 11, 1, 11
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))
assert get_min_tries(bm, rm, bn, rn) == (2, 2)

bm, rm, bn, rn = 11, 1, 1, 11
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))
assert get_min_tries(bm, rm, bn, rn) == (12, 1)

bm, rm, bn, rn = 0, 1, 0, 1
print('\n', bm, rm, bn, rn, ' -> ', get_min_tries(bm, rm, bn, rn))
assert get_min_tries(bm, rm, bn, rn) == (1, 1)