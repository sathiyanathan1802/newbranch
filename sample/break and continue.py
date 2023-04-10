




for a in range(1,10,1):
    if a==8:
        break
    print(a)
# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7

for a in range(1,10,1):
    if a==5 or a==3 or a== 7:  #5 is skip
        continue
    print(a)
# output
1
2
4
6
8
9


