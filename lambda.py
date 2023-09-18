# x=lambda  a,b,c :a+30+b*c
# print(x(7,7,4))

def fun(n):
    return  lambda   b:b+n
x=fun(2)
print(x(8))