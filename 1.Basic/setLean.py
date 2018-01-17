# 重複を許さない集合
set1 = {"1","1","2","2","3"}
print(set1)

# リストから集合に変換
# 重複が排除される
lst1 = ["1","1","2","2","3"]
set2 = set(lst1)
print(set2)

# 追加,削除
set3 = {"1","1","2","2","3"}
set3.add("4")
print(set3)
set3.remove("4")
print(set3)
