from sys import exit 
try:
    score = int(input("数字を入力してください"))
#except ValueError:
# こうすると発生した例外を拾ってくれる
except:
    print("不正な数値が入力されました")
    exit()

if score>= 80:
    print("合格")
else :
    print("不合格")

