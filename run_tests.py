import math
import pandas
import numpy
import random
import statistics

from log import ln
from power_function import power_function
from mean_absolute_deviation import mean_absolute_deviation
from standard_deviation import standard_deviation
from sine import sine
from cosh import cosh
from pi import pi_function

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

PRECISION = 0.000000001


# pi test
def pi_test():
    print(f'{bcolors.HEADER}pi test starting...')
    for i in range(-10, 10):
        calc = pi_function([i])
        result = (math.pi)**(i)
        error = calc - result

        error = abs(error)

        if error > PRECISION:
            print(f'{bcolors.FAIL}Outside of acceptable range. \n \t pi({i}) = {calc} \n \t actual = {result} \n \t error of: {error} \n')
            return False

    return True

# ln test
def ln_test():
    print(f'{bcolors.HEADER}ln test starting...')
    for i in range(1, 10000):
        calc = ln([i])
        result = math.log(i)
        error = calc - result

        error = abs(error)
        if error > PRECISION:
            print(f'{bcolors.FAIL}Outside of acceptable range. \n \t ln({i}) = {calc} \n \t actual = {result} \n \t error of: {error} \n')
            return False

    return True

# sine test
def sine_test():
    print(f'{bcolors.HEADER}sine test starting...')
    for i in range(-10, 10):
        calc = sine([i])
        result = math.sin(i)
        error = round(calc, 10) - round(result, 10)

        error = abs(error)

        if error > PRECISION:
                print(f'{bcolors.FAIL}Outside of acceptable range. \n \t sine({i}) = {calc}. \n \t actual = {result}. \n \t error of: {error}. \n')
                return False
    return True

# cosh test 
def cosh_test():
    print(f'{bcolors.HEADER}cosh test starting...')
    for i in range(-10, 10):
        calc = round(cosh([i]), 10)
        result = round(math.cosh(i), 10)
        error = calc - result

        error = abs(error)

        if error > PRECISION:
            print(f'{bcolors.FAIL}Outside of acceptable range. \n \t cosh({i}) = {calc}. \n \t actual = {result}. \n \t error of: {error}. \n')
            return False

    return True


# power function test for integer cases
def pf_test_integer():
    print(f'{bcolors.HEADER}pf_integer test starting...')
    for i in range(-10, 10):
        for j in range(-10, 10):
            if not (i == 0 and j < 0):
                calc = round(power_function([i, j]), 10)
                result = round(math.pow(i, j), 10)
                error = calc - result

                error = abs(error)

                if error > PRECISION:
                    print(f'{bcolors.FAIL}Outside of acceptable range. \n \t power_function({i},{j}) = {calc}. \n \t actual: {result}. \n \t error of: {error} \n')
                    return False
    return True

# power function test for decimal cases
def pf_test_decimal():
    print(f'{bcolors.HEADER}pf_decimal test starting...')
    for i in range(0, 10):
        for j in range(-10, 10):
            if not (i == 0 and j < 0):
                i += 0.5
                j += 0.5

                calc = round(power_function([i, j]), 3)
                result = round(math.pow(i, j), 3)
                error = calc - result

                error = abs(error)

                if error > PRECISION:
                    print(f'{bcolors.FAIL}Outside of acceptable range. \n \t power_function({i},{j}):{calc}. \n \t actual: {result}. \n \t error of: {error} \n')
                    return False

    return True

# mean absolute deviation test for integer cases
def mad_test_integer():
    print(f'{bcolors.HEADER}mad_integer test starting...')
    for i in range(0, 10): 
        list = []
        for j in range(0, 10):
            x = random.randint(0, 100)
            list.append(x)
        calc = round(mean_absolute_deviation(list), 10)
        result = round(pandas.Series(list).mad(), 10)
        error = calc - result

        error = abs(error)

        if error > PRECISION:
            print(f'{bcolors.FAIL}Outside of acceptable range. \n \t list: {list} \n \t mean_absolute_deviation:{calc}. \n \t actual: {result}. \n \t error of: {error} \n')
            return False
    return True

# mean absolute deviation test for decimal cases
def mad_test_decimal():
    print(f'{bcolors.HEADER}mad_decimal test starting...')
    for i in range(0, 10): 
        list = []
        for j in range(0, 10):
            x = random.random()
            list.append(x)
        calc = round(mean_absolute_deviation(list), 10)
        result = round(pandas.Series(list).mad(), 10)
        error = calc - result

        error = abs(error)

        if error > PRECISION:
            print(f'{bcolors.FAIL}Outside of acceptable range. \n \t list: {list} \n \t mean_absolute_deviation:{calc}. \n \t actual: {result}. \n \t error of: {error} \n')
            return False
    return True

# standard deviation test for decimal cases
def std_test_integer():
    print(f'{bcolors.HEADER}std_integer test starting...')
    for i in range(0, 10): 
        list = []
        for j in range(0, 10):
            x = random.randint(0, 100)
            list.append(x)
        calc = round(standard_deviation(list), 10)
        result = round(statistics.pstdev(list), 10)
        error = calc - result

        error = abs(error)

        if error > PRECISION:
            print(f'{bcolors.FAIL}Outside of acceptable range. \n \t list: {list} \n \t standard_deviation:{calc}. \n \t actual: {result}. \n \t error of: {error} \n')
            return False
    return True

# standard deviation test for integer cases
def std_test_decimal():
    print(f'{bcolors.HEADER}std_decimal test starting...')
    for i in range(0, 10): 
        list = []
        for j in range(0, 10):
            x = random.random()
            list.append(x)
        calc = round(standard_deviation(list), 10)
        result = round(statistics.pstdev(list), 10)
        error = calc - result

        error = abs(error)

        if error > PRECISION:
            print(f'{bcolors.FAIL}Outside of acceptable range. \n \t list: {list} \n \t standard_deviation:{calc}. \n \t actual: {result}. \n \t error of: {error} \n')
            return False

    return True

# Define all tests and their names
test_map = {
    'ln': ln_test,
    'sine': sine_test,
    'cosh': cosh_test,
    'power_function_integer': pf_test_integer,
    'power_function_decimal': pf_test_decimal,
    'mean_absolute_deviation_integer': mad_test_integer,
    'mean_absolute_deviation_decimal': mad_test_decimal,
    'standard_deviation_integer': std_test_integer,
    'standard_deviation_decimal': std_test_decimal,
    'pi' : pi_test
}


def main():

    for name, function in test_map.items():
        if function():
            print(f'{bcolors.OKGREEN}{name} test passed \n')
        else:
            print(f'{bcolors.FAIL}{name} test failure \n')

if __name__ == "__main__":
    main()
