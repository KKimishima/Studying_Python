# 文字列は配列としても扱える
strS = "春夏秋冬"

for s in strS:
    print(s)

#配列から切り出し
numStr = "12345"
print(numStr[1:4])

# 文字検索
numStr2 = "0123456789"

# 見つからないときは-1を返す
index = numStr2.find("4")
if index != -1:
    print("ヒット:index="+str(index))
else:
    print("ヒットなし")

# 文字列のフォーマットをしていする
str1 = "ほげ"
str2 = "ふー"
flotStr = 10 /2.54


print("一番目の文字は{}で二番目の文字は{}".format(str1,str2))
print("小数点１桁で表示{:.1f}".format(flotStr))
