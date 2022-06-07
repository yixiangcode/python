import random
while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    list=[dice1,dice2,dice3]
    sum = dice1+dice2+dice3
    guess = input("请输入大小（输入Q或q结束程式）：")
    if 11<=sum<=18:
        result = "大"
    elif 3<=sum<=10:
        result = "小"
    print ("结果为%s"%result)
    print(list)
    if guess.lower() == "q":
        print("程式结束~")
        break
    elif guess == result:
        print("恭喜您猜对了！")
    else:
        continue