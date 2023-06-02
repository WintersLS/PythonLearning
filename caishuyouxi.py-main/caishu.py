#10以内随机数，可以根据猜的数提出大小，有三次机会
import random

secret = random.randint(1, 10)
ans = int(input("请输入您所猜想的数字："))
if ans > secret:
    print("大啦！")
    ans = int(input("再猜一次吧！"))
    if ans == secret:
        print("恭喜您猜对啦！")
    elif ans > secret:
        print("还是大。。")
        ans = int(input("再猜一次吧！"))
        if ans == secret:
            print("终于答对了！")
        else:
            print("还是错啦！")
    elif ans < secret:
        print("又小了")
        ans = int(input("再猜一次吧！"))
        if ans == secret:
            print("终于答对了！")
        else:
            print("还是错啦！")

elif ans < secret:
    print("小啦！")
    ans = int(input("再猜一次吧！"))
    if ans == secret:
        print("恭喜您猜对啦！")
    elif ans > secret:
        print("还是大。。")
        ans = int(input("再猜一次吧！"))
        if ans == secret:
            print("终于答对了！")
        else:
            print("还是错啦！")
    elif ans < secret:
        print("又小了")
        ans = int(input("再猜一次吧！"))
        if ans == secret:
            print("终于答对了！")
        else:
            print("还是错啦！")
elif ans == secret:
    print("恭喜您第一次就猜对啦！")
