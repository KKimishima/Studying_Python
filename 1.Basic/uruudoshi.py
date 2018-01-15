# 条件
# 西暦で4で割り切れる
# 100年で割り切れる年ではない
# 400年で割り切れる年でである

year = int(input("西暦を入力してください:"))

if(year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print(str(year) + "年は閏年です")
else:
    print(str(year) + "年は閏年ではないです!!!")
    
