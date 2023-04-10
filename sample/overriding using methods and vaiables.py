


# OVER RIDING USING VARIABLES



class Moon:
    i='10' #global varibles


class Sun(Moon):
    i='15'  # local variables   #same name of variables

    def sath(self):
        print(self.i)
        print(super().i)

s=Sun()
s.sath()

