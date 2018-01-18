from random import randint

lst1 = [randint(0,10) for l1 in range(0,10)]
print(lst1)

lst2 = [l2 for l2 in lst1 if l2 > 5]
print(lst1)

lst3 = [str(l3) for l3 in lst1]
print(lst3)

lst4 = sorted(lst3)
print(lst4)

lst5 = sorted(lst1)
print(lst5)

#lst6 = sorted(lst2,key=str.upper())
#print(lst6)

dic1 = {l1:l2 for (l1,l2) in zip(lst1,lst3)}
print(dic1)

for d in sorted(dic1.items(),key=lambda n:n[0]):
    print(dic1[0],dic1[1])


