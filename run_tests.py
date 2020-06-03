import math

from Logarithm import ln
from power_function import power_function

PRECISION = 0.00000001

# ln test
def ln_test():
    for i in range(100000, 100):
        calc = ln([i])
        result = math.log(i)
        error = calc - result
        if error > PRECISION:
            print(f'Outside of acceptable range: ln({i}:{calc}, actual: {result}')
            return False
    return True

# power function test for integer cases
def pf_test_integer():
    for i in range(-10, 10):
        for j in range(-10, 10):
            if not (i == 0 and j < 0):
                calc = power_function([i, j])
                result = math.pow(i, j)
                error = calc - result
                if error > PRECISION:
                    print(f'Outside of acceptable range: power_function({i},{j}):{calc}, actual: {result}')
                    return False
    return True

# power function test for decimal cases
def pf_test_decimal():
    for i in range(0, 10):
        for j in range(-10, 10):
            if not (i == 0 and j < 0):
                i += 0.5
                j += 0.5

                calc = power_function([i, j])
                result = math.pow(i, j)
                error = calc - result
                if error > PRECISION:
                    print(f'Outside of acceptable range: power_function:{calc}, actual: {result}')
                    return False
    return True

# Define all tests and their names
test_map = {
    'ln': ln_test,
    'power_function_integer': pf_test_integer,
    'power_function_decimal': pf_test_decimal
}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():

    for name, function in test_map.items():
        if function():
            print(f'{bcolors.OKGREEN}{name} test passed')
        else:
            print(f'{bcolors.FAIL}{name} test failure')

if __name__ == "__main__":
    main()