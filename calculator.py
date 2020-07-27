from power_function import power_function
from log import ln
from sine import sine
from cosh import cosh
from pi import pi_function
from mean_absolute_deviation import mean_absolute_deviation
from standard_deviation import standard_deviation


# Class used for usage history
class UsagePoint:
    def __init__(self, function_called, input, output):
        self.function_called = function_called
        self.input = input
        self.output = output


# Placeholder function for the function map
def ph(args):
    #do nothing
    print(f'Arguments received : {args}')
    return


# Variable which maps the function name to its helper description and function pointer.
function_map = {
    'sin': [sine, 'Calculates the sine of an input x.'],
    'pi^': [pi_function, 'Calculates pi^x for a given input x.'],
    'ln': [ln, 'Calculates the natural logarithm for an input x.'],
    #'a^x': [ph, 'NOT IMPLEMENTED.'],
    'mad': [mean_absolute_deviation, 'Calculates the mean absolute deviation for a given input [x,y,z,...].'],
    'stdev': [standard_deviation, 'Calculates the standard deviation for a given input [x,y,z,...].'],
    'cosh': [cosh, 'Calculates the hyperbolic cosine for a given input x.'],
    'x^y': [power_function, 'Calculates the power function for a given base x and power y.'],
}

def main():
    #List valid inputs
    print('Welcome to ETERNITY')
    print('Separate function call and arguments by a colon (:)\nSeparate multiple arguments by a single comma .. arg1,arg2\nSample input: stdev:1,2,3')
    print('Print out usage history by inputting "history".')
    print(f'Here are the functions available for use:')

    for k,v in function_map.items():
        print(f'{k} : {v[1]}')
    print()

    # Create list used to store all previous function results
    usage_history = []

    # Loop until the user exits the script
    while True:
        user_input = input("Enter expression: ").split(':')

        if len(user_input) == 1 and user_input[0] == 'history':
            if len(usage_history) > 0 :
                for history in usage_history:
                    print(f"Function called: {history.function_called}, Input: {history.input}, Output: {history.output}")
            else:
                print("No history to show")

        elif len(user_input) == 2:
            function = user_input[0]
            arguments = user_input[1].split(',')

            # Try converting the list of strings into a list of numbers
            try:
                arguments = [float(i) for i in arguments]
            except Exception:
                print('Invalid argument(s).')
                continue

            # Check if the function specified exists in the function map, if it does, call the mapped function with the provided arguments
            if function in function_map.keys():
                try:
                    result = function_map[function][0](arguments)
                    usage_history.append(UsagePoint(function, arguments, result))

                    print(f'Result: {result}')
                except Exception as e:
                    print(str(e))
            else:
                print('Invalid.')
        else:
            print('Invalid input.')


if __name__ == "__main__":
    main()