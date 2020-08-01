from Controllers.calculator_controller import CalculatorController
from Views.calculator_view import CalculatorView


def main():
    # Instantiate the controller and view
    controller = CalculatorController()
    view = CalculatorView(controller)

    # Subscribe the view as an observer of the controller
    controller.attach(view)

    view.listen_to_user_input()


if __name__ == "__main__":
    main()
