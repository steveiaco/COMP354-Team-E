import numpy as np
import Power_Function as pf


def standard_deviation(input):
    count = len(input)
    if count > 0:
        # if the length of argument list is 1, return 0 directly
        if count == 1:
            return 0;
        # compute mean
        args = np.array(input)
        mean, s = total_count(args)/count, 0
        # get a new list after each item minus mean, and square
        args_new = args - mean
        for i in range(count):
            args_new[i] = pf.power_integer(args_new[i], 2)

        return pf.power_fractional(total_count(args_new) / count, 0.5)
    else:
        raise TypeError('Invalid Argument !')


def total_count(args):
    s = 0
    for i in range(len(args)):
        s = s + args[i]
    return s


arr = [1,2,3,4,5,6,7,8,9,10]
print("Computed by numpy:           " + str(np.std(arr)))
print("Computed by original python: " + str(standard_deviation(arr)))

    

