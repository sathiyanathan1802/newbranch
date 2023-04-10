

# overriding USING METHOD


class Father:
    def gold(self):     #same method
        print("this is my gold")

class Son(Father):    #inheritance concept in over riding
    def gold(self):     #same method
        print("this is my silver")
        super().gold()   #calling outside the class

s=Son()
s.gold()