import random


def generaterandom(upper):
    r = random.randint(1, upper)
    return r


def main():
    program = True
    num1 = generaterandom(10)
    num2 = generaterandom(10)
    result = num1 + num2
    while program:
        ans = input("what is" + str(num1) + "x" + str(num2) + "=")
        if ans.isdigit():
            if int(ans) == result:
                print("correct")
                program = False
            else:
                print("incorrect")
        else:
            print("answer must ne positive")
    x = 10
    for x in range(x):
        main()
