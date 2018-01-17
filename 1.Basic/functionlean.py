def hello(t,initStr= "デフォルト値"):
    return t + "hello" + initStr

# キーワード引き数でもデキる
#message = hello(t ="テスト" )
message = hello("テスト","test")

print(message)

