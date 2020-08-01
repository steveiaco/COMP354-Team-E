# Goal: Calculate the standard deviation of a given list
# Author: Jinchen

from Functions.power_function import power_function
from Functions.auxiliary_functions import total_count


def standard_deviation(args):
    # helper function that returns a list storing each valie - mean
    def helper(arg_list, length):
        # compute mean
        mean = total_count(arg_list) / count
        # a new list stores the values of each element - mean
        args_new = []
        for i in range(length):
            args_new.append(arg_list[i] - mean)

        for i in range(length):
            args_new[i] = power_function([args_new[i], 2])
        return args_new

    count = len(args)
    if count > 0:
        print('Please choose the type of standard deviation')
        print('1. Population Standard Deviation')
        print('2. Sample Standard Deviation')
        option = input("Enter option: ")
        if option == '1':
            if count == 1:
                return 0
            else:
                args_sqr = helper(args, count)
                return power_function([total_count(args_sqr) / count, 0.5])
        if option == '2':
            # Sample stdev requires at least 2 numbers
            if count == 1:
                raise TypeError('Invalid Argument !')
            else:
                args_sqr = helper(args, count)
                return power_function([total_count(args_sqr) / (count-1), 0.5])
        else:
            raise TypeError('Invalid Argument !')
    else:
        raise TypeError('Invalid Argument !')