class Cliente: #la clase clientes
    archivo = open("Clientes.txt", "a")
    def __init__(self, nombre, rut, telefono, direccion, correo):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

class tipo:
    def __init__(self, tipo):
        self.tipo = tipo

    def mostrar_tipo(self):
        if self.tipo == "1":
            print("Cliente Regular")
        elif self.tipo == "2":
            print("Cliente Premium")
        elif self.tipo == "3":
            print("Cliente Corporativo")
        else:
            print("Tipo de cliente no válido")

class registro: #comando para el boton de registro de clientes
    def registrar_cliente(self):
        self.nombre = entri_nombre.get()
        self.rut = entri_rut.get()
        self.telefono = entri_telefono.get()
        self.direccion = entri_direccion.get()
        self.correo = entri_correo.get()
        self.tipo = entri_tipo.get()
        numero = 0
        for each in self.tipo:
            if each.isdigit():
                numero += 1
        with open("Clientes.txt", "a") as archivo:
            archivo.write(f"\n{numero}{self.nombre},{self.rut},{self.telefono},{self.direccion},{self.correo},{self.tipo}\n")


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
eti_rut.place(x=330, y=10)

entri_rut = tk.Entry()
entri_rut.place(x=360, y=12)

eti_telefono = tk.Label(text = "Teléfono: ")
eti_telefono.place(x=10, y=40)

entri_telefono = tk.Entry()
entri_telefono.place(x=75, y=40)

eti_direccion = tk.Label(text = "Dirección: ")
eti_direccion.place(x=300, y=40)

entri_direccion = tk.Entry()
entri_direccion.place(x=360, y=40)

eti_correo = tk.Label(text = "Correo: ")
eti_correo.place(x=10, y=70)

entri_correo = tk.Entry()
entri_correo.place(x=75, y=70)
entri_correo.config(width=40)

tipo_cliente = tk.Label(text = '''
        ##################
        TIPO DE CLIENTE
        ##################
        1. Cliente Regular
        2. Cliente Premium
        3. Cliente Corporativo
        ''')
tipo_cliente.place(x=10, y=100)

entri_tipo = tk.Entry()
entri_tipo.place(x=170, y=170)
entri_tipo.config(width=5)

class ValueError(Exception): #excepcion para el ingreso de numeros en rut y telefono
    try: 
        entri_rut.get().isdigit()
        entri_telefono.get().isdigit()
    except ValueError:
        if not entri_rut.get().isdigit():
            raise ValueError("El RUT debe ser un número")
        if not entri_telefono.get().isdigit():
            raise ValueError("El teléfono debe ser un número")
    except ValueError as e:
        print(e)


class Mostrar: #comando para el boton de mostrar clientes
    def mostrar_clientes():
        with open("Clientes.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)


btn_registrar = tk.Button(text="Registrar Cliente", command=registro().registrar_cliente)
btn_registrar.place(x=10, y=250)

btn_mostrar = tk.Button(text="Mostrar Clientes", command=lambda: Mostrar.mostrar_clientes())
btn_mostrar.place(x=150, y=250)




ventana.mainloop()