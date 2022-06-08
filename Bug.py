def division (x, y):
    try:
        return int (x) / int (y)
    except Exception :
        print("资料输入错误")

while True:
    a = input("请输入一个被除数：")
    b = input("请输入一个除数：")
    print( "答案为 " , division(a, b) , "\n")
