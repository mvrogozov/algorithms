class Stack:
    def __init__(self):
        self.array = []
        self.sum = 0
        self.pref_sum = [0]

    def pop(self):
        self.pref_sum.pop()
        return self.array.pop()

    def get_k_sum(self, k: int):
        return self.pref_sum[-1] - self.pref_sum[- k - 1]

    def push(self, n: int):
        self.array.append(n)
        self.pref_sum.append(self.pref_sum[-1] + n)

def main():
    n = int(input())
    stack = Stack()
    for _ in range(n):
        command = input()
        if command.startswith('+'):
            stack.push(int(command[1:]))
        if command.startswith('-'):
            print(stack.pop())
        if command.startswith('?'):
            print(stack.get_k_sum(int(command[1:])))

main()

print('#####')
a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print('_____')
print(a.pref_sum)
print(a.get_k_sum(1))
print(a.get_k_sum(2))
print(a.get_k_sum(3))
print(a.get_k_sum(4))
print('_____')
a.pop()
print(a.array)
a.pop()
print(a.array)