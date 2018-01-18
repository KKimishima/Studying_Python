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
