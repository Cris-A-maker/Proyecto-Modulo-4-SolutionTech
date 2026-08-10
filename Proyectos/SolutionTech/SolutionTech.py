import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

ARCHIVO = "Clientes.txt"


class Cliente:  # la clase clientes
    def _init_(self, nombre, rut, telefono, direccion, correo, tipo):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.tipo = tipo

    def a_linea(self):
        return f"{self.rut},{self.nombre},{self.telefono},{self.direccion},{self.correo},{self.tipo}"


class Tipo:  # sub clase de tipo de cliente
    DESCRIPCIONES = {
        "1": "Cliente Regular",
        "2": "Cliente Premium",
        "3": "Cliente Corporativo",
    }

    def _init_(self, tipo):
        self.tipo = tipo

    def mostrar_tipo(self):
        return self.DESCRIPCIONES.get(self.tipo, "Tipo de cliente no válido")


def validar_formulario(nombre, rut, telefono, correo, tipo):
    #Devuelve un mensaje de error, o None si los datos son válidos
    if not nombre or not rut:
        return "El nombre y el RUT son obligatorios."
    if not rut.isdigit():
        return "El RUT debe contener solo números."
    if not telefono.isdigit():
        return "El teléfono debe contener solo números."
    if "@" not in correo:
        return "Ingrese un correo válido."
    if tipo not in ("1", "2", "3"):
        return "El tipo de cliente debe ser 1, 2 o 3."
    return None


def leer_clientes():
    clientes = []
    if not os.path.exists(ARCHIVO):
        return clientes
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            if len(partes) == 6:
                rut, nombre, telefono, direccion, correo, tipo = partes
                clientes.append(Cliente(nombre, rut, telefono, direccion, correo, tipo))
    return clientes


def escribir_clientes(clientes):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for c in clientes:
            archivo.write(c.a_linea() + "\n")


def limpiar_campos():
    for entrada in (entri_nombre, entri_rut, entri_telefono, entri_direccion, entri_correo, entri_tipo):
        entrada.delete(0, tk.END)


class Registro:  # comando para el boton de registro de clientes
    def registrar_cliente(self):
        nombre = entri_nombre.get().strip()
        rut = entri_rut.get().strip()
        telefono = entri_telefono.get().strip()
        direccion = entri_direccion.get().strip()
        correo = entri_correo.get().strip()
        tipo = entri_tipo.get().strip()

        error = validar_formulario(nombre, rut, telefono, correo, tipo)
        if error:
            messagebox.showerror("Datos inválidos", error)
            return

        clientes = leer_clientes()
        nuevo = Cliente(nombre, rut, telefono, direccion, correo, tipo)

        # Si el RUT ya existe, actualizamos en vez de duplicar (esto habilita "editar")
        for i, c in enumerate(clientes):
            if c.rut == rut:
                clientes[i] = nuevo
                escribir_clientes(clientes)
                messagebox.showinfo("Actualizado", f"Se actualizaron los datos de {nombre}.")
                limpiar_campos()
                return

        clientes.append(nuevo)
        escribir_clientes(clientes)
        messagebox.showinfo("Registrado", f"{nombre} fue registrado como {Tipo(tipo).mostrar_tipo()}.")
        limpiar_campos()


class Buscar:  # comando para el boton de buscar / editar clientes
    def buscar_cliente(self):
        rut_buscar = entri_rut.get().strip()
        if not rut_buscar:
            messagebox.showwarning("RUT requerido", "Ingrese un RUT en el campo correspondiente para buscar.")
            return

        for c in leer_clientes():
            if c.rut == rut_buscar:
                entri_nombre.delete(0, tk.END); entri_nombre.insert(0, c.nombre)
                entri_telefono.delete(0, tk.END); entri_telefono.insert(0, c.telefono)
                entri_direccion.delete(0, tk.END); entri_direccion.insert(0, c.direccion)
                entri_correo.delete(0, tk.END); entri_correo.insert(0, c.correo)
                entri_tipo.delete(0, tk.END); entri_tipo.insert(0, c.tipo)
                messagebox.showinfo(
                    "Cliente encontrado",
                    f"{c.nombre} ({Tipo(c.tipo).mostrar_tipo()})\n\n"
                    "Sus datos se cargaron en el formulario.\n"
                    "Puede modificarlos y presionar 'Registrar Cliente' para guardar los cambios."
                )
                return
        messagebox.showwarning("No encontrado", f"No existe un cliente con RUT {rut_buscar}.")


