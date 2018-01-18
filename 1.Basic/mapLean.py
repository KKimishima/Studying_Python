from random import randint
def to_cm(m1):
    return m1 * 2.54


lst1 = [randint(0,10) for l1 in range(0,10)]
# print(lst1)
# マップObjectを私用した場合
# map(処理を行う関数,対象のリスト)
for m1 in map(to_cm,lst1):
    print(m1)

# mapを利用しない場合
for m2 in lst1:
    print(to_cm(m2))

# map結果をリストを変換する
lst2 = list(map(to_cm,lst1))
print(lst2)

#ラムダ式で使う
lst3 = list(map(lambda n:n*2.54,lst1))
print(lst3)
