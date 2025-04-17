from collections import namedtuple


a = [0] * 3
b = list(range(10))
print(a)

c = namedtuple('cars', 'name1 name2') #['name1', 'name2'])
d = c('bmw', 'audi')
print(d[0], ' = ', d[1])