#Goal: Calculate the standard deviation of a given list
# Author: Jinchen

from power_function import power_function

def standard_deviation(input):
    count = len(input)
    if count > 0:
        # if the length of argument list is 1, return 0 directly
        if count == 1:
            return 0
        # compute mean
        args = np.array(input)
        mean = total_count(args)/count
        # get a new list after each item minus mean, and square
        args_new = args - mean
        for i in range(count):
            args_new[i] = power_function([args_new[i], 2])

        return power_function([total_count(args_new) / count, 0.5])

    else:
        raise TypeError('Invalid Argument !')


def total_count(args):
    s = 0
    for i in range(len(args)):
        s = s + args[i]
    return s


    

