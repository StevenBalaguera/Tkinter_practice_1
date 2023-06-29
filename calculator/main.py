from tkinter import *
from tkinter import ttk
import math

cont = 0
contador_punto = 0

def evaluacion_parentesis(cont_abierto, cont_cerrado):
	if cont_abierto == 0 and cont_cerrado == 1:
		entrada_1.set("(" + entrada_1.get())

	elif cont_abierto == 1 and cont_cerrado == 0:
		entrada_1.set(entrada_1.get() + ")")

	elif cont_abierto == 2 and cont_cerrado == 1:
		entrada_1.set(entrada_1.get() + ")")

	elif cont_abierto == 1 and cont_cerrado == 2:
		entrada_1.set("(" + entrada_1.get())

	elif cont_abierto == 2 and cont_cerrado == 0:
		entrada_1.set(entrada_1.get() + ")" + ")")

	elif cont_abierto == 0 and cont_cerrado == 2:
		entrada_1.set("(" + "(" + entrada_1.get())

	elif cont_abierto == 3 and cont_cerrado == 0:
		entrada_1.set(entrada_1.get() + ")" + ")" + ")")	

def Tema_Claro(*args):
	estilos_frame.configure('mainFrame.TFrame', background = "#DBDBDB", foreground = "black")
    
	estilo_label_1.configure('label1.TLabel', background = "#DBDBDB", foreground = "black")
	estilos_label_2.configure('label2.TLabel', background = "#DBDBDB", foreground = "black")

	botones_numericos.configure('botones_numericos.TButton', background = "#FFFFFF", foreground = "black")
	botones_numericos.map('botones_numericos.TButton', background = [("active","#EAEEE0")])

	botones_borrar.configure('botones_borrar.TButton', background = "#CECECE", foreground = "black")
	botones_borrar.map('botones_borrar.TButton', background = [("active","#858585")])

	botones_restantes.configure('botones_restantes.TButton', background = "#CECECE", foreground = "black")
	botones_restantes.map('botones_restantes.TButton', background = [("active", "#858585")])

	boton_igual.configure('boton_igual.TButton', background = "#CECECE", foreground = "black")
	boton_igual.map('boton_igual.TButton', background = [("active", "#DADADC")])

def Tema_Oscuro(*args):
	estilos_frame.configure('mainFrame.TFrame', background = "#010924")

	estilo_label_1.configure('label1.TLabel', background = "#010924", foreground = "white")
	estilos_label_2.configure('label2.TLabel', background = "#010924", foreground = "white")

	botones_numericos.configure('botones_numericos.TButton', background = "#00044A", foreground = "white")
	botones_numericos.map('botones_numericos.TButton', background = [("active", "#020A90")])

	botones_borrar.configure('botones_borrar.TButton', background = "#010924", foreground = "white")
	botones_borrar.map('botones_borrar.TButton', background = [("active", "#000AB1")])

	botones_restantes.configure('botones_restantes.TButton', background = "#010924", foreground = "white")
	botones_restantes.map('botones_restantes.TButton', background = [("active", "#000AB1")])

	boton_igual.configure('boton_igual.TButton', background = "#010924", foreground = "white")
	boton_igual.map('boton_igual.TButton', background = [("active", "#000AB1")])

def boton_operacion():
	boton_resta.config(state = "Normal")
	boton_suma.config(state = "Normal")
	boton_multiplicacion.config(state = "Normal")
	boton_division.config(state = "Normal")

def boton_operacion_inactivo():
	boton_resta.config(state = "disabled")
	boton_suma.config(state = "disabled")
	boton_multiplicacion.config(state = "disabled")
	boton_division.config(state = "disabled")
	boton_raiz_cuadrada.config(state = "disabled")

def boton_validacion_activo():
	boton_operacion()
	del_buttons.config(state = "Normal")
	boton_raiz_cuadrada.config(state = "Normal")
	boton_resultado.config(state = "Normal")  
	boton_parentesis_1.config(state = "Normal")  
	boton_parentesis_2.config(state = "Normal")  
	boton_punto.config(state = "Normal") 
	boton_0.config(state = "Normal")
	boton_1.config(state = "Normal")
	boton_2.config(state = "Normal")
	boton_3.config(state = "Normal")
	boton_4.config(state = "Normal")
	boton_5.config(state = "Normal")
	boton_6.config(state = "Normal")
	boton_7.config(state = "Normal")
	boton_8.config(state = "Normal")
	boton_9.config(state = "Normal")

