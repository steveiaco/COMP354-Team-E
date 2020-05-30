# Algorithm
# 1. Calculate Mean
# 2. Sum the absolute values of all values minus the mean
# 3. Divide the sum by the number of values

# Primary Algoirthm
def mean_absolute_deviation(args):
    
    # Local variables
    mean = calculate_mean(args)
    dividend = 0
    diviser = len(args)

    # Calculate the dividend
    for x in args:
        dividend += absolute_value(x - mean)

    # Return the Mean Absolute Deviation
    return (float(dividend) / diviser)
        
# Helper Functions
def calculate_mean(input): 
    sum = 0
    for x in input:
        sum += x
    return (sum / len(input))

def absolute_value(input):
    if input < 0:
        return -input
    else:
        return input

# Test Functions
# --------------

# Should equal 127.2
x = mean_absolute_deviation([600, 470, 170, 430, 300])

# Should equal 3.75
y = mean_absolute_deviation([3, 6, 6, 7, 8, 11, 15, 16])

# Should equal 0.0
z = mean_absolute_deviation([0, 0, 0, 0, 0, 0])


print(x)
print(y)
print(z)
