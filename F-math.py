def F_math(num):
    if num < 2:
        print(num)
        return
    a=0; b=1; c=0
    for _ in range(num-1):
        c = b
        b += a
        a = c
        # print("a:",a," b:",b)
    print(b)
F_math(1)
# F_math(2)
# F_math(5)
# F_math(50)
# F_math(9999)
# F_math(100000)

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    print(a)
# fib_iterative(1000000)

fib_iterative(10)