def boton_validacion_operacion():
    boton_operacion_inactivo()
    del_buttons.config(state = "disabled")
    boton_resultado.config(state = "disabled")  
    boton_parentesis_1.config(state = "disabled")  
    boton_parentesis_2.config(state = "disabled")  
    boton_raiz_cuadrada.config(state = "disabled")
    boton_punto.config(state = "disabled") 
    boton_0.config(state = "disabled")
    boton_1.config(state = "disabled")
    boton_2.config(state = "disabled")
    boton_3.config(state = "disabled")
    boton_4.config(state = "disabled")
    boton_5.config(state = "disabled")
    boton_6.config(state = "disabled")
    boton_7.config(state = "disabled")
    boton_8.config(state = "disabled")
    boton_9.config(state = "disabled")

def raiz_cuadrada():
	entrada_1.set("")
	try:
		resultado = math.sqrt(float(entrada_2.get()))
		boton_raiz_cuadrada.config(state = "disabled")
		boton_punto.config(state = "disabled")
		entrada_2.set("")
		entrada_1.set(resultado)
		boton_resultado.config(state = "Normal")	
	except ValueError:
		entrada_2.set("Error")
		boton_validacion_operacion()


def borrar():
	inicio = 0
	final = len(entrada_2.get())
	entrada_2.set(entrada_2.get()[inicio:final-1])
	boton_punto.config(state = "Normal")
	if entrada_2.get().isdigit() == False:
		boton_punto.config(state = "disabled")
		boton_operacion_inactivo()

def borrar_todo():
	inicio = 0
	final = len(entrada_2.get())
	entrada_1.set(entrada_1.get()[inicio:final-final])
	entrada_2.set(entrada_2.get()[inicio:final-final])
	boton_validacion_activo()
	boton_operacion_inactivo()
	boton_resultado.config(state = "disabled")
	boton_resta.config(state = "Normal")
	boton_punto.config(state = "disabled")	

def inserta_valores(tecla):
	global cont
	global contador_punto
	boton_punto.config(state = "Normal")	
	boton_resultado.config(state = "Normal")
	if tecla.isdigit():
		cont += 1
	if cont >= 1 or tecla == "(" or tecla == ")":
		boton_operacion()
		boton_resultado.config(state = "Normal")
		boton_raiz_cuadrada.config(state = "Normal")	
		entrada_2.set(entrada_2.get() + tecla)
		for i in range(0, len(entrada_2.get())):
			if entrada_2.get()[i] == ".":
				contador_punto += 1
		if contador_punto == 1:
			boton_punto.config(state = "disabled")	
	contador_punto = 0		
	cont = 0	 
	if tecla == ".":
		entrada_2.set(entrada_2.get() + tecla)
		boton_punto.config(state = "disabled")
		boton_operacion_inactivo()

	if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
		boton_punto.config(state = "disabled")
		boton_resultado.config(state = "disabled")
		if tecla == "*":
			boton_operacion_inactivo()
			entrada_1.set(entrada_1.get() + entrada_2.get() + "*")

		elif tecla == "/":
			boton_operacion_inactivo()
			entrada_1.set(entrada_1.get() + entrada_2.get() + "/")

		elif tecla == "+":
			boton_operacion_inactivo()
			entrada_1.set(entrada_1.get() + entrada_2.get() + "+")

		elif tecla == "-":
			boton_operacion_inactivo()
			entrada_1.set(entrada_1.get() + entrada_2.get() + "-")	
		entrada_2.set('')
    
	if tecla == "=":
		contador_parentesis_abierto = 0
		contador_parentesis_cerrado = 0

		boton_resultado.config(state = "disabled")
		entrada_1.set(entrada_1.get() + entrada_2.get())

		for character in range(0, len(entrada_1.get())):
			if entrada_1.get()[character] == "(":
				contador_parentesis_abierto += 1 
			if entrada_1.get()[character] == ")":
				contador_parentesis_cerrado += 1 	
		if  entrada_1.get()[0] == "*" or entrada_1.get()[0] == "/": 
			entrada_1.set("0" + entrada_1.get())

		evaluacion_parentesis(contador_parentesis_abierto, contador_parentesis_cerrado)

		try:
			resultado = eval(entrada_1.get())
			entrada_2.set(resultado)
			entrada_1.set("")
    
		except SyntaxError:
			entrada_2.set("Error")
			boton_validacion_operacion()
			
		except ZeroDivisionError:
			entrada_2.set("Error")
			boton_validacion_operacion()

		if entrada_2.get().isdigit() == False:
			boton_punto.config(state = "disabled")

		elif entrada_2.get().isdigit():
			boton_punto.config(state = "Normal")		

