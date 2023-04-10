


# def argu(x,y):
#     print(x,y)
#
# argu(10,90)  #positional argument
#
# argu(x=89,y=90)#keyword arguments
# argu(45,y=77)  #combining both positional as well as keyword arguments
# argu(x=0,y=9)

#combining both positional as well as keyword arguments
a=10                #it can acess everyehere in to function global varibale
def argu(x=12,y=34):

    print(a,x,y)
argu()
argu(100,200)
argu(13333,3333)


#Example : function can return multiple values


def sath(a,b):
    if a<b:
        return a,b
    else:
        return b,a
print(sath(100,20))     #postional argument #its return as tuple() round brackets
print(sath(b=90,a=25))      #keyword argument
