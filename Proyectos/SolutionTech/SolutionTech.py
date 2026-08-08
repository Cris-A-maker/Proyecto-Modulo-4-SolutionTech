class Cliente:
    def __init__(self, nombre, apellido, rut, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.telefono = telefono
        self.direccion = direccion

    def tipo_cliente(self):
        print('''
        ##################
        TIPO DE CLIENTE
        ##################
        1. Cliente Regular
        2. Cliente Premium
        3. Cliente Corporativo
        ''')
        tipo = input("Que tipo de cliente es?: ")
        return tipo


import tkinter as tk #preparando la ventana tk
ventana = tk.Tk()
ventana.title("Control de Clientes")





ventana.mainloop()