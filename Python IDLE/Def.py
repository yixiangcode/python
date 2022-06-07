def msg(people):
    str1="同学您好，"
    str2="恭喜您被录取了！"
    str3="XX大学上"
    for name in people:
        content=name + str1 + "\n" + str2 + "\n" + str3
        print (content,"\n")
students = ["张","毕","陈"]
msg(students)
