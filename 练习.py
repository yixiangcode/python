import random
answer = str(random.randint(1, 50))
time = 0
while True:
    time += 1
    number = input("请猜一个1-50的数字（输入Q或q可结束程式）：")
    if number.lower() == "q":
        print("程式结束~")
        break
    elif number == answer:
        print("恭喜答对了！！\n您总共试了 %d 次才猜对哦~\n"%time)
        time = 0
        answer = str(random.randint(1, 50))
    elif number < answer:
        print("要再猜大一点哟\n第 %d 次尝试失败\n"%time)
    elif number > answer:
        print("要再猜小一点哟\n第 %d 次尝试失败\n"%time)
