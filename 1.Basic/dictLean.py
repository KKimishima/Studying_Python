dict1 = {1:"a",2:"b",3:"c",4:"d",5:"e"}
print(len(dict1))
print(dict1[1])

# キーを追加する
dict1[6] = "f"
print(dict1[6])
# キーの削除
del dict1[6]
print(dict1)

try:
    print("正常な値" + dict1[3])
    print(dict1[100])
except:
    print("辞書に存在しない値です")

# 事前に要素を調べておくパターン
dict2 = {1:"a",2:"b",3:"c",4:"d",5:"e"}

key = 5
if key in dict2:
    del dict2[key]
    print(dict2)
else:
    print("ヒットなし")

# すべてのキーを取得
print(dict2.keys())
# すべての値を取得
print(dict2.values())
# リストに変換
lst1 = list(dict2.values())
print(lst1)

# イテレーション
for num,strn in dict2.items():
    print("キー{}とアイテム{}のセットです".format(num,strn))

# 集計
lst2 = ["1","3","3","6","7","1","8","8"]
# 空の辞書作製
result = {}

# 収納
for l in lst2:
    if l in result:
        result[l] += 1
    else:
        result[l] = 1
# 結果
for r1,r2 in result.items():
    print("キー{}は{}個重複していました".format(r1,r2))


