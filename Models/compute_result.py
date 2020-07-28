# Class used for usage history
class ComputeResult:
    def __init__(self, function_called, input, output, error, error_message):
        self.function_called = function_called
        self.input = input
        self.output = output
        self.error = error
        self.error_message = error_message
