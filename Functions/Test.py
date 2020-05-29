from Power_Function import power_function
from math import sqrt

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
