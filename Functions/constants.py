# Goal: contain all functions that generate constant values
# Author: Steven Iacobellis, co-authored by many

from Functions import power_function as pf
from Functions import auxiliary_functions as af
import math

# Initial values
pi = 0
e = 0
ln10 = 0


# Calculate pi using the Chudnovsky algorithm
def get_pi():
    global pi

    if pi == 0:
        series_sum = 0

        # We iterate for 2 iterations, as Chudnosvky converges very
        # quickly
        for i in range(2):
            series_sum += (pf.power_function([-1, i]) * af.factorial(6 * i)
                           * (13591409 + (545140134 * i))) \
                          / (af.factorial(3 * i)
                             * pf.power_function([math.factorial(i), 3])
                             * pf.power_function([640320, 3 * i + 1.5]))

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


def get_ln10():
    global ln10

    if ln10 == 0:
        # if the ln(10) isn't already calculated, then calculate it for
        # the first time and store it for the duration of runtime
        sum = 0
        for i in range(1000):
            sum += (1 / (2 * i + 1)) * pf.power_function(
                [(10 - 1) / (10 + 1), 2 * i + 1])

        ln10 = 2 * sum

    return ln10
