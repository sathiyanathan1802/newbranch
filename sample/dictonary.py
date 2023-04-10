

#         key   : values
mydic={"sathya":"agila","priya":"karu","naryanan":"chitra"}
print(mydic)
print(mydic['sathya'])
mydic["sathya"]="ammu"
print(mydic)

for i in(mydic):  # it will print only the values
    print(mydic[i])

for i in mydic.values():  # it will print only the values
    print(i)
for x,y in mydic.items():
     print(x,y)

print("sathya" in mydic)  #5. check key is exist in dictionary or not
print("priya" in mydic)


#6. Adding items in a dictionary

mydic["anand"]="chan"
print(mydic)

# 7. Removing item from dictionary

mydic.pop("sathya")
print(mydic)


for i in mydic.items():
    print(i)

for x,y in mydic.items():
    print(x,y)
print(len(mydic))

mydic.clear()     #clear the set values
print(mydic)

del mydic
print(mydic)



