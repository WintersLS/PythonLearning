a = 1
while a <= 9:
    b = 1
    while b <= a:
        print(f"{b}x{a}={a*b}",end="\t")
        b += 1
    a += 1
    print()