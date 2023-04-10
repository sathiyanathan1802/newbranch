#
#
#
# i,j=10,20
# class fun():
#     a = 30
#     b = 40
#     def cool(self,x,y):
#
#        print(x+y)
#        print(self.a+self.b)
#        print(i+j)
#        # print(globals()['i'],globals()['j'])
#
# mc=fun()
# mc.cool(2,4)
#
# i,j,z=1,2,3
#
# class fun():
#     s=12
#     y=13
#     def agil(self,i,j):
#         print(i+j)
#         print(self.s*self.y)
#         print(globals()['i'] + globals()['j'] * globals()['z'])    # call global varible
#
#     # def sat(i,j):    #static variable
#     #     print(i+j)
#
#
#
#
#
# mc=fun()
# mc.agil(10,20)
# # mc.sat(40,50)
# # fun.sat(1,2)
#
#
# # same name as varibale

a,b=20,30

class Spr():

    a=90
    b=23
    def agil(self,a,b):
        print(a*b)
        print(self.a-self.b)
        print(globals()["a"]+globals()["b"])

mc=Spr()
mc.agil(2,2)


