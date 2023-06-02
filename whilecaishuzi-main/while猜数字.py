import random

secret = random.randint(0,100)
ans = int(input("请输入您所猜数字（0-100）:"))
times = 0
stop = False
while stop == False:
    times += 1
    if ans > secret:
        ans = int(input("大啦！请重试！"))
    elif ans < secret:
        ans = int(input("小啦！请重试！"))
    else:
        print("恭喜您猜对啦，您所猜次数为%s"% times)
        stop = True
