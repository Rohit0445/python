class A:
    __x = 10
    def __private():
        print("private method ")

class B(A):
    pass 

obj = B()
# print(obj.__x)
# print(obj.__private())
# print(A.__x)
# print(A.__private())
# print(dir(A))

# BY namemangling

# print(obj._A__x)
obj._A__private()
