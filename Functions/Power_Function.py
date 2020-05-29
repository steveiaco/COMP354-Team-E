#Goal: Calculate the specified power of a specified base
#Method: Exponentiation by squaring 

def power_function (args):
    base = 0
    power = 0

    # If the right number of arguments are passed, then continue
    if(len(args) == 2):
        base = args[0]
        power = args[1]
    else:
        raise Exception(f"Invalid number of arguments, power_function got {len(args)} but expected 2.")

    #Case 1: Power is a negative number
    if (power<0):
        base = 1/base
        power = -power

    #Case 2: Power is equal to 0
    if (power==0):
        return 1
    
    #Case 3: Power is equal to 1
    if (power==1):
        return base
    
    #Case 4: Power is a positive number greater than 1
    result=1
    while(power>1):
        if(power%2==0):
            base=(base*base)
            power=power/2
        else: 
            result=base*result
            base=base*base
            power=(power-1)/2
    
    return base*result