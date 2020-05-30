from Power_Function import power_function
from Logarithm import ln

#Placeholder function for the function map
def ph(args):
    #do nothing
    print(f'Arguments received : {args}')
    return

# Variable which maps the function name to its helper description and function pointer.
function_map = {
    'sin': [ph, 'Description placeholder'],
    'pi^': [ph, 'Description placeholder'],
    'ln': [ln, 'Description placeholder'],
    'a^x': [ph, 'Description placeholder'],
    'mad': [ph, 'Description placeholder'],
    'stdev': [ph, 'Description placeholder'],
    'cosh': [ph, 'Description placeholder'],
    'x^y': [power_function, 'Description placeholder'],
}

def main():
    #List valid inputs
    print('Welcome to ETERNITY')
    print('Separate function call and arguments by a colon (:)\nSeparate multiple arguments by a single comma (arg1,arg2)')
    print(f'Here are the functions available for use:')

    for k,v in function_map.items():
        print(f'{k} : {v[1]}')
    print()

    # Loop until the user exits the script
    while True:
        user_input = input("Enter expression: ").split(':')

        if len(user_input) == 2:
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
                    print(f'Result: {function_map[function][0](arguments)}')
                except Exception as e:
                    print(str(e))
            else:
                print('Invalid.')

        else:
            print('Invalid input.')


if __name__ == "__main__":
    main()