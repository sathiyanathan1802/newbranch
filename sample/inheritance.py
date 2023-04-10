# # single inheritance
#
# class father():    #father class base class
#
#     book= "sathya","25"
#     def home(self):
#         print("this is my home")
#
# class son(father):     #child class
#     def phone(self):
#         print("this is my phone")
#
# s=son()
# s.phone()
# s.home()
# print(s.book)
#
#
# mutilvel inheritance
#
# class grandfather():     #base class
#
#     sathya="nathan"
#     def car(self):
#         print("this is my car")
#
# class father(grandfather):  #base class
#     def home(self):
#         print("this is my home")
#
# class son(father):   #child class
#     def phone(self):
#         print("this is my phone")
#
#
# c=son()
# c.home()
# c.phone()
# c.car()
# print(c.sathya)
#
# e=father()
# e.home()
# e.car()
#
# d=grandfather()
# d.car()
# print(d.sathya)
#
#
#  heirachhy inheritance
#
# class father():     #base class
#     sathya="123456"
#     def car(self):
#         print("this is my car")
#
# class daughter(father):     #child class
#     def home(self):
#         print("this is my home")
#
# class son(father):      #child class
#     def phone(self):
#         print("this is my phone")
#
#
# d=daughter()
# d.home()
# d.car()
# print(d.sathya)
#
# s=son()
# s.phone()
# s.car()
# print(s.sathya)
#
# q=father()
# q.car()
# print(q.sathya)



# multiple inheritance
class mother():

    tech="0987"
    def jewel(self):
        print("this is my jewel")

class father():
    mahi="1234"
    def car(self):
        print("this is my car")

class son(father,mother):
    def phone(self):
        print("this is my phone")

s=son()
s.jewel()
s.car()
s.phone()
print(s.tech)
print(s.mahi)

a=father()
a.car()
print(a.mahi)

b=mother()
b.jewel()
print(b.tech)


