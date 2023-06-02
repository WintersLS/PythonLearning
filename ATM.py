name = input("请输入您的姓名:")
money = 50000
machine = True
def menu():
    '''
    主菜单函数
    :return:用户的选择
    '''
    print(f"-------主菜单-------\n"
          f"{name}你好，欢迎来到小马银行ATM机请选择您的操作：\n"
          f"查询余额\t[输入1]\n"
          f"存款\t\t[输入2]\n"
          f"取款\t\t[输入3]\n"
          f"退出\t\t[输入4]")
    num = int(input("请输入您的选择："))
    if num == 1:
        yue()
        menu()
    elif num == 2:
        cash = int(input("请输入您的存款金额：（元）"))
        save(cash)
    elif num == 3:
        cash = int(input("请输入您的取款金额：（元）"))
        withdraw(cash)
    elif num == 4:
        global machine
        print("程序退出啦")
        machine = False
    else:
        print("输入有误，请重新输入")
        menu()
def yue():
    '''
    余额显示界面
    :return:
    '''
    print(f"{name}您好！你的账户余额为{money}元")


def save(cash):
    '''
    存款函数
    :param cash: 存款金额
    :return:
    '''
    global money
    money += cash
    print(f"{name}你好，您成功存款{cash}元")
    yue()


def withdraw(cash):
    global money
    if cash <= money:
        money -= cash
        print(f"{name}你好，您成功取款{cash}元")
        yue()
    else:
        print(money)
        cash = int(input(f"不好意思，您的账户余额不足{cash}元，请重新输入金额:"))

        withdraw(cash)

while machine:
    menu()
