print("【创建账号】")
accounts=["账号","密码"]
account=input("请输入您的新账号：")
password=input("请输入您的新密码：")
print("Hi"+" "+account)
accounts.insert(0,account)
accounts.insert(1,password)
ac=input("请输入您的账号：")
if ac in accounts[0]:
    pwd=input("请输入您的密码 :")
else:
    print("【您输入的是无效账号 ！】")
if pwd in accounts[1]:
    print("【欢迎回到新世界~】")
else:
    print("【密码错误 ！】")
