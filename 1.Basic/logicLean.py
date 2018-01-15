# ifの分岐の練習
age = int(input("年齢を入力してください:"))

# if分岐練習
if age < 3:
    print("無料です")
elif age < 13:
    print("200円です")
elif age < 65:
    print("400円です")

# 論理演算子
if(age == 3) or (age == 5) or (age == 7):
    print("七五三さんです")

