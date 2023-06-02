import random
account = 10000
for i in range(1,21):
    score = random.randint(0,10)
    if account <= 0:
        print("账户余额不足，停止发放工资")
        break
    elif score < 5:
        print(f"您是第{i}位员工，您的绩效分是{score}分，太低啦，不发工资，下一位！")
        continue
    else:
        print(f"您是第{i}位员工，您的绩效分是{score},请您收好1000元！")
        account -= 1000
        print(f"公司账户余额为{account}")