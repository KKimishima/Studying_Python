import os,sys,random

def main():
    arg_check(sys.argv)
    path_check(sys.argv[1])
    random_str = ["大吉","中吉","凶"]
    write_file(random_str,sys.argv[1])
    print("書き込み成功")
def arg_check(ag):
    if len(ag) != 2:
        print("ファイル名を一つ指定してください")
        sys.exit(1)

def path_check(path_str):
    if os.path.exists(path_str):
        if input("上書きしますますか?(Y/N)") != "Y":
            sys.exit()

def write_file(random_str,path):
    try:
        with open(path,"w",encoding="utf_8") as fw:
            fw.write(random_str[random.randint(0,(len(random_str)-1))]+"\n")
    except:
        print("ファイル書き込み失敗")
        sys.exit()
if __name__ == '__main__':
    main()
