from datetime import datetime

def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes

def eratosthenes_effective(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers


def method5(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out     

def to_prime(num):
    result = ''
    if num == 1:
        return 1
    prime = 2
    t1 = datetime.now()
    #prime_list = get_least_primes_linear(num)
    t2 = datetime.now()
    print('start while - > ', t2-t1)
    i = 2
    while i * i < num:
        
        '''if num in prime_list:
            print('prime')
            result += str(num)
            break'''
        while num % i != 0:
            if num == i:
                break
            i += 1
        result += str(i) + ' '
        num = num // i
    t2 = datetime.now()
    if num > 1:
        result += num
    print('start while - > ', t2-t1)
    return result

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(n))
   return primfac

if __name__ == '__main__':
    print(to_prime(int(70578583)))
    #print(' '.join(map(str, primfacs(int(input())))))