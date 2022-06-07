import random
winpercent=int(input("庄家赢的几率(0-100之间)："))
while True:
    print("猜大小的游戏：L或l表示大，S或s表示小，Q或q则结束")
    inputnum=input("=")
    if inputnum == "Q" or inputnum == "q":
        print("结束~")
        break
    num=random.randint(1,100)
    if num>winpercent:
        print("恭喜答对~")
    else:
        print("答错了喔，请再来一次~")
