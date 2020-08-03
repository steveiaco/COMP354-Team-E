import os


class CalculatorView:

    def __init__(self, controller):
        self.controller = controller

    def generate_cli(self):
        # todo: find a better way to clear the command prompt
        os.system("cls")

        # Print ASCII logo
        print(" ______ ______ ______  ______  __   __  __  ______ __  __    ")
        print("/\\  ___/\\__  _/\\  ___\\/\\  == \\/\\ \"-.\\ \\/\\ \\/\\__  _/\\ \\_\\ \\   ")
        print("\\ \\  __\\/_/\\ \\\\ \\  __\\\\ \\  __<\\ \\ \\-.  \\ \\ \\/_/\\ \\\\ \\____ \\  ")
        print(" \\ \\_____\\\\ \\_\\\\ \\_____\\ \\_\\ \\_\\ \\_\\\\\"\\_\\ \\_\\ \\ \\_\\\\/\\_____\\ ")
        print("  \\/_____/ \\/_/ \\/_____/\\/_/ /_/\\/_/ \\/_/\\/_/  \\/_/ \\/_____/   \n")

        # Print usage instructions
        print("Usage instructions:")
        print('Separate function call and arguments by a colon (:)\nSeparate multiple arguments with commas .. arg1,'
              'arg2\nSample input: stdev:1,2,3')
        print('For arithmetic operation, space is required on both sides of operator\nSample input: sin:10 + cosh:10')
        print('To indicate additional precision (up to 15), you can add a second colon (:) followed by a number between 1 and 15.\nSample input: ln:2:5')
        print('Print out usage history by inputting "history".')
        print(f'\nHere are the functions available for use:')

        # Print function info
        functions = self.controller.get_available_functions()

        for k,v in functions.items():
            print(f'{k} : {v[1]}')

        #
        print(f"\nNumber of operations performed: {self.controller.get_compute_history_size()}\n")

    def listen_to_user_input(self):

        self.update()
        # Loop until the user exits the script
        while True:
            # Get input from user
            args = input("Enter expression: ")
            if (" + " in args) or (" - " in args) or (" * " in args) or (" / " in args):
                if "+" in args:
                    argsList = args.split("+")
                    self.arith_compute(argsList, "+")
                elif "-" in args:
                    argsList = args.split("-")
                    self.arith_compute(argsList, "-")
                elif "*" in args:
                    argsList = args.split("*")
                    self.arith_compute(argsList, "*")
                elif "/" in args:
                    argsList = args.split("/")
                    self.arith_compute(argsList, "/")

            else:
                # Split function from it's arguments
                user_input = args.split(':')

                if len(user_input) == 1 and user_input[0] == 'history':
                    self.print_history()

                elif len(user_input) == 2:
                    function = user_input[0]
                    arguments = user_input[1].split(',')
                    self.controller.parse_function_and_dispatch(function, arguments)

                elif len(user_input) == 3:
                    function = user_input[0]
                    arguments = user_input[1].split(',')
                    precision = user_input[2]
                    self.controller.parse_function_and_dispatch(function, arguments, precision)

                else:
                    self.controller.invalid_user_input(user_input)

    def print_history(self):
        history = self.controller.get_compute_history()

        print("\nOperation history:")
        for h in history:
            self.format_and_print_history_point(h)
        input("\nPress enter to continue...")
        self.update()

    @staticmethod
    def format_and_print_history_point(h):
        if h.error:
            if h.function_called2 is not None:
                print(f"{h.function_called}:{h.input} {h.operator} {h.function_called2}:{h.input2} {h.error_message}")
            else:
                print(f"{h.function_called}:{h.input} {h.error_message}")
        elif h.function_called2 is not None:
            if "+" in h.operator:
                finalres = h.output + h.output2
            elif "-" in h.operator:
                finalres = h.output - h.output2
            elif "*" in h.operator:
                finalres = h.output * h.output2
            elif "/" in h.operator:
                finalres = h.output / h.output2
            print(f"{h.function_called}:{h.input} {h.operator} {h.function_called2}:{h.input2} = {finalres}")
        else:
            print(f"{h.function_called}:{h.input} = {h.output}")

    # Observer function used to update the view whenever there is a change in the Model / Controller
    def update(self):
        self.generate_cli()

        if len(self.controller.compute_history) > 0:
            print("Last operation:")
            self.format_and_print_history_point(self.controller.compute_history[-1])
            print()

    def arith_compute(self, argsList, operator):
        if len(argsList) != 2:
            print("invalid input: too many terms")
        arg0 = argsList[0]
        arg0List = arg0.split(':')
        precision0 = 0
        if len(arg0List) == 3:
            precision0 = arg0List[2]
        arg0Function = arg0List[0]
        arg0Arguments = arg0List[1].split(',')

        arg1 = argsList[1]
        arg1List = arg1.split(':')
        precision1 = 0
        if len(arg0List) == 3:
            precision1 = arg1List[2]
        arg1Function = arg1List[0]
        arg1Arguments = arg1List[1].split(',')

        # should be space on both sides
        if (arg0Arguments[-1][-1] != " ") or (arg1Function[0] != " "):
            self.compute_history.append(ComputeResult(function, arguments, None, True, "Invalid arguments", None,
                                                      None, None, None))
        arg1Function = arg1Function[1:len(arg1Function)]
        self.controller.arith_parse(arg0Function, arg0Arguments, precision0, arg1Function, arg1Arguments, precision1,
                                    operator)
