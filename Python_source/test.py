import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Creamos el objeto Treeview
table = ttk.Treeview(root, columns=("column1", "column2", "column3"), show="headings")

# Agregamos los encabezados de las columnas
table.heading("column1", text="Columna 1")
table.heading("column2", text="Columna 2")
table.heading("column3", text="Columna 3")

# Agregamos los datos a la tabla
table.insert("", tk.END, values=("Dato 1", "Dato 2", "Dato 3"))
table.insert("", tk.END, values=("Dato 4", "Dato 5", "Dato 6"))

# Empaquetamos la tabla en la ventana
table.pack()

root.mainloop()
