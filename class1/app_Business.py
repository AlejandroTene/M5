from laptop_business import Laptop_Business
import tkinter as tk
from tkinter import ttk


class app:
    def __init__(self,root):
        self.root=root
        self.laptops = []
        root.title("Ingresar Datos - Laptops Business")
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root,text="Marca").grid(row=0,column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)

        ttk.Label(self.root,text="Procesador").grid(row=1,column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)

        ttk.Label(self.root,text="Memoria").grid(row=2,column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1)

        ttk.Label(self.root,text="Almacenamiento").grid(row=3,column=0)
        self.almacenamento = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.almacenamento).grid(row=3,column=1)

        ttk.Label(self.root,text="Duración bateria").grid(row=4,column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.duracion_bateria).grid(row=4,column=1)

        ttk.Label(self.root,text="Precio").grid(row=5,column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.precio).grid(row=5,column=1)

        ttk.Button(self.root,text="Agregar Laptop",command=self.agregar_laptop).grid(row=6,column=0)

        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=7,column=0,columnspan=2)


    def agregar_laptop(self):
        nueva_laptop = Laptop_Business(self.marca.get(),self.procesador.get(),self.memoria.get(),self.almacenamento.get(),self.duracion_bateria.get(),self.precio.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")

        pass



root = tk.Tk()

app =app(root)
root.mainloop()