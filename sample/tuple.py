


mytuple=("ammu","agila","priya","karu")
print(mytuple)
#accessing the elements

print(mytuple[2])
print(mytuple[-1])

# # Tuple---> list ---> modify ---> convert into tuple again

mylist=list(mytuple)
mylist[1]='danger'
print(mylist)
mytuple=tuple(mylist)
print(mytuple)
# Reading items using for loop

for i in(mytuple):
    print(i)

#Check if the item is present in tuple

print ("sathya" in mytuple)

#to know the Number of items in a tuple
print(len (mytuple))