root = Tk()
root.title("calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

estilos_frame = ttk.Style()
estilos_frame.theme_use("clam")
estilos_frame.configure('mainFrame.TFrame', background = "#DBDBDB")

main_frame = ttk.Frame(root, style = "mainFrame.TFrame")
main_frame.grid(row = 0, column = 0, sticky = (W, N, E, S ))
main_frame.config(cursor = "hand2")
main_frame.columnconfigure(0, weight = 1)
main_frame.columnconfigure(1, weight = 1)
main_frame.columnconfigure(2, weight = 1)
main_frame.columnconfigure(3, weight = 1)

main_frame.rowconfigure(0, weight = 1)
main_frame.rowconfigure(1, weight = 1)
main_frame.rowconfigure(2, weight = 1)
main_frame.rowconfigure(3, weight = 1)
main_frame.rowconfigure(4, weight = 1)
main_frame.rowconfigure(5, weight = 1)
main_frame.rowconfigure(6, weight = 1)
main_frame.rowconfigure(7, weight = 1)

####-------------------------------- estilos label ---------------------------------------------####
estilo_label_1 = ttk.Style()
estilo_label_1.configure('label1.TLabel', font = "arial 15", anchor = "e")

estilos_label_2 = ttk.Style()
estilos_label_2.configure('label2.TLabel', font = "arial 40", anchor = "e")

####-------------------------------- estilos botones ------------------------------------------####

botones_numericos = ttk.Style()
botones_numericos.configure('botones_numericos.TButton', width = 5, font = "arial 22", relief = "flat", background = "#FFFFFF")
botones_numericos.map('botones_numericos.TButton', background = [("active","#EAEEE0")])

botones_borrar = ttk.Style()
botones_borrar.configure('botones_borrar.TButton', width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
botones_borrar.map('botones_borrar.TButton', foreground = [("active","#FF0000")], background =[("active","#858585")])

botones_restantes = ttk.Style()
botones_restantes.configure('botones_restantes.TButton', width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
botones_restantes.map('botones_restantes.TButton', background = [("active", "#858585")])

boton_igual = ttk.Style()
boton_igual.configure('boton_igual.TButton',width = 5, font = "arial 22", relief = "flat", background = "#CECECE")
boton_igual.map('boton_igual.TButton', foreground = [("active", "#70FF8B")], background = [("active", "#DADADC")])

####------------------------- pantalla calculadora -------------------------####
entrada_1 = StringVar()
label_entrada_1 = ttk.Label(main_frame, textvariable = entrada_1, style = "label1.TLabel")
label_entrada_1.grid(row = 0, column = 0, columnspan = 4, sticky = (W, N, E, S))

entrada_2 = StringVar()
label_entrada_2 = ttk.Label(main_frame, textvariable = entrada_2, style = "label2.TLabel")
label_entrada_2.grid(row = 1, column = 0, columnspan = 4, sticky = (W, N, E, S))

####-------------------------  Definicion De Botones --------------------------####
boton_0 = ttk.Button(main_frame, text = "0", style = "botones_numericos.TButton", command = lambda:inserta_valores("0"))
boton_1 = ttk.Button(main_frame, text = "1", style = "botones_numericos.TButton", command = lambda:inserta_valores("1"))
boton_2 = ttk.Button(main_frame, text = "2", style = "botones_numericos.TButton", command = lambda:inserta_valores("2"))
boton_3 = ttk.Button(main_frame, text = "3", style = "botones_numericos.TButton", command = lambda:inserta_valores("3"))
boton_4 = ttk.Button(main_frame, text = "4", style = "botones_numericos.TButton", command = lambda:inserta_valores("4"))
boton_5 = ttk.Button(main_frame, text = "5", style = "botones_numericos.TButton", command = lambda:inserta_valores("5"))
boton_6 = ttk.Button(main_frame, text = "6", style = "botones_numericos.TButton", command = lambda:inserta_valores("6"))
boton_7 = ttk.Button(main_frame, text = "7", style = "botones_numericos.TButton", command = lambda:inserta_valores("7"))
boton_8 = ttk.Button(main_frame, text = "8", style = "botones_numericos.TButton", command = lambda:inserta_valores("8"))
boton_9 = ttk.Button(main_frame, text = "9", style = "botones_numericos.TButton", command = lambda:inserta_valores("9"))

del_buttons = ttk.Button(main_frame, text = chr(9003), style = "botones_borrar.TButton", command = lambda:borrar())
boton_borrar_todo = ttk.Button(main_frame, text = "C", style = "botones_borrar.TButton", command = lambda:borrar_todo())
boton_parentesis_1 = ttk.Button(main_frame, text = "(", style = "botones_restantes.TButton", command = lambda: inserta_valores("("))
boton_parentesis_2 = ttk.Button(main_frame, text = ")", style = "botones_restantes.TButton", command = lambda: inserta_valores(")"))
boton_punto = ttk.Button(main_frame, text = ".", style = "botones_restantes.TButton", command = lambda: inserta_valores("."))
boton_punto.config(state = "disabled")

boton_suma = ttk.Button(main_frame, text = chr(43), style = "botones_restantes.TButton", command = lambda:inserta_valores("+"))
boton_suma.config(state = "disabled")
boton_resta = ttk.Button(main_frame, text = chr(8722), style = "botones_restantes.TButton", command = lambda:inserta_valores("-"))
boton_resta.config(state = "Normal")
boton_multiplicacion = ttk.Button(main_frame, text = chr(215), style = "botones_restantes.TButton", command = lambda:inserta_valores("*"))
boton_multiplicacion.config(state = "disabled")
boton_division = ttk.Button(main_frame, text = chr(247), style = "botones_restantes.TButton", command = lambda: inserta_valores("/"))
boton_division.config(state = "disabled")

boton_raiz_cuadrada = ttk.Button(main_frame, text = chr(8730), style = "botones_restantes.TButton", command = lambda: raiz_cuadrada())
boton_raiz_cuadrada.config(state = "disabled")
boton_resultado = ttk.Button(main_frame, text = chr(61), style = "boton_igual.TButton", command = lambda: inserta_valores("="))
boton_resultado.config(state = "disabled")

####-------------- botones en pantalla ---------------####
boton_parentesis_1.grid(row = 2, column = 0, sticky = (W,N,E,S))
boton_parentesis_2.grid(row = 2, column = 1, sticky = (W,N,E,S))
boton_borrar_todo.grid(row = 2, column = 2, sticky = (W,N,E,S))
del_buttons.grid(row = 2, column = 3, sticky = (W,N,E,S))

boton_7.grid(column = 0, row = 3, sticky = (W, N, E, S))
boton_8.grid(column = 1, row = 3, sticky = (W, N, E, S))
boton_9.grid(column = 2, row = 3, sticky = (W, N, E, S))
boton_division.grid(column = 3, row = 3, sticky = (W, N, E, S))

boton_4.grid(column = 0, row = 4, sticky = (W, N, E, S))
boton_5.grid(column = 1, row = 4, sticky = (W, N, E, S))
boton_6.grid(column = 2, row = 4, sticky = (W, N, E, S))
boton_multiplicacion.grid(column = 3, row = 4, sticky = (W, N, E, S))

boton_1.grid(column = 0, row = 5, sticky = (W, N, E, S))
boton_2.grid(column = 1, row = 5, sticky = (W, N, E, S))
boton_3.grid(column = 2, row = 5, sticky = (W, N, E, S))
boton_suma.grid(column = 3, row = 5, sticky = (W, N, E, S))

boton_0.grid(row = 6, column = 0, columnspan = 2, sticky = (W, N, E, S))
boton_punto.grid(row = 6, column = 2, sticky = (W, N, E, S))
boton_resta.grid(row = 6,column = 3, sticky = (W, N, E, S))

boton_resultado.grid(row = 7, column = 0, columnspan = 3, sticky = (W, N, E, S))
boton_raiz_cuadrada.grid(row = 7, column = 3 , sticky = (W, N, E, S))

####--------------- para que los botones tengan simetria ---------------####
for child in main_frame.winfo_children():
	child.grid_configure(ipady= 10, padx = 1, pady = 1) 

root.bind('<KeyPress-o>',Tema_Oscuro)
root.bind('<KeyPress-c>',Tema_Claro)	

root.mainloop()