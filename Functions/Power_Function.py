#Goal: Calculate the specified power of a specified base
#Handling: Does not compute complex numbers 

def power_function (args):
    base = 0
    power = 0

    # If the right number of arguments are passed, then continue
    if(len(args) == 2):
        base = args[0]
        power = args[1]
    else:
        raise Exception(f"Invalid number of arguments, power_function got {len(args)} but expected 2.")
  
    #Case 1: Power is equal to 0
    if (power == 0):
        return 1
        
    #Case 2: Power is equal to 1
    elif (power == 1):
        return base
        
    #Case 3: Power is an integer neither equal to 0 nor to 1
    elif (floor_function(power) == power):
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
    #Case 1: Power is greater or equal to 0 and base is equal to 0
    if(power > 0 and base == 0):
        return 0
    #Case 2: Power is between 0 and 1 exclusively 
    elif (power > 0 and power < 1):
        integer_result = 1
        decimal_value = power
    #Case 3: Power is between -1 and 0 exclusively 
    elif (power > -1 and power < 0):
        try:
            return 1 / power_fractional(base, absolute_value(power))
        except Exception as e:
            return -0.0
    #Case 4: Power is less than -1 or greater than 1
    else: 
        integer_value = floor_function(power)
        integer_result = power_integer(base, integer_value)
        decimal_value = power - integer_value
    
    precision = 0.0000000000001
    low = 0.0
    high = 1.0

    try: 
        root = sqrt_function(base)
        decimal_result = root   
        mid = high / 2
    
        while(abs(mid - decimal_value) > precision):
            root = sqrt_function(root)
    
            if (mid <= decimal_value):
                low = mid
                decimal_result *= root
            else:
                high = mid
                decimal_result *= (1 / root)
    
            mid = (low + high) / 2
    except Exception as e:
        print("ERROR: " + str(e))
        return -0.0
    
    return decimal_result * integer_result

def floor_function(power):
    power *= 1.0
    number = str(power)

    #Case 1: Power is a non-integer negative number
    if (number[0] == "-" and power != int(power)):
        number = -1 * (int(number[1: number.find(".")]) + 1)
    #Case 2: Power is positive rational number
    else: 
        number = int(power)
    
    return number

def sqrt_function(base):
    precision = 0.0000000000001
    previous, mid = 0, float(base)

    while absolute_value(mid - previous) > precision:
        previous, mid = mid, (mid + (base / mid)) / 2.0
    
    return mid

def absolute_value(number):
    if (number < 0):
        number *= -1
    
    return number