accounts=[]
account=input("请输入新账号=")
accounts.append(account)
print("[%s]"%account)
print("系统确认中...\n此名字尚未被使用，账号注册成功")
print("请为此账号设置一个密码")
n=1
comform=1
comform2=1
while comform==1:

    while n<=3 and comform2==1:
        n=1
        password=input("请输入新密码=")
        while len(password)<10:
            print("该密码安全性过低，请设置一个至少10个由数字组成的密码")
            password=input("请输入新密码")
        passwordChecking=input("请再次输入新密码=")
        if passwordChecking==password:
            comform2=0
        while n<=3 and passwordChecking!=password:
            n+=1
            print("密码错误，请再次输入")
            passwordChecking=input("请再次输入新密码=")
        if passwordChecking!=password:
            print("由于确认密码多次与新密码不一样，请重新输入新密码")
            n=1

    if passwordChecking==password:
        comform=0
print("密码创立成功！")
accountLogin=input("请输入账号")
while accountLogin not in accounts:
    print("账号不存在")
    accountLogin=input("请输入账号")
passwordLogin=input("请输入账号密码")
while passwordLogin != password:
    passwordLogin=input("密码错误，请再次输入密码")
print("welcome")



