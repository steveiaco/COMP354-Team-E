# Class used for usage history
class ComputeResult:
    def __init__(
            self, function_called, input, output, error, error_message, function_called2, input2, output2, operator):
        self.function_called = function_called
        self.input = input
        self.output = output
        self.error = error
        self.error_message = error_message
        self.function_called2 = function_called2
        self.input2 = input2
        self.output2 = output2
        self.operator = operator
