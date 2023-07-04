import math

from calculator.Buttons.ButtonState import ButtonState


class Operation:
    def __init__(self, calculator):
        self.calculator = calculator
        self.button_state = ButtonState(calculator)
        self.cont = 0
        self.point_cont = 0
        self.start = 0
        self.end = len(calculator.entrada_2.get())

    def insert_values(self, tecla):
        if tecla.isdigit():
            self.cont += 1

        if self.cont >= 1 or tecla == "(" or tecla == ")": 
            self.button_state.resoult_button()         
            self.button_state.inactive_button_operation()
            self.button_state.inactive_rest_button()
            self.button_state.inactive_square_root()

            if self.cont >= 1:  
                self.button_state.point_button()
                self.button_state.operation_button()
                self.button_state.active_square_root_button()
                self.button_state.resoult_button()

            self.calculator.entrada_2.set(self.calculator.entrada_2.get() + tecla)
            self.cont = 0

        for point in range(0, len(self.calculator.entrada_2.get())):
            if self.calculator.entrada_2.get()[point] == ".":
                self.point_cont += 1
        if self.point_cont == 1:
            self.button_state.inactive_point_button()
        self.point_cont = 0
     
        if tecla == ".":
            self.calculator.entrada_2.set(self.calculator.entrada_2.get() + tecla)
            self.button_state.inactive_point_button()
            self.button_state.inactive_button_operation()
            self.button_state.inactive_rest_button()
        
        if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
            self.button_state.inactive_point_button()
            self.button_state.resoult_button_disabled()
            self.button_state.inactive_button_operation()
            self.button_state.active_rest_button()
            if tecla == "*":
                self.calculator.entrada_1.set(self.calculator.entrada_1.get() + self.calculator.entrada_2.get() + "*")
            elif tecla == "/":
                self.calculator.entrada_1.set(self.calculator.entrada_1.get() + self.calculator.entrada_2.get() + "/")
            elif tecla == "+":
                self.calculator.entrada_1.set(self.calculator.entrada_1.get() + self.calculator.entrada_2.get() + "+")
            elif tecla == "-":
                self.calculator.entrada_1.set(self.calculator.entrada_1.get() + self.calculator.entrada_2.get() + "-")
                self.button_state.inactive_rest_button()
            self.calculator.entrada_2.set('')

        if tecla == "=":
            open_bracket_counter = 0
            close_bracket_counter = 0
            self.button_state.resoult_button_disabled()
            self.calculator.entrada_1.set(self.calculator.entrada_1.get() + self.calculator.entrada_2.get())

            for character in range(0, len(self.calculator.entrada_1.get())):
                if self.calculator.entrada_1.get()[character] == "(":
                    open_bracket_counter += 1
                elif self.calculator.entrada_1.get()[character] == ")":
                    close_bracket_counter += 1

            try: 
                resoult = eval(self.calculator.entrada_1.get())
                self.calculator.entrada_2.set(resoult)
                self.calculator.entrada_1.set("")

            except SyntaxError:
                self.calculator.entrada_2.set("Error")
                self.button_state.inactive_buttons()

            except ZeroDivisionError:
                self.calculator.entrada_2.set("Error")
                self.button_state.inactive_buttons()

            if self.calculator.entrada_2.get().isdigit() == False:
                self.button_state.inactive_point_button()

            elif self.calculator.entrada_2.get().isdigit():
                self.button_state.point_button()

    def square_root(self):
        try:
            self.calculator.entrada_2.set(self.calculator.entrada_1.get() + self.calculator.entrada_2.get())
            eval_resoult = eval(self.calculator.entrada_2.get())
            self.calculator.entrada_2.set(eval_resoult)
            resoult = math.sqrt(float(self.calculator.entrada_2.get()))
            self.button_state.inactive_point_button()
            self.button_state.inactive_square_root()
            self.calculator.entrada_2.set(resoult)
            self.calculator.entrada_1.set("")

        except ValueError:
            self.calculator.entrada_2.set("Error")
            self.calculator.entrada_1.set("")
            self.button_state.inactive_buttons()

        except TypeError:
            self.calculator.entrada_2.set("Error")
            self.calculator.entrada_1.set("")
            self.button_state.inactive_buttons()            

    def del_button(self):
        self.calculator.entrada_2.set(self.calculator.entrada_2.get()[self.start:self.end - 1])
        self.button_state.point_button()
        if not self.calculator.entrada_2.get().isdigit():
            self.button_state.resoult_button_disabled()
            self.button_state.inactive_point_button()
            self.button_state.inactive_button_operation()
            self.button_state.active_rest_button()

    def del_all_buttons(self):
        self.calculator.entrada_1.set(self.calculator.entrada_1.get()[self.start:self.end - self.end])
        self.calculator.entrada_2.set(self.calculator.entrada_2.get()[self.start:self.end - self.end])
        self.button_state.active_buttons()
        self.button_state.inactive_button_operation()
        self.button_state.resoult_button_disabled()
        self.button_state.inactive_point_button()


