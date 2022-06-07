import MyMath
while True:
    choice = input("请输入1/2/3/4（加/减/乘/除，输入Q或q可结束程式)：")
    
    if choice.lower() == "q":
        print("运算结束")
        break
    if choice == "1":
        num1 = int(input("请输入数字："))
        num2 = int(input("请输入另一个数字："))
        MyMath.add(num1, num2)
        continue
    elif choice == "2":
        num1 = int(input("请输入数字："))
        num2 = int(input("请输入另一个数字："))
        MyMath.sub(num1, num2)
        continue
    elif choice == "3":
        num1 = int(input("请输入数字："))
        num2 = int(input("请输入另一个数字："))
        MyMath.mul(num1, num2)
        continue
    elif choice == "4":
        num1 = int(input("请输入数字："))
        num2 = int(input("请输入另一个数字："))
        MyMath.div(num1, num2)
        continue
    else:
        print("没有 %s 的选项喔~"%choice)
        continue