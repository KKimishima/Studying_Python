#import calendar
# モジュールを省略してかける
from calendar import TextCalendar
from math import sqrt
from random import randrange
# カレンダー表示する引き数はカレンダの頭位置
cal = TextCalendar(6)
# 文字列にする
cal_str = cal.formatmonth(2018,1)
print(cal_str)

num = sqrt(16)
print("平方根" + str(num))

list = ["大吉","中吉","凶"]

print("ランダムクジ:" + list[randrange(len(list))])

