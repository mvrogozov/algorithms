class A:
    def __init__(self, *args):
        self.param_a = args[0]

    @classmethod
    def cl_met(cls):
        return f'cls method -> '
    
    def inst_met(self):
        return f'inst method -> {self.param_a}'
    

a = A('aaaa')

print(A.cl_met())
print(A.inst_met(a))