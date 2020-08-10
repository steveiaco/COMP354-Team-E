# Goal: Calculate the standard deviation of a given list
# Author: Jinchen

from Functions.power_function import power_function
from Functions.auxiliary_functions import total_count


def standard_deviation(args):
    # helper function that returns a list storing each value - mean
    def helper(arg_list, length):
        # compute mean
        mean = total_count(arg_list) / length
        # a new list stores the values of each element - mean
        args_new = []
        for i in range(length):
            args_new.append(arg_list[i] - mean)

        for i in range(length):
            args_new[i] = power_function([args_new[i], 2])
        return args_new

    count = len(args)
    if count > 1:
        # Get the last element in the list
        flag = args[-1]
        # population stdev
        if flag == 0.0:
            if count == 2:
                return 0
            else:
                args = args[:-1]
                count -= 1
                args_sqr = helper(args, count)
                return power_function([total_count(args_sqr) / count, 0.5])
        # sample stdev
        if flag == 1.0:
            # Sample stdev requires at least 2 numbers
            if count == 2:
                raise TypeError('Sample Standard Deviation requires at least '
                                '2 numbers !')
            else:
                args = args[:-1]
                count -= 1
                args_sqr = helper(args, count)
                return power_function([total_count(args_sqr)
                                       / (count - 1), 0.5])
        else:
            raise TypeError('Please specify the type of standard deviation !')
    else:
        raise TypeError('Invalid Argument !')