class Eliminar:  # comando para el boton de eliminar clientes
    def eliminar_cliente(self):
        rut = entri_rut.get().strip()
        if not rut:
            messagebox.showwarning("RUT requerido", "Ingrese un RUT en el campo correspondiente para eliminar.")
            return

        clientes = leer_clientes()
        restantes = [c for c in clientes if c.rut != rut]

        if len(restantes) == len(clientes):
            messagebox.showwarning("No encontrado", f"No existe un cliente con RUT {rut}.")
            return

        if messagebox.askyesno("Confirmar eliminación", f"¿Eliminar al cliente con RUT {rut}?"):
            escribir_clientes(restantes)
            messagebox.showinfo("Eliminado", "El cliente fue eliminado correctamente.")
            limpiar_campos()


class Mostrar:  # comando para el boton de mostrar clientes
    def mostrar_clientes(self):
        clientes = leer_clientes()
        ventana_lista = tk.Toplevel(ventana)
        ventana_lista.title("Listado de Clientes")
        ventana_lista.geometry("600x400")
        
        def __str__(self):
            return(
            f"Nombre: {self.nombre}\n"
            f"RUT: {self.rut}\n"
            f"Telefono: {self.telefono}\n"
            f"Direccion: {self.direccion}\n"
            f"Correo: {self.correo}\n"
            f"Tipo: {Tipo(self.tipo).mostrar_tipo()}\n"
            )

        texto = scrolledtext.ScrolledText(ventana_lista, width=70, height=20)
        texto.pack(padx=10, pady=10, fill="both", expand=True)

        if not clientes:
            texto.insert(tk.END, "No hay clientes registrados.")
        else:
            for c in clientes:
                texto.insert(
                    tk.END,
                    f"Nombre: {c.nombre}\n"
                    f"RUT: {c.rut}\n"
                    f"Teléfono: {c.telefono}\n"
                    f"Dirección: {c.direccion}\n"
                    f"Correo: {c.correo}\n"
                    f"Tipo: {Tipo(c.tipo).mostrar_tipo()}\n"
                    f"{'-' * 40}\n"
                )

        texto.config(state="disabled")


# ---------- Interfaz gráfica ----------
ventana = tk.Tk()
ventana.config(width=800, height=600)
ventana.title("Control de Clientes")

eti_nombre = tk.Label(text="Nombre: ")
eti_nombre.place(x=10, y=10)
entri_nombre = tk.Entry(width=40)
entri_nombre.place(x=75, y=12)


eti_rut = tk.Label(text="RUT: ")
eti_rut.place(x=330, y=10)

entri_rut = tk.Entry()
entri_rut.place(x=360, y=12)

eti_telefono = tk.Label(text="Teléfono: ")
eti_telefono.place(x=10, y=40)

entri_telefono = tk.Entry()
entri_telefono.place(x=75, y=40)

eti_direccion = tk.Label(text="Dirección: ")
eti_direccion.place(x=300, y=40)

entri_direccion = tk.Entry()
entri_direccion.place(x=360, y=40)

eti_correo = tk.Label(text="Correo: ")
eti_correo.place(x=10, y=70)

entri_correo = tk.Entry(width=40)
entri_correo.place(x=75, y=70)


tipo_cliente = tk.Label(text='''
        ##################
        TIPO DE CLIENTE
        ##################
        1. Cliente Regular
        2. Cliente Premium
        3. Cliente Corporativo
        ''')
tipo_cliente.place(x=10, y=100)

entri_tipo = tk.Entry(width=5)
entri_tipo.place(x=170, y=170)

btn_registrar = tk.Button(text="Registrar Cliente", command=Registro().registrar_cliente)
btn_registrar.place(x=10, y=250)

btn_mostrar = tk.Button(text="Mostrar Clientes", command=Mostrar().mostrar_clientes)
btn_mostrar.place(x=150, y=250)

btn_buscar = tk.Button(text="Buscar / Editar Cliente", command=Buscar().buscar_cliente)
btn_buscar.place(x=300, y=250)

btn_eliminar = tk.Button(text="Eliminar Cliente", command=Eliminar().eliminar_cliente)
btn_eliminar.place(x=480, y=250)

btn_limpiar = tk.Button(text="Limpiar Campos", command=limpiar_campos)
btn_limpiar.place(x=620, y=250)

ventana.mainloop()