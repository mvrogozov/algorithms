import re

a = 'exh_art/event'

regex = re.compile(r'[^a-zA-Z0-9]')

match = regex.sub('', a)
#print(match)
def count_distinct(n: int) -> int:
    """Count distinct search trees with n unique numbers."""
    if n == 0:
        return 1
    result = 0
    for i in range(1, n + 1):
        result += (
            count_distinct(i - 1) * count_distinct(n - i) 
        )
        print(f'i={i}, n={n}, {result}')
    return result


def get_factorial(n: int):
    if n == 1:
        return 1
    return n * get_factorial(n - 1)

def get_katalan_number(n):
    a = get_factorial(2 * n)
    b = get_factorial(n + 1)
    c = b / (n + 1)
    return int(a / (b * c))


#n = int(input())
#print(get_katalan_number(n))


class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def print_reverse_tree(vertex: Node):
    if vertex.left is not None:
        print_reverse_tree(vertex=vertex.left)
    if vertex.right is not None:
        print_reverse_tree(vertex=vertex.right)
    print(vertex.value, end=' -> ')


def lmr_tree(node: Node):
    if node.left:
        lmr_tree(node.left)
    if node.right:
        lmr_tree(node.right)
    print(node.value)


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

#print_reverse_tree(a)
print(lmr_tree(a))