import os


class CalculatorView:

    def __init__(self, controller):
        self.controller = controller

    def generate_cli(self):
        # todo: find a better way to clear the command prompt
        os.system("cls")
        # List valid inputs
        print('Welcome to ETERNITY')
        print('Separate function call and arguments by a colon (:)\nSeparate multiple arguments by a single comma .. arg1,arg2\nSample input: stdev:1,2,3')
        print('Print out usage history by inputting "history".')
        print(f'Here are the functions available for use:')
        print(self.controller.generate_function_instructions())

    # Observer function used to update the view whenever there is a change in the Model / Controller
    def update(self):
        temp = 1