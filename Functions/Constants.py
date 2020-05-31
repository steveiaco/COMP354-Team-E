from Power_Function import power_function
import math

# Initial values
pi = 0
e = 0

# Calculate pi using the Chudnovsky algorithm
def get_pi():
    global pi

    if pi == 0:
        series_sum = 0

        # We iterate for 20 iterations, as Chudnosvky converges very quickly
        for i in range(20):
            series_sum += (power_function([-1, i]) * math.factorial(6 * i) * (13591409 + (545140134 * i)) ) / (math.factorial(3 * i) * power_function([math.factorial(i),3]) * power_function([640320, 3*i + 1.5]))

        pi = 1 / (12 * series_sum)

    return pi

def get_e():
    global e

    if e == 0:
        series_sum = 0

        for i in range(1000):
            series_sum += (1 / math.factorial(i))

        e = series_sum

    return e

def main():

    print(get_e())
    print(get_e())


if __name__ == "__main__":
    main()