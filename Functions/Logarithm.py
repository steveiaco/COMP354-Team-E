from Power_Function import power_function

#Goal: Calculate the natural logarithm, log base e, of a given input x
#Method: we use a series based on the area hyperbolic tangent function
def ln(x):
    #Variable used to store the calculated sum
    s = 0

    #Number of iterations currently hardcoded at 1000, but we can change this to an accuracy based metric by calculating the accuracy of e^s = x to a certain bound.
    for i in range(1000):
        s += ( 1 / (2 * i + 1) ) * power_function((x-1) / (x+1), 2 * i + 1)

    return 2 * s