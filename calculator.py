def addtwo1(c, d):
    added = c + d
    return added

def multiply1(a, b):
    multiplyed = a * b
    return multiplyed

def divison1(a, b):
    divisoned = a / b
    return divisoned

def extraction1(a, b):
    extractioned = a - b
    return extractioned

def add():
    x = int(input("Press number"))
    y = int(input("Press number"))
    e = addtwo1 (x, y)
    print (e)
    
def multiply():
    x = int(input("Press number"))
    y = int(input("Press number"))
    e = multiply1 (x, y)
    print (e)

def division():
    x = int(input("Press number"))
    y = int(input("Press number"))
    e = divison1 (x, y)
    print (e)

def extraction():
    x = int(input("Press number"))
    y = int(input("Press number"))
    e = extraction1 (x, y)
    print (e)

def calculator():
    islem = input("""
(1) + 
(2) x
(3) /
(4) -
(0) Exit""")    
    sayi = int(islem)
    if sayi == 1:
        add()

    if sayi == 2:
        multiply()    
    
    if sayi == 3:
        division()
    
    if sayi == 4:
        extraction()

    if sayi == 0:
        exit(0)
    calculator()

calculator()



