

a=50
z=22 #global varible
def cool():
    global c
    global z
    a=10  #local varible
    b=20
    c=23
    print(a, b)

cool()
print(a,c,z)
print(c)
print(a)

