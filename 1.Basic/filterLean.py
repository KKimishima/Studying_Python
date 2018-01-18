from random import randint

lst1 = [randint(0,10) for l1 in range(0,10)]
print(lst1)

def func1(arg1):
    return arg1 > 5

lst2 = []

for lst1 in filter(func1,lst1):
    lst2.append(lst1 * 2)
print(lst2)

lst3 = []
for l3 in filter(lambda lst1:lst1 > 5,lst2):
    lst3.append(lst1 * 2)
print(lst3)


lst4 = [randint(0,10) for l1 in range(0,10)]
print(lst4)
lst5 = [l1  for l1 in lst1 if l1 > 5]
print(lst4)
#lst5 =[str(l5) for l5 in lst1]
#lst5 =[]
#for l5 in lst1:
#    print(str(l5))
#iprint(lst5)
#ilst5 = sorted(str(lst1))
#print(lst5)
