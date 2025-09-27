#simple calculator 
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b!=0:
        return a/b
    else:
        return ZeroDivisionError