myset={"sathya","karu","ammu","papa"}
print(myset)
for i in (myset):
    print(i)
print("papa" in myset)
print("nathan " in myset)

myset.add('nathan')
print(myset)
myset.update(['chitra','narayanan'])
print(myset)

print(len(myset))

myset.remove("sathya")
print(myset)
myset.discard("chitra")
print(myset)

# myset.clear()
# print(myset)  # it will remove all the items in a set
# del myset
# print(myset)

myset1={"ammmmmuuuu","anand"}
myset2={"sathya",'mango'}
myset3=myset1.union(myset2)
print(myset3)

myset1.update(myset2)
