import math

from calculator.Buttons.ButtonState import ButtonState


class Operation:
    def __init__(self, calculator):
        self.button_state = ButtonState(calculator)
        self.cont = 0
        self.point_cont = 0

    def insert_values(self, tecla, calculator):
        if tecla.isdigit():
            self.cont += 1

        if self.cont >= 1 or tecla == "(" or tecla == ")":
            if self.cont >= 1:
                self.button_state.point_button()
                self.button_state.operation_button()
                self.button_state.active_square_root_button()
            self.button_state.resoult_button()
            calculator.entrada_2.set(calculator.entrada_2.get() + tecla)
            self.cont = 0

        for point in range(0, len(calculator.entrada_2.get())):
            if calculator.entrada_2.get()[point] == ".":
                self.point_cont += 1
        if self.point_cont == 1:
            self.button_state.inactive_point_button()
        self.point_cont = 0
     
        if tecla == ".":
            calculator.entrada_2.set(calculator.entrada_2.get() + tecla)
            self.button_state.inactive_point_button()
            self.button_state.inactive_button_operation()
            self.button_state.inactive_rest_button()
        
        if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
            self.button_state.inactive_point_button()
            self.button_state.resoult_button_disabled()
            self.button_state.inactive_button_operation()
            self.button_state.active_rest_button()
            if tecla == "*":
                calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get() + "*")
            elif tecla == "/":
                calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get() + "/")
            elif tecla == "+":
                calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get() + "+")
            elif tecla == "-":
                calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get() + "-")
                self.button_state.inactive_rest_button()
            calculator.entrada_2.set('')

        if tecla == "=":
            open_bracket_counter = 0
            close_bracket_counter = 0
            self.button_state.resoult_button_disabled()
            calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get())

            for character in range(0, len(calculator.entrada_1.get())):
                if calculator.entrada_1.get()[character] == "(":
                    open_bracket_counter += 1
                elif calculator.entrada_1.get()[character] == ")":
                    close_bracket_counter += 1
            if calculator.entrada_1.get()[0] == "*" or calculator.entrada_1.get()[0] == "/":
                calculator.entrada_1.set("0" + calculator.entrada_1.get())

            try: 
                resoult = eval(calculator.entrada_1.get())
                calculator.entrada_2.set(resoult)
                calculator.entrada_1.set("")

            except SyntaxError:
                calculator.entrada_2.set("Error")
                self.button_state.inactive_buttons()

            except ZeroDivisionError:
                calculator.entrada_2.set("Error")
                self.button_state.inactive_buttons()

            if calculator.entrada_2.get().isdigit() == False:
                self.button_state.inactive_point_button()

            elif calculator.entrada_2.get().isdigit():
                self.button_state.point_button()

    def square_root(self, calculator):
        try:
            calculator.entrada_2.set(calculator.entrada_1.get() + calculator.entrada_2.get())
            eval_resoult = eval(calculator.entrada_2.get())
            calculator.entrada_2.set(eval_resoult)
            resoult = math.sqrt(float(calculator.entrada_2.get()))
            self.button_state.inactive_point_button()
            self.button_state.inactive_square_root()
            calculator.entrada_2.set(resoult)
            calculator.entrada_1.set("")

        except ValueError:
            calculator.entrada_2.set("Error")
            calculator.entrada_1.set("")
            self.button_state.inactive_buttons()