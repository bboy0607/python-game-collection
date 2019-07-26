import random
  
answer = random.randint(1,101)
num_min = 1
num_max = 100
count = 0

while True :
    count += 1
    print('請輸入 %d ~ %d 間的數值' %(num_min, num_max))
    num = int(input('輸入: ' ))
    if num < answer:
        print('再大一點')
        num_min = num
    elif num > answer:
        print('再小一點')
        num_max = num
    else:
        print('恭喜你答對啦!答案是 %d，你總共猜了 %d 次。' %(answer, count))
        break
