heigt = float(input("身長(cm)を入力してください"))
#heigt = 180
bmi   = 22

# **で累乗の意味
std_wight = bmi * (heigt / 100) **2
# endで最終文字指定
print("身長:" +str(heigt) +"cm ->",  end="")
print("標準体重:" + str(std_wight) + "kg")
