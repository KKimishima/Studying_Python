# 小さい方を返す
lm1 = lambda num1,num2 :num2 if num1 > num2 else num1
print(lm1(1,2))

# キーワードデフォルト値を使用する
lm2 = lambda l1,l2= 100 : l1 * l2
print(lm2(l1 = 1))

# 可変引き数を使用する
lm3 = lambda *l3 : sum(l3) /len(l3)
print(lm3(10,1,2,4,5,2,1))
