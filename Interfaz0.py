# -*- coding: utf-8 -*-
# import sys
from Tkinter import *
import ttk
# import tkSimpleDialog
# import tkMessageBox

# Inicializar banderas
start_calcs = 0


def actualizar():
    start_calcs = 1
    App.update()
    return start_calcs

App = Tk()
App.geometry("1700x600+-10+20")
App.title("Interfaz gráfica")
print "start_calcs es: ", start_calcs
if start_calcs == 0:
    Argumentos = ['Optimizar', 'Jdomax', 'Jrmax']
# primer_Argumento='Optimizar'
# segundo_Argumento='Jdomax'
# tercer_Argumento='Jrmax'

# Var declaration
label_x_init = 120
label_y_init = 150
label_x_offset = 0
box_x_init = 185
box_y_init = 150
box_y_offset = 45
box_x_offset = 270


# Declaration of labels for first column
Label(App, justify=RIGHT, text="T:\n\n\na:\n\n\nK:\n\n\nL:\n\n\n" + Argumentos[0] + ":\n\n\n" +
                               Argumentos[1] + ":\n\n\n" + Argumentos[2] + ":\n\n\nMs:").\
    grid(row=0, column=0, padx=label_x_init, pady=label_y_init)

# Declaration of labels for second column
Label(App, justify=RIGHT, text="Kc:\n\n\nTi:\n\n\nTd:\n\n\nβ:\n\n\n\n\n\n\n\n\nα:\n\n\nγ:"
      ).grid(row=0, column=1, padx=label_x_init+label_x_offset, pady=label_y_init)

# Declaration of labels for third column
Label(App, justify=RIGHT, text="Time:\n\n\nr:\n\n\ndi_magnitude:\n\n\ndi_time:\n\n\nndo_magnitude:\n\n\n"
                               "do_time:").grid(row=0, column=2, padx=label_x_init+label_x_offset, pady=label_y_init)

# Aquí hay que mejorar los datos. Tengo que poner al final de cada cajita las unidades en las que se aceptan los datos

# Define text spaces and var get() for first column
button_T = Entry(App)
button_T.grid(row=0, column=1)
button_T.place(x=box_x_init, y=box_y_init)

button_a = Entry(App)
button_a.grid(row=1, column=1)
button_a.place(x=box_x_init, y=box_y_init+box_y_offset)


button_K = Entry(App)
button_K.grid(row=2, column=1)
button_K.place(x=box_x_init, y=box_y_init+2*box_y_offset)

button_L = Entry(App)
button_L.grid(row=3, column=1)
button_L.place(x=box_x_init, y=box_y_init+3*box_y_offset)

# Define Combobox for Ms values
menu_Optimizar = ttk.Combobox(App, values=["Jdimax", "Jdomax", "Jrmax"])
menu_Optimizar.grid(row=4, column=1)
menu_Optimizar.place(x=box_x_init, y=box_y_init+4*box_y_offset)
menu_Optimizar.set("Jdimax")
menu_Optimizar.configure(width=17)

if menu_Optimizar.current() == 0:
    Argumentos[1] = 'Jdomax'
    Argumentos[2] = 'Jrmax'
elif menu_Optimizar.current() == 1:
    Argumentos[1] = 'Jdimax'
    Argumentos[2] = 'Jrmax'
elif menu_Optimizar.current() == 2:
    Argumentos[1] = 'Jdimax'
    Argumentos[2] = 'Jdomax'
# Para obtener el valor actual

#print menu_Optimizar.current()

# button_Jdimax = Entry(App)
# button_Jdimax.grid(row=4, column=1)
# button_Jdimax.place(x=box_x_init, y=box_y_init+4*box_y_offset)

button_Jdomax = Entry(App)
button_Jdomax.grid(row=5, column=1)
button_Jdomax.place(x=box_x_init, y=box_y_init+5*box_y_offset)

button_Jdrmax = Entry(App)
button_Jdrmax.grid(row=6, column=1)
button_Jdrmax.place(x=box_x_init, y=box_y_init+6*box_y_offset)

# Define Combobox for Ms values
menu_Ms = ttk.Combobox(App, values=["2.0", "1.8", "1.6"])
menu_Ms.grid(row=7, column=1)
menu_Ms.place(x=box_x_init, y=box_y_init+7*box_y_offset)
menu_Ms.set("2.0")
menu_Ms.configure(width=17)

# Define space for output in the second column
button_Kc = Label(App, text="valor1")
button_Kc.grid(row=0, column=2)
button_Kc.place(bordermode=INSIDE, height=20, width=50, x=box_x_init+box_x_offset, y=box_y_init)

button_Ti = Label(App, text="valor2")
button_Ti.grid(row=1, column=2)
button_Ti.place(bordermode=INSIDE, height=20, width=50, x=box_x_init+box_x_offset, y=box_y_init+box_y_offset)

button_Td = Label(App, text="valor2")
button_Td.grid(row=2, column=2)
button_Td.place(bordermode=INSIDE, height=20, width=50, x=box_x_init+box_x_offset, y=box_y_init+2*box_y_offset)

button_beta = Label(App, text="valor2")
button_beta.grid(row=3, column=2)
button_beta.place(bordermode=INSIDE, height=20, width=50, x=box_x_init+box_x_offset, y=box_y_init+3*box_y_offset)

button_alpha = Entry(App)
button_alpha.grid(row=6, column=2)
button_alpha.place(x=box_x_init+box_x_offset, y=box_y_init+6*box_y_offset)

button_gamma = Entry(App)
button_gamma.grid(row=7, column=2)
button_gamma.place(x=box_x_init+box_x_offset, y=box_y_init+7*box_y_offset)

activate_button = Button(App, text="Toca para actualizar", width=20, command=actualizar)
activate_button.grid(row=0, column=5)

App.mainloop()
