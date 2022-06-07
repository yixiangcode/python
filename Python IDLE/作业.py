import random
money=300
bet=100
min,max=1,100
winpercent=int(input("请庄家输入赢钱比(0-100)："))
while True:
    print("欢迎光临：目前筹码金额是%d美金"%money)
    print("每次赌注：%d美金"%bet)
    print("猜大小游戏：L或l表示大，S或s表示小，Q或q则程式结束")
    customernum=input("= ")
    if customernum=="Q" or customernum=="q":
        break
    num=random.randint(min,max)
    if num > winpercent:
        print("恭喜！答对了\n")
        money+=bet
    else:
        print("答错了，请在试一次\n")
        money-=bet
    if money <= 0:
        break
print("欢迎下次再来")
