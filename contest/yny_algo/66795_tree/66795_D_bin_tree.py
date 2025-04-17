class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def add(value, tree):
        if tree.value == value:
            print('ALREADY')
            return
        if tree.value > value:
            if tree.left:
                return Tree.add(value, tree.left)
            node = Tree(value)
            tree.left = node
            print('DONE')
            return
        if tree.value < value:
            if tree.right:
                return Tree.add(value, tree.right)
            node = Tree(value)
            tree.right = node
            print('DONE')
            return

    @staticmethod
    def is_in_tree(value, tree):
        if tree.value == value:
            print('YES')
            return
        if tree.value > value:
            if tree.left:
                return Tree.is_in_tree(value, tree.left)
            print('NO')
            return
        if tree.value < value:
            if tree.right:
                return Tree.is_in_tree(value, tree.right)
            print('NO')
            return

    @staticmethod
    def print_tree(tree, n: int = -1):
        n += 1
        if tree.left:
            Tree.print_tree(tree.left, n)
        print('.' * n, end='')
        print(tree.value)
        if tree.right:
            Tree.print_tree(tree.right, n)


tree = None
with open('input.txt') as f:
    data = f.read().splitlines()
    for command in data:
        if command.startswith('ADD'):
            val = int(command.split()[-1])
            if not tree:
                tree = Tree(val)
                print('DONE')
                continue
            tree.add(val, tree)
            continue
        if command.startswith('SEARCH'):
            if tree:
                val = int(command.split()[-1])
                tree.is_in_tree(val, tree)
                continue
            print('NO')
        if command.startswith('PRINTTREE'):
            tree.print_tree(tree)


# data = [5, 15, 6, -4, 0, 9, -100, -1, 2, 35, 8, 6, 10]
# tree = Tree(7)
# # data = [3, 2, 6, 7]
# # tree = Tree(5)

# for item in data:
#     tree.add(item, tree)

# tree.print_tree(tree)
# tree.is_in_tree(-100, tree)
#print_tree(tree)



# def insert_in_tree(value, tree: Tree):
#     if tree.value == value:
#         return 'ALREADY'
#     if tree.value > value:
#         if tree.left:
#             return insert_in_tree(value, tree.left)
#         node = Tree(value)
#         tree.left = node
#         return 'DONE'
#     if tree.value < value:
#         if tree.right:
#             return insert_in_tree(value, tree.right)
#         node = Tree(value)
#         tree.right = node
#         return 'DONE'


# def print_tree(tree: Tree, n: int = -1):
#     n += 1
#     if tree.left:
#         print_tree(tree.left, n)
#     print('.' * n, end='')
#     print(tree.value)
#     if tree.right:
#         print_tree(tree.right, n)

