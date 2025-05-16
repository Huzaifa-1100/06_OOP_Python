class A:
    def show(self):
        print("A.show()")


class B(A):
    def show(self):
        print("B.show()")


class C(A):
    def show(self):
        print("C.show()")


class D(B, C):
    pass


# Example Usage
d = D()
d.show()  # MRO: B.show() is called because B comes before C in the inheritance order
print(D.mro())  # Print Method Resolution Order