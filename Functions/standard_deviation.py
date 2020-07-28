#Goal: Calculate the standard deviation of a given list
# Author: Jinchen

from Functions.power_function import power_function
from Functions.auxiliary_functions import total_count

def standard_deviation(args):
    count = len(args)
    if count > 0:
        # if the length of argument list is 1, return 0 directly
        if count == 1:
            return 0
        # compute mean
        mean = total_count(args)/count
        # get a new list after each item minus mean, and square
        args_new = []
        for i in range(count):
            args_new.append(args[i] - mean)

        for i in range(count):
            args_new[i] = power_function([args_new[i], 2])

        return power_function([total_count(args_new) / count, 0.5])

    else:
        raise TypeError('Invalid Argument !')





    

