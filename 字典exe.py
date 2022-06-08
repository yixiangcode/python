print("【英汉字典】\n请输入所要翻译之星期的英文\n若想结束此次翻译可按x哟~\n")
星期={"Monday".lower():"星期一",
      "Tuesday".lower():"星期二",
      "Wednesday".lower():"星期三",
      "Thursday".lower():"星期四",
      "Friday".lower():"星期五",
      "Saturday".lower():"星期六",
      "Sunday".lower():"星期日"}
while True:
    星期输入=input("请输入要查询之星期的英文：")
    if 星期输入.lower()=="x":
            print("翻译结束,谢谢老师~")
            break
    if 星期输入 in 星期:
        print("%s的中文为%s\n"%(星期输入,星期[星期输入]))
    else:
            print("输入错误！")
            print("请输入正确的英文星期哟~\n")

print("【汉英字典】\n请输入所要翻译之中文月份（例如：一月）\n若想结束此次翻译请按x哟\n")
月份={"一月":"January",
    "二月":"February",
    "三月":"March",
    "四月":"April",
    "五月":"May",
    "六月":"June",
    "七月":"July",
    "八月":"August",
    "九月":"September",
    "十月":"October",
    "十一月":"November",
    "十二月":"December"}

while True:
        月份输入=input("请输入要翻译的中文月份：")
        if 月份输入.lower()=="x":
            print("翻译结束,谢谢老师~")
            break
        if 月份输入 in 月份:
            print("%s的英文为%s\n"%(月份输入,月份[月份输入]))
        else:
            print("输入错误！")
            print("请输入正确的中文月份（例如：一月）哟~\n")

fruits={"Watermelon":15,"Banana":20,"Pineapple":25,"Orange":12,"Apple":18}
print("五种水果的fruits字典：")
for fruit,price in fruits.items():
    print(fruit,":",price)
print("\n依水果名排序列印：")
for newfruits,newprice in sorted(fruits.items()):
    print(newfruits,":",newprice)