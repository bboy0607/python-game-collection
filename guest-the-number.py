import random

answer = random.randint(1,101)
count = 0

while True :
    count += 1
    num = int(input('請輸入 1 ~ 100 間的數值: '))
    if num < answer:
        print('再大一點')
        
    elif num > answer:
        print('再小一點')

    else:
        print('恭喜你答對啦!答案是 %d，你猜了 %d 次' %(answer, count))
        break
