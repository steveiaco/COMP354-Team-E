import copy
from Functions.power_function import power_function
from Functions.log import ln
from Functions.sine import sine
from Functions.cosh import cosh
from Functions.pi import pi_function
from Functions.mean_absolute_deviation import mean_absolute_deviation
from Functions.standard_deviation import standard_deviation

from Models.compute_result import ComputeResult


# We setup the MVC architecture with an Observer design pattern so that the View is observing the
# controller and is updated whenever it changes.


class CalculatorController:

    def __init__(self):
        self.observers = []

        # List used to store all previous function results
        self.compute_history = []

        # Variable which maps the function name to its helper description and function pointer.
        self.function_map = {
            'sin': [sine, 'Calculates the sine of an input x.'],
            'pi^': [pi_function, 'Calculates pi^x for a given input x.'],
            'ln': [ln, 'Calculates the natural logarithm for an input x.'],
            # 'a^x': [ph, 'NOT IMPLEMENTED.'],
            'mad': [mean_absolute_deviation, 'Calculates the mean absolute deviation for a given input [x,y,z,...].'],
            'stdev': [standard_deviation, 'Calculates the standard deviation for a given input [x,y,z,...].'],
            'cosh': [cosh, 'Calculates the hyperbolic cosine for a given input x.'],
            'x^y': [power_function, 'Calculates the power function for a given base x and power y.'],
        }

    ####
    # Functions called by the View
    ####

    def handle_args(self, args):

        # Split function from it's arguments
        user_input = args.split(':')

        if len(user_input) == 1 and user_input[0] == 'history':
            return self.__generate_compute_history()

        elif len(user_input) == 2:
            function = user_input[0]
            arguments = user_input[1].split(',')
            self.__parse_function_and_dispatch(function, arguments)

        else:
            print('Invalid input.')

        # Notify observers that there has been a change in the Models
        self.notify()

    def generate_function_instructions(self):
        return "placeholder"

    ####
    # Helper functions
    ####

    def __generate_compute_history(self):
        return copy.deepcopy(self.compute_history)

    def __parse_function_and_dispatch(self, function, arguments):

        # Try converting the list of strings into a list of numbers
        try:
            arguments = [float(i) for i in arguments]
        except Exception:
            self.compute_history.append(ComputeResult(function, arguments, None, True, "Invalid arguments"))

        # Check if the function specified exists in the function map, if it does, call the mapped function with the
        # provided arguments
        if function in self.function_map.keys():
            try:
                result = self.function_map[function][0](arguments)
                self.compute_history.append(ComputeResult(function, arguments, result, False, None))
            except Exception as e:
                print(str(e))
        else:
            self.compute_history.append(ComputeResult(function, arguments, None, True, "Invalid function name"))

    ####
    # Observer functions
    ####

    # Adds an observer to the controller
    def attach(self, observer):
        self.observers.append(observer)

    # Removes an observer from the controller
    def detach(self, observer):
        self.observers.remove(observer)

    # Notify all observers that there has been a change in the controller
    def notify(self):
        for o in self.observers:
            o.update()
