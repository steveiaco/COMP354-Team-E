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
        print('To indicate additional precision (up to 15), you can add a second colon (:) followed by a number '
              'between 1 and 15.\nSample input: ln:2:5')
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
            print(f"{h.function_called}:{h.input} {h.error_message}")
        else:
            print(f"{h.function_called}:{h.input} = {h.output}")

    # Observer function used to update the view whenever there is a change in the Model / Controller
    def update(self):
        self.generate_cli()

        if len(self.controller.compute_history) > 0:
            print("Last operation:")
            self.format_and_print_history_point(self.controller.compute_history[-1])
            print()