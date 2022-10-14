class A:
    def do(self):
        print("defined in A")


class B(A):
    def do(self):
        print("defined in B")


class C(A):
    def do(self):
        print("defined in C")


class D(B, C):
    def do(self):
        print("defined in D")


t = D()
t.do()
print(D.__mro__)
print(D.mro())
print(help(D))
