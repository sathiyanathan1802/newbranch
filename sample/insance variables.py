

class Myclass:
    a,b=90,80
    def cool(self):
        print(self.a*self.b)

    def mul(name):  #Instance method
        print(name.a/name.b)

m=Myclass()
m.cool()
m.mul()

print(m.a,m.b)
