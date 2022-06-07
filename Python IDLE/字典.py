fruits={"Watermelon":15,"Banana":20,"Pineapple":25,"Orange":12,"Apple":18}
print("五种水果的fruits字典：")
for fruit,price in fruits.items():
    print(fruit,":",price)
print("\n依水果名排序列印：")
for newfruits,newprice in sorted(fruits.items()):
    print(newfruits,":",newprice)
