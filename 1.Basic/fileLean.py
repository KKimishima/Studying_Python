from random import randint
# ファイル読み込み

fw = open("./test.txt","w",encoding="utf_8")
fw.write("テスト1\n")
fw.write("テスト2\n")
fw.write("テスト3")
fw.close()

fr = open("./test.txt","r",encoding="utf_8")
print(fr.read())
fr.close()

fr2 = open("./test.txt","r",encoding="utf_8")
print(fr2.readlines())
fr2.close()

fr3 = open("./test.txt","r",encoding="utf_8")
li2 = fr3.readlines()
for i,l2 in enumerate(li2):
    print("{:4}:{}".format(i + 1,l2.strip()))
fr3.close()
# ランダム生成

lsi1 = [ls1 for ls1 in range(0,10)] 
lsi2 = ["ランダム" +str(ls2) for ls2 in range(0,10)]
print(lsi2)
dic1 = {l1:l2 for (l1,l2) in zip(lsi1,lsi2)}
print(dic1)
fw2 = open("./test.txt","w",encoding="utf_8")
for wr in dic1:
    fw2.write((dic1[randint(0,9)]) +"\n")
fw2.close() 

with open("./test.txt","r",encoding="utf_8") as fr4:
    for f in fr4:
        print(f.rstrip("\n"))

print("集計開始")
rs = {}
with open("./test.txt","r",encoding="utf_8") as fr5:
    for fr in fr5:
        str1 = fr.rstrip("\n")
        if str1 in rs:
            rs[str1] +=1
        else:
            rs[str1] = 1
print("集計")
for sort1 in sorted(rs.items(),key=lambda c:c[1],reverse=True):
    print(sort1[0]+ ":" +str(sort1[1]))
