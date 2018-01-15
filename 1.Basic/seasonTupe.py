# タプルを

month = int(input("月の値を入力してください"))

if month in (12,1,2):
    print("冬の季節です")
elif month in (3,4,5):
    print("春の季節です")
elif month in (6,7,8):
    print("夏の季節です")
elif month in (9,10,11):
    print("冬の季節です")
else:
    print("1~12の値を入力してください")
