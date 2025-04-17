import bisect
import random
import datetime
import sys

SIZE = 70000

random.seed
def black():
    my_list = []
    t_start = datetime.datetime.now()
    for i in range(SIZE):
        new_item = random.randrange(SIZE*2)
        bisect.insort(my_list, new_item)
        #print('%3d -> ' % new_item, my_list)
    print(my_list[6990:])
    print(my_list[-1])
    t_end = datetime.datetime.now()
    print('time= ', t_end - t_start)


def print_pyrs(pyrs):
    pyr_1, pyr_2, pyr_3 = pyrs
    print(f'1= {pyr_1}')
    print(f'2= {pyr_2}')
    print(f'3= {pyr_3}')
    print('_____________________')


def hanoi(n, pyr_1=['A', 'B', 'C'], pyr_2=[], pyr_3=[]):
    pyr_3.append(pyr_1.pop())
    pyr_2.append(pyr_1.pop())
    pyr_2.append(pyr_3.pop())
    pyr_3.append(pyr_1.pop())
    pyr_1.append(pyr_2.pop())
    pyr_3.append(pyr_2.pop())
    pyr_3.append(pyr_1.pop())
    if n - 3 > 0:
        buf = pyr_2
        pyr_2.append(pyr_1.pop)
        # переносим три во второй
        pyr_2.append(hanoi(n - 1, pyr_3, pyr_1, buf))
        #pyr_3.append(hanoi(n - 1, pyr_2, pyr_1, pyr_3))
    print('n=',n)
    return pyr_3


def time_deco(func):
    time_start = datetime.datetime.now()
    func()
    time_end = datetime.datetime.now()
    print(f'\ntime = ', time_end - time_start)


#@time_deco
def time_print():
    num_lines = 100000
    output_numbers = []
    for i in range(num_lines):
        result = i
        output_numbers.append(str(result))
        #print(result)
    print('\n'.join(output_numbers))
    


if __name__ == '__main__':
    #print(hanoi(3, pyr_1=['A', 'B', 'C']))
    #print(hanoi(4, pyr_1=['A', 'B', 'C', 'D']))
    #time_print
    a = sys.stdin.readline()
    print(a)
