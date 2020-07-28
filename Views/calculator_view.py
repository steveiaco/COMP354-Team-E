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
        print('Print out usage history by inputting "history".')
        print(f'\nHere are the functions available for use:')
        print(self.controller.generate_function_instructions())

    def listen_to_user_input(self):

        self.update()
        # Loop until the user exits the script
        while True:
            # todo fix history
            returned = self.controller.handle_args(input("Enter expression: "))

    # Observer function used to update the view whenever there is a change in the Model / Controller
    def update(self):
        self.generate_cli()

        if len(self.controller.compute_history) > 0:
            last_operation = self.controller.compute_history[-1]

            if last_operation.error:
                print(f"{last_operation.function_called}:{last_operation.input} {last_operation.error_message}")
            else:
                print(f"{last_operation.function_called}:{last_operation.input} = {last_operation.output}")
