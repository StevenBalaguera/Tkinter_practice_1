import math

from calculator.Buttons.ButtonState import ButtonState


class Operation:
    def __init__(self, calculator):
        self.calculator = calculator
        self.button_state = ButtonState(calculator)
        self.cont = 0
        self.point_cont = 0
        self.count_brakets = 0
        self.start = 0
        self.end = len(calculator.entrada_2.get())

    def insert_values(self, tecla):
        if tecla.isdigit():
            self.cont += 1

        if self.cont >= 1 or tecla == "(" or tecla == ")": 
            self.button_state.inactive_button_operation()
            self.button_state.inactive_point_button()
            self.button_state.inactive_square_root()
            self.button_state.resoult_button_disabled()
            self.button_state.active_open_brackets()
            self.button_state.active_closed_brackets()

            if self.cont >= 1:  
                self.button_state.point_button()
                self.button_state.operation_button()
                self.button_state.active_square_root_button()
                self.button_state.resoult_button()
            elif tecla == ")":
                self.button_state.inactive_closed_brackets()
                self.button_state.active_open_brackets()
                self.button_state.resoult_button()
                self.button_state.operation_button()

            elif tecla == "(":
                self.button_state.inactive_open_brackets()
                self.button_state.active_closed_brackets()

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
            numeric_cont = 0
            self.button_state.active_open_brackets()
            self.button_state.active_closed_brackets()
            self.button_state.resoult_button_disabled()
            self.calculator.entrada_1.set(self.calculator.entrada_1.get() + self.calculator.entrada_2.get())

            for character in range(0, len(self.calculator.entrada_1.get())):
                if self.calculator.entrada_1.get()[character] == "(":
                    open_bracket_counter += 1
                elif self.calculator.entrada_1.get()[character] == ")":
                    close_bracket_counter += 1   
                elif self.calculator.entrada_1.get()[character].isdigit():
                    numeric_cont += 1
            self.brackets_eval(open_bracket_counter, close_bracket_counter)
            if open_bracket_counter == 1 and close_bracket_counter == 1 and numeric_cont == 0:
                self.calculator.entrada_1.set("Error")  
            elif open_bracket_counter == 1 and close_bracket_counter == 0 and numeric_cont == 0:
                self.calculator.entrada_1.set("Error")

            if self.calculator.entrada_1.get()[0].isdigit() and self.calculator.entrada_1.get()[1] == "(" and self.calculator.entrada_1.get()[2].isdigit() and self.calculator.entrada_1.get()[3] == ")":
                self.calculator.entrada_1.set("Error")
            if self.calculator.entrada_1.get()[0].isdigit() and self.calculator.entrada_1.get()[1] == "(" and self.calculator.entrada_1.get()[2].isdigit():
                self.calculator.entrada_1.set("Error")
            try: 
                resoult = eval(self.calculator.entrada_1.get())
                self.calculator.entrada_2.set(resoult)
                self.calculator.entrada_1.set("")

            except SyntaxError:
                self.calculator.entrada_2.set("Error")
                self.calculator.entrada_1.set("")
                self.button_state.inactive_buttons()

            except ZeroDivisionError:
                self.calculator.entrada_2.set("Error")
                self.calculator.entrada_1.set("")
                self.button_state.inactive_buttons()

            except NameError:
                    self.calculator.entrada_2.set("Error")
                    self.calculator.entrada_1.set("")
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

        except SyntaxError:
            self.calculator.entrada_2.set("Error")
            self.calculator.entrada_1.set("")
            self.button_state.inactive_buttons()  

        except ZeroDivisionError:
            self.calculator.entrada_2.set("Error")
            self.calculator.entrada_1.set("")
            self.button_state.inactive_buttons()  

    def del_button(self):
        self.calculator.entrada_2.set(self.calculator.entrada_2.get()[self.start:self.end - 1])
        self.button_state.point_button()
        self.button_state.operation_button()
        self.button_state.inactive_open_brackets()
        self.button_state.inactive_closed_brackets()
        if not self.calculator.entrada_2.get().isdigit():
            self.button_state.resoult_button_disabled()
            self.button_state.inactive_point_button()
            self.button_state.inactive_button_operation()
            self.button_state.active_rest_button()
            self.button_state.active_open_brackets()
            self.button_state.active_closed_brackets()
        else:
            self.button_state.active_open_brackets()
            self.button_state.active_closed_brackets()

    def del_all_buttons(self):
        self.calculator.entrada_1.set(self.calculator.entrada_1.get()[self.start:self.end - self.end])
        self.calculator.entrada_2.set(self.calculator.entrada_2.get()[self.start:self.end - self.end])
        self.button_state.active_buttons()
        self.button_state.inactive_button_operation()
        self.button_state.resoult_button_disabled()
        self.button_state.inactive_point_button()

    def brackets_eval(self, cont_abierto, cont_cerrado):
        if cont_abierto == 0 and cont_cerrado == 1:
            self.calculator.entrada_1.set("(" + self.calculator.entrada_1.get())

        elif cont_abierto == 1 and cont_cerrado == 0:
            self.calculator.entrada_1.set(self.calculator.entrada_1.get() + ")")


