print("函数练习")
print("第一题：")
def 正负(number):
    if(number<0):
        number*=-1
    print("绝对值输出：",number,"\n")
输入=int(input("请输入数字："))
正负(输入)

print("第二题和第三题：")
def 计算机():
    num1=int(input("请输入一个数字："))
    num2=int(input("请输入另一个数字："))
    符号=input("请输入运算符号：")
    if(符号=="+"):
        print(num1+num2)
    if(符号=="-"):
        print(num1-num2)
    if(符号=="*"):
        print(num1*num2)
    if(符号=="/"):
        print(num1/num2)
    重复()
def 重复():
    if(input("若想继续请输入Y或y：").lower()=="y"):
        计算机()
    else:
        print("运算结束\n")
计算机()

print("第四题：")
def pizza(pizzasize,pizzatype,*toppings):
    print("这个"+pizzasize+"的"+pizzatype+"披萨配料如下：")
    for topping in toppings:
        print("----",topping)
pizza("9寸","起司","番茄","洋葱","胡椒","蘑菇","香肠")

