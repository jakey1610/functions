from sympy import expand, factor
from sympy.abc import x,y
def composite(f,g):
    #formatting basics:
    #x**2 is equal to x squared
    #x*(x+1) needs to be written to multiply two objects together
    compfunc = []
    for letters in f:
        if letters == "x":
            compfunc.append("(")
            compfunc.append(g)
            compfunc.append(")")
        else:
            compfunc.append(letters)
    function = ""
    for letters in compfunc:
        function += letters

    #expand the function here

    expfunc = expand(function)
    print(expfunc)


