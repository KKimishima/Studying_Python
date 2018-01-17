from random  import randint
# リスト要素の生成
lst1 = []
for l1 in range(1,10,2):
    lst1.append(l1)
print(lst1)

# 内部表記でリスト生成
# 入れる時の処理 for 変数 in 繰り返し
lst2 =[num for num in range(1,11)]
print(lst2)

# リストからリストを生成させる
lst3 =[1,2,3,4,5]
num = 6
lst4 = [lst3 * num for lst3 in lst3]
print(lst4)

# 文字を変動箇所だけ入れてを入れって
lst5 = ["1","2","3","4","5"]
lst6 = [l6 + "0" for l6 in lst5]
print(lst6)

lst7 = [l7 for l7 in range(1,11)]
print(lst7)
# ワンラインでifまで実行する
lst8 = [l8 for l8 in lst7 if(l8 % 3) == 0]
print(lst8)

# 文字検索
lst9 = [str(randint(100,999)) for l8 in range(1,20)]
print(lst9)

lst10 = [l9[2:] for l9 in lst9]
print(lst10)

lst11 = [l9[2:] for l9 in lst9 if l9.startswith("2")]
print(lst11)

lst12 = [("1","1"),("3","1"),("5","2")]
print(lst12)

lst13 =[n[0] for n in lst12 if n[1] == "2"]
print(lst13)

dic1 = {d9:1 for d9 in lst9}
print(dic1)

lst14 = [l14 for l14 in range(0,10)]
print(lst14)

lst15 = [l15 for l15 in range(9,-1,-1)]
print(lst15)

dic2 = {l14:l15 for (l14,l15) in zip(lst14,lst15)}
print(dic2)

dic3 = {l15:l14 for (l14,l15) in zip(lst14,lst15)}
print(dic3)

lst16 = [int(l16) for l16 in lst9]
print(lst16)
set1 ={s1 for s1 in lst16 if s1 > 500}
print(set1)
