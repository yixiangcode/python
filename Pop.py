import random
letter = ["A","B","C","D","E"]
while True:
    random.shuffle(letter)
    letter.pop()
    letter.sort()
    print(letter)
    if not letter:
        print("串列无元素，结束！")
        break