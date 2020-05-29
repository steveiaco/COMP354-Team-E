#Goal: Calculate the specified power of a specified base
#MHandling: Does not compute complex numbers 

from math import floor
from math import sqrt

def power_function (base, power):
    #Case 1: Power is equal to 0
    if (power == 0):
        return 1
        
    #Case 2: Power is equal to 1
    elif (power == 1):
        return base
        
    #Case 3: Power is an integer neither equal to 0 nor to 1
    elif (floor(power) == power):
        return power_integer(base, power)
    
    #Case 4: Power is a decimal
    else:
        return power_fractional(base, power)

def power_integer(base, power):
    #Case 1: Power is a negative integer
    if (power < 0):
        base = 1/base
        power = -power
    
    #Case 2: Power is a positive integer greater than 1
    result = 1
    while(power > 1):
        if(power % 2 == 0):
            base = (base * base)
            power = power/2
        else: 
            result = base * result
            base = base * base
            power = (power - 1) / 2
    
    return base * result
    
def power_fractional (base, power):
    #Case 1: Power is between -1 and 1 exclusively 
    if (power > -1 and power < 1):
        integer_result = 1
        decimal_value = power
    #Case 2: Power is less than -1 or greater than 1
    else: 
        integer_value = floor(power)
        integer_result = power_integer(base, integer_value)
        decimal_value = power - integer_value
    
    #Case 3: Power is greater or equal to 0 and base is equal to 0
    if(power > 0 and base == 0):
        return 0
        
    precision = 0.0000000000001
    low = 0.0
    high = 1.0

    try: 
        root = sqrt(base)
        decimal_result = root;    
        mid = high / 2
    
        while(abs(mid - decimal_value) > precision):
            root = sqrt(root)
    
            if (mid <= decimal_value):
                low = mid
                decimal_result *= root
            else:
                high = mid
                decimal_result *= (1/root)
    
            mid = (low + high) / 2
    except Exception as e:
        print("ERROR: " + str(e))
        return -0.0
    
    return decimal_result * integer_result

def text_function ():
    answer = power_function(0,0.1)
    if (str(answer) != "-0.0"):
        print(answer)
        #Output-> 0
        #Validity-> Correct 
    answer = power_function(0,-0.1)
    if (str(answer) != "-0.0"):
        print(answer)
        #Output-> ERROR: float division by zero
        #Validity-> Correct: Answer is a complex number
    answer = power_function(2,1.1)
    if (str(answer) != "-0.0"):
        print(answer)
        #Output-> 2.143546925072451
        #Validity-> Correct
    answer = power_function(2,2)
    if (str(answer) != "-0.0"):
        print(answer)
        #Output-> 4
        #Validity-> Correct
    answer = power_function(4,sqrt(2))
    if (str(answer) != "-0.0"):
        print(answer)
        #Output-> 7.1029933013161255
        #Validity-> Correct
    answer = power_function(4,4)
    if (str(answer) != "-0.0"):
        print(answer)
        #Output-> 256
        #Validity-> Correct
    answer = power_function(-0.5,-0.5)
    if (str(answer) != "-0.0"):
        print(answer)
        #Output-> ERROR: math domain error
        #Validity-> Correct: Answer is a complex number

text_function()