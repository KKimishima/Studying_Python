lst1 = ["1","2","3"]
lst2 = ["4","5"]

# リスト結合
print(lst1 + lst2)
# 要素の追加
lst3 = ["A"] * 4
print(lst3)

# スライス
lst4 = lst1 +lst2
print(lst4[2:4])

str1 = "一,二,三,四,五"
lst5 = str1.split(",")
print(lst5)

# 探索
if "百" in lst5:
    print("ヒット")
else:
    print("ハズレ")
# インデックスを調べる
str2 = "五"
try:
    index2 = lst5.index(str2)
    print("インデックス={}です".format(index2))
except :
    print("インデックスなし")

lst5[4] = 5
lst5.append(6.0)
lst5.append([7.1,7.2,7.3])
lst5.remove("一")
del lst5[0]

print(lst5)
