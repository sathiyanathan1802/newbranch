


mylist=["sathya","agila","kani","siva"]
print (mylist [::-1])
print(list(mylist))
print(mylist[1])
#.Change the item value because it is mutable
mylist[1]="ammu"
print(mylist)
# Reading the items using loop
for i in mylist:
    print(i)

#check if the item is existing in the list or not ..
if "ammu" in mylist:
    print('present in list')
else:
    print("absent in list")
# #check if the item is existing in the list or not ..
print(len(mylist))
# Adding the items into the list
mylist.append("muuuu")
print(mylist)
mylist.insert(1,"nathan")
print(mylist)
del mylist[3]
print(mylist)
mylist1=['priya']
print(mylist+mylist1)
# add text
mylist1=['sathya','agilamuuu']
mylist.extend(mylist1)
print(mylist)
for i in (mylist):
    print(i)
