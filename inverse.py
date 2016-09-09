from sympy.abc import x,y
from sympy import *
def inverse(f):
    func = []
    for letters in f:
        if letters == "x":
            func.append("y")
        else:
            func.append(letters)
    invfunc = ""
    for letters in func:
        invfunc += str(letters)

    invfunc += "-x"
    invfunc = solve(invfunc, y)
    invfunc = "f**-1(x)=" + str(invfunc)
    print(invfunc)

ffunc = input("Please enter a function: ")
inverse(ffunc)


