class Cliente:
    archivo = open("clientes.txt", "a")
    def __init__(self, nombre, rut, telefono, direccion, correo):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo


    def registrar_cliente(self):
        self.nombre = entri_nombre.get()
        self.rut = entri_rut.get()
        self.telefono = entri_telefono.get()
        self.direccion = entri_direccion.get()
        self.correo = entri_correo.get()
        with open("clientes.txt", "a") as archivo:
            archivo.write(f"\n{self.nombre},{self.rut},{self.telefono},{self.direccion},{self.correo}\n")


import tkinter as tk #preparando la ventana tk
ventana = tk.Tk()
ventana.config(width=800, height=600)
ventana.title("Control de Clientes")

eti_nombre = tk.Label(text = "Nombre: ") #preparando el ingreso de datos
eti_nombre.place(x=10, y=10)

entri_nombre = tk.Entry()
entri_nombre.place(x=75, y=12)
entri_nombre.config(width=40)

eti_rut = tk.Label(text = "RUT: ")
eti_rut.place(x=10, y=40)

entri_rut = tk.Entry()
entri_rut.place(x=75, y=42)

eti_telefono = tk.Label(text = "Teléfono: ")
eti_telefono.place(x=10, y=70)

entri_telefono = tk.Entry()
entri_telefono.place(x=75, y=72)

eti_direccion = tk.Label(text = "Dirección: ")
eti_direccion.place(x=10, y=100)

entri_direccion = tk.Entry()
entri_direccion.place(x=75, y=102)

tipo_cliente = tk.Label(text = '''
        ##################
        TIPO DE CLIENTE
        ##################
        1. Cliente Regular
        2. Cliente Premium
        3. Cliente Corporativo
        ''')
tipo_cliente.place(x=10, y=130)

entri_tipo = tk.Entry()
entri_tipo.place(x=37, y=250)

eti_correo = tk.Label(text = "Correo: ")
eti_correo.place(x=10, y=160)

entri_correo = tk.Entry()
entri_correo.place(x=75, y=162)


boton = tk.Button(text="Registrar Cliente", command=Cliente.registrar_cliente)
boton.place(x=10, y=300)





ventana.mainloop()