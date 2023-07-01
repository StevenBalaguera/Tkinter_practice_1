class Operation:
    def __init__(self):
        self.cont = 0
        self.point_cont = 0

    def inactive_buttons(self, calculator):
        self.inactive_button_operation(calculator)
        calculator.button_0.config(state = "disabled")
        calculator.button_1.config(state = "disabled")        
        calculator.button_2.config(state = "disabled")
        calculator.button_3.config(state = "disabled")
        calculator.button_4.config(state = "disabled")
        calculator.button_5.config(state = "disabled")
        calculator.button_6.config(state = "disabled")
        calculator.button_7.config(state = "disabled")
        calculator.button_8.config(state = "disabled")
        calculator.button_9.config(state = "disabled")
        calculator.del_button.config(state = "disabled")
        calculator.resoult_button.config(state = "disabled")
        calculator.bracket_button_1.config(state = "disabled")
        calculator.bracket_button_2.config(state = "disabled")
        calculator.point_button.config(state = "disabled")

    def inactive_button_operation(self, calculator):
        calculator.sum_button.config(state = "disabled")
        calculator.rest_button.config(state = "disabled")
        calculator.mult_button.config(state = "disabled")
        calculator.divition_button.config(state = "disabled")
        calculator.square_root_button.config(state = "disabled")

    def operation_button(self, calculator):
        calculator.sum_button.config(state = "Normal")
        calculator.rest_button.config(state = "Normal")
        calculator.mult_button.config(state = "Normal")
        calculator.divition_button.config(state = "Normal")

    def insert_values(self, tecla, calculator):
        calculator.point_button.config(state = "Normal")
        calculator.resoult_button.config(state = "Normal")
        if tecla.isdigit():
            self.cont += 1

        if self.cont >= 1 or tecla == "(" or tecla == ")":
            self.operation_button(calculator)
            calculator.square_root_button.config(state = "Normal")
            calculator.entrada_2.set(calculator.entrada_2.get() + tecla)
            self.cont = 0

        for point in range(0, len(calculator.entrada_2.get())):
            if calculator.entrada_2.get()[point] == ".":
                self.point_cont += 1
        if self.point_cont == 1:
            calculator.point_button.config(state = "disabled")
        self.point_cont = 0
     
        if tecla == ".":
            calculator.entrada_2.set(calculator.entrada_2.get() + tecla)
            calculator.point_button.config(state = "disabled")
            self.inactive_button_operation(calculator)
        
        if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
            calculator.point_button.config(state = "disabled")
            calculator.resoult_button.config(state = "disabled")
            self.inactive_button_operation(calculator)
            if tecla == "*":
                calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get() + "*")
            elif tecla == "/":
                calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get() + "/")
            elif tecla == "+":
                calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get() + "+")
            elif tecla == "-":
                calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get() + "-")
            calculator.entrada_2.set('')

        if tecla == "=":
            open_bracket_counter = 0
            close_bracket_counter = 0
            calculator.resoult_button.config(state = "disabled")
            calculator.entrada_1.set(calculator.entrada_1.get() + calculator.entrada_2.get())

            for character in range(0, len(calculator.entrada_1.get())):
                if calculator.entrada_1.get()[character] == "(":
                    open_bracket_counter += 1
                elif calculator.entrada_1.get()[character] == ")":
                    close_bracket_counter += 1
            if calculator.entrada_1.get()[0] == "*" or calculator.entrada_1.get()[0] == "/":
                calculator.entrada_1.set("0" + calculator.entrada_1.get())

            try: 
                resultado = eval(calculator.entrada_1.get())
                calculator.entrada_2.set(resultado)
                calculator.entrada_1.set("")

            except SyntaxError:
                calculator.entrada_2.set("Error")
                self.inactive_buttons(calculator)

            except ZeroDivisionError:
                calculator.entrada_2.set("Error")
                self.inactive_buttons(calculator)

            if calculator.entrada_2.get().isdigit() == False:
                calculator.point_button.config(state = "disabled")

            elif calculator.entrada_2.get().isdigit():
                calculator.point_button.config(state = "Normal")