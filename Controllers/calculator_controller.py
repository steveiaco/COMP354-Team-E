# We setup the MVC architecture with an Observer design pattern so that the View is observing the
# controller and is updated whenever it changes.


class CalculatorController:

    def __init__(self):
        self.observers = []

    def handle_args(self, args):
        x = []

    def generate_function_instructions(self):
        return "placeholder"

    # Observer functions

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
