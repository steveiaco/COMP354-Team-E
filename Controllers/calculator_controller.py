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
            'x^y': [power_function, 'Calculates the power function for a given base x and power y. \n\t\tInstructions: Call the function then input the power and the base as "x^y:power,base". For a fractional result, input 0 as a third argument.'],
        }

    ####
    # Functions called by the View
    ####

    def get_available_functions(self):
        return copy.deepcopy(self.function_map)

    def get_compute_history(self):
        return copy.deepcopy(self.compute_history)

    def get_compute_history_size(self):
        return len(self.compute_history)

    def parse_function_and_dispatch(self, function, arguments, precision = 0):

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
                # Check if user has specified a precision 
                if int(precision) > 0 and int(precision) <= 15:
                    result = round(result, int(precision))
                self.compute_history.append(ComputeResult(function, arguments, result, False, None))
            except Exception as e:
                print(str(e))
        else:
            self.compute_history.append(ComputeResult(function, arguments, None, True, "Invalid function name"))

        # Notify the observers that the model has changed
        self.notify()

    def invalid_user_input(self, input):
        self.compute_history.append(ComputeResult(input, None, None, True, "Invalid user input"))

        # Notify the observers that the model has changed
        self.notify()
    ####
    # Helper functions
    ####

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
