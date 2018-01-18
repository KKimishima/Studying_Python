# 可変引き数
# 可変引き数ではタプルになる
def func1(arg1,*arg2):
    print(arg1,arg2)

func1(1,2,3,4)
func1("こんにちは",12,0.1)

# 平均値を出す関数
def func2(*arg3):
    sum = 0
    for a3 in arg3:
        sum += a3
    return int(sum / len(arg3))

print(func2(1,100,12,22,44))

# タプルではなく可変辞書型で受け取る
def func3(**dic1):
    print(dic1)

func3(name="ほげ",age = 99)

