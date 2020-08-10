import copy
from Functions.power_function import power_function
from Functions.log import ln
from Functions.log import log
from Functions.sine import sine
from Functions.cosh import cosh
from Functions.pi import pi_function
from Functions.mean_absolute_deviation import mean_absolute_deviation
from Functions.standard_deviation import standard_deviation

from Models.compute_result import ComputeResult


# We setup the MVC architecture with an Observer design pattern so that
# the View is observing the controller and is updated whenever it
# changes.


class CalculatorController:

    def __init__(self):
        self.observers = []

        # List used to store all previous function results
        self.compute_history = []

        # Variable which maps the function name to its helper
        # description and function pointer.
        self.function_map = {
            'sin': [sine, '\tCalculates the sine of an input x. Optional: '
                          'Specify "radians" or "degrees" at the end of '
                          'the input to specify the input type. Default is '
                          'radians if nothing is added. '
                          '\n\t\tExample input: sin(5) radians'],
            'pi^': [pi_function, '\tCalculates pi^x for a given input x.'
                                 '\n\t\tExample input: pi^5'],
            'ln': [ln, '\tCalculates the natural logarithm for an input x.'],
            'log': [log, '\tCalculates the logarithm for an operand '
                         'x.\n\t\tOptional: base b is optional, b = 10 if it '
                         'is excluded.\n\t\tExample: log(5) base 2'],
            'mad': [mean_absolute_deviation, '\tCalculates the mean absolute '
                                             'deviation for a given input ['
                                             'x,y,z,...]. '
                                             '\n\t\tExample input: mad:1,2,3'],
            'stdev': [standard_deviation, 'Calculates the standard deviation '
                                          'for a given input [x,y,z,...0/1]. '
                                          'Optional '
                                          ': Specify "population" or '
                                          '"sample" at the end of the input '
                                          'to specify '
                                          'population or sample standard '
                                          'deviation. '
                                          '\n\t\tExample input: stdev:1,2,'
                                          '3 population'],
            'cosh': [cosh, '\tCalculates the hyperbolic cosine for a given '
                           'input x. Optional: Specify "radians" or '
                           '"degrees" at the end of the input to specify the '
                           'input type. Default is radians if '
                           'nothing is added.'
                           '\n\t\tExample input: cosh(5) degrees'],
            'x^y': [power_function, '\tCalculates the power function for a '
                                    'given base x and power y. Optional: '
                                    'Specify "fraction" at the end of the '
                                    'input for a fractional result. '
                                    '\n\t\tExample input: 5^-1.1 fraction'],
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

    def parse_function_and_dispatch(self, function, arguments, precision=0):

        # Try converting the list of strings into a list of numbers
        try:
            arguments = [float(i) for i in arguments]
        except Exception:
            self.compute_history.append(ComputeResult(function, arguments,
                                                      None, True,
                                                      "Invalid arguments"))

        # Check if the function specified exists in the function map,
        # if it does, call the mapped function with the provided
        # arguments
        if function in self.function_map.keys():
            try:
                result = self.function_map[function][0](arguments)
                # Check if user has specified a precision 
                if int(precision) > 0 and int(precision) <= 15:
                    result = round(result, int(precision))
                self.compute_history.append(ComputeResult(function, arguments,
                                                          result, False, None,
                                                          None, None, None,
                                                          None))
            except Exception as e:
                print(str(e))
        else:
            self.compute_history.append(ComputeResult(function, arguments,
                                                      None, True,
                                                      "Invalid function name",
                                                      None, None, None, None))

        # Notify the observers that the model has changed
        self.notify()

    def arith_parse(self, function, arguments, precision, function2,
                    arguments2, precision2, operator):
        # Try converting the list of strings into a list of numbers
        result2 = 0
        try:
            arguments = [float(i) for i in arguments]
            arguments2 = [float(e) for e in arguments2]
        except Exception:
            self.compute_history.append(ComputeResult(function, arguments,
                                                      None, True,
                                                      "Invalid arguments",
                                                      None, None, None, None))
        if (function in self.function_map.keys()) and \
                (function2 in self.function_map.keys()):
            try:
                result = self.function_map[function][0](arguments)
                # Check if user has specified a precision
                if 0 < int(precision) <= 15:
                    result = round(result, int(precision))
            except Exception as e:
                print(str(e))
            try:
                result2 = self.function_map[function2][0](arguments2)
                # Check if user has specified a precision
                if 0 < int(precision2) <= 15:
                    result2 = round(result2, int(precision))
            except Exception as e:
                print(str(e))
            self.compute_history.append(ComputeResult(function, arguments,
                                                      result, False, None,
                                                      function2, arguments2,
                                                      result2, operator))

        else:
            self.compute_history.append(ComputeResult(function, arguments,
                                                      None, True,
                                                      "Invalid function name",
                                                      function2, arguments2,
                                                      None, operator))
        self.notify()

    def invalid_user_input(self, input):
        self.compute_history.append(ComputeResult(input, None, None, True,
                                                  "Invalid user input", None,
                                                  None, None, None))

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

    # Notify all observers that there has been a change in the
    # controller
    def notify(self):
        for o in self.observers:
            o.update()
