



class Newclass:

    def gud(self):
        pass

    @staticmethod
    def sath(name):   #  self no present in static methods
        print(name)

mc=Newclass()
mc.gud()
Newclass.sath("sathya")
# class Myclass:          #It is a class
#
#     def myfunc(self):    #Methods  # Self is a default argument, just to represnt this method belongs to this class
#         pass        #None , it means no implementation i have given
#
#     @staticmethod
#     def display(name):        #static method
#         print(name)
#
#
# mc=Myclass()     #object creation (instance)
# mc.myfunc()
# Myclass.display("oranium")    # calling the static method with class name