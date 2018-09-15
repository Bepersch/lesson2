def task1():
    try:
        a = int(input("Number: "))
        n = str(input("Convert to b or kb: "))
    except ValueError:
        print("NotLikeThis")
    else:
        if n == "b":
            print(a, "kb =", a * 1024, "b")
        elif n == "kb":
            print(a, "b =", a / 1024, "kb")


def task2():
    try:
        a = int(input("Number: "))
    except ValueError:
        print("NotLikeThis")
    else:
        s = 0
        c = 1
        for i in str(a):
            s += int(i)
            c *= int(i)
        print("s =", s, "| c =", c)


def task3():
    try:
        a = int(input("Begin: "))
        b = int(input("End: "))
        c = int(input("Step: "))
    except ValueError:
        print("NotLikeThis")
    else:
        while a <= b:
            print("x: ", a, "| y: ", -1.24 * a ** 2 + a)
            a += c


def task4():
    try:
        a = int(input("Number: "))
    except ValueError:
        print("NotLikeThis")
    else:
        b = True
        i = 1
        for j in str(a):
            if j != str(a)[-i]:
                b = False
            i += 1
        print(b)


def task5():
    try:
        n = int(input("Count: "))
    except ValueError:
        print("NotLikeThis")
    else:
        s = 0
        j = 0
        while n > 0:
            try:
                num = int(input("Number: "))
            except ValueError:
                print("NotLikeThis")
            else:
                if num > 0:
                    s += num
                    j += 1
                n -= 1
        try:
            print("s: ", s / j)
        except ZeroDivisionError:
            print("Zero >0 numbers")

