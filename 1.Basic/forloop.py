# リストから取り出して繰り返す
week = ["月","火","水","木","金","土","日"]

for day in week:#:list`>:
    print(day)

for count in range(10):
    print(count)

for count in range(3,33,3):
    print(count)

end =  int(input("総和を求める数字を入力:"))

sum = 0
for num in range(0,end + 1):
    sum += num
print("総和:" + str(sum))


end =  int(input("whileで総和を求める数字を入力:"))
sum2 = 0
counter = 0
while counter <= end:
    sum2 += counter
    counter += 1

print("総和:" + str(sum2))

wordTaplu = ("旅行","ラジオ","海","山")

for index,word in enumerate(wordTaplu):
    if word == "海":
        print(str(index+1) + "番目でヒット")
        break
    print(word)

list1 = [1,2,3,4,5]
list2 = [11,22,33,44,55]

２つの要素をタプルで返す
for (l1,l2) in zip(list1,list2):
    print(str(l1) + str(l2) )

