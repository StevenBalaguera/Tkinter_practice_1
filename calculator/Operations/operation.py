class Operation:
    def __init__(self):
        self.cont = 0
        self.point_cont = 0

    def inactive_buttons(self, button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, sum_button, rest_button, mult_button, divition_button, square_root_button, del_buton, resoult_button, bracket_button_1, bracket_button_2, boton_point):
        self.inactive_button_operation(sum_button, rest_button, mult_button, divition_button, square_root_button)
        button_0.config(state = "disabled")
        button_1.config(state = "disabled")        
        button_2.config(state = "disabled")
        button_3.config(state = "disabled")
        button_4.config(state = "disabled")
        button_5.config(state = "disabled")
        button_6.config(state = "disabled")
        button_7.config(state = "disabled")
        button_8.config(state = "disabled")
        button_9.config(state = "disabled")
        del_buton.config(state = "disabled")
        resoult_button.config(state = "disabled")
        bracket_button_1.config(state = "disabled")
        bracket_button_2.config(state = "disabled")
        boton_point.config(state = "disabled")

    def inactive_button_operation(self, boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada):
        boton_suma.config(state = "disabled")
        boton_resta.config(state = "disabled")
        boton_multiplicacion.config(state = "disabled")
        boton_division.config(state = "disabled")
        boton_raiz_cuadrada.config(state = "disabled")

    def operation_button(self, boton_suma, boton_resta, boton_multiplicacion, boton_division):
        boton_suma.config(state = "Normal")
        boton_resta.config(state = "Normal")
        boton_multiplicacion.config(state = "Normal")
        boton_division.config(state = "Normal")

    def insert_values(self, tecla, boton_parentesis_1, boton_parentesis_2, del_buton,  boton_0, boton_1, boton_2, boton_3, boton_4, boton_5, boton_6, boton_7, boton_8, boton_9, entrada_1, entrada_2, boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada, boton_punto, boton_resultado):
        boton_punto.config(state = "Normal")
        boton_resultado.config(state = "Normal")
        if tecla.isdigit():
            self.cont += 1

        if self.cont >= 1 or tecla == "(" or tecla == ")":
            self.operation_button(boton_suma, boton_resta, boton_multiplicacion, boton_division)
            boton_raiz_cuadrada.config(state = "Normal")
            entrada_2.set(entrada_2.get() + tecla)
            self.cont = 0

        for point in range(0, len(entrada_2.get())):
            if entrada_2.get()[point] == ".":
                self.point_cont += 1
        if self.point_cont == 1:
            boton_punto.config(state = "disabled")
        self.point_cont = 0
     
        if tecla == ".":
            entrada_2.set(entrada_2.get() + tecla)
            boton_punto.config(state = "disabled")
            self.inactive_button_operation(boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada)
        
        if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
            boton_resultado.config(state = "disabled")
            self.inactive_button_operation(boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada)
            if tecla == "*":
                entrada_1.set(entrada_1.get() + entrada_2.get() + "*")
            elif tecla == "/":
                entrada_1.set(entrada_1.get() + entrada_2.get() + "/")
            elif tecla == "+":
                entrada_1.set(entrada_1.get() + entrada_2.get() + "+")
            elif tecla == "-":
                entrada_1.set(entrada_1.get() + entrada_2.get() + "-")
            entrada_2.set('')

        if tecla == "=":
            open_bracket_counter = 0
            close_bracket_counter = 0
            boton_resultado.config(state = "disabled")
            entrada_1.set(entrada_1.get() + entrada_2.get())

            for character in range(0, len(entrada_1.get())):
                if entrada_1.get()[character] == "(":
                    open_bracket_counter += 1
                elif entrada_1.get()[character] == ")":
                    close_bracket_counter += 1
            if entrada_1.get()[0] == "*" or entrada_1.get()[0] == "/":
                entrada_1.set("0" + entrada_1.get())

            try: 
                resultado = eval(entrada_1.get())
                entrada_2.set(resultado)
                entrada_1.set("")

            except SyntaxError:
                entrada_2.set("Error")
                self.inactive_buttons(boton_0, boton_1, boton_2, boton_3, boton_4, boton_4, boton_5, boton_6, boton_7, boton_8, boton_9, boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada, del_buton, boton_parentesis_1, boton_parentesis_2, boton_punto)

            except ZeroDivisionError:
                entrada_2.set("Error")
                self.inactive_buttons(boton_0, boton_1, boton_2, boton_3, boton_4, boton_4, boton_5, boton_6, boton_7, boton_8, boton_9, boton_suma, boton_resta, boton_multiplicacion, boton_division, boton_raiz_cuadrada, del_buton, boton_parentesis_1, boton_parentesis_2, boton_punto)

            if entrada_2.get().isdigit() == False:
                boton_punto.config(state = "disabled")

            elif entrada_2.get().isdigit():
                boton_punto.config(state = "Normal")