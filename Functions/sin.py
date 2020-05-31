import math


def factorial(number):
    # factorial by recursion
    if number < 0:
        print("factorial is undefined for negative numbers!")
        return None
    if number == 1 or number == 0:
        return 1
    else:
        return number*factorial(number-1)


def taylor_sin(num):
    res = 0
    twopi = 2 * math.pi

    # program will crush if num too big
    # so minus 2pi continuously, since sin(x+2pi)=sin(x)
    # this step is losing precision and very slow when num is big, like x=10^9
    while num > twopi:
        num -= twopi
    while num < -twopi:
        num += twopi
    # using for loop to create summation i=0 to i=39
    for i in range(40):
        res += ((-1)**i)*(num**(2*i+1))/(factorial(2*i+1))
    return res

    # ** should be replaced by our own implementation


x = -10

print(math.sin(x))
print(taylor_sin(x))

