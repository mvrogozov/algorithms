def gen_binary(n, prefix):
    if n == 0:
        print(prefix)
    else:
        gen_binary(n - 1, prefix + '0')
        gen_binary(n - 1, prefix + '1') 

gen_binary(3,'')


a = [[2, 3], [2, 1], [1, 10], [2, 1, 2]]
a.sort()
print(a)