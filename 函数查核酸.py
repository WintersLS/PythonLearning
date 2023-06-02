
def hesuan(tem):
    if tem > 37.5:
        print(f"您的体温是{tem}摄氏度，体温过高，无法进入。")
    else:
        print(f"您的体温是{tem}摄氏度，体温合格，请进。")

while True:
    a = float(input("请出示您的核算证明并检测体温："))
    hesuan(a)