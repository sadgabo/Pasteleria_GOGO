from tkinter import *
from tkinter.ttk import Treeview

def tree():
    
    window = Tk()
    window.withdraw()
    
    tree_screen  = Toplevel(window)
    tree_screen.title('tabla')
    tree_screen.geometry('800x500')

    
    tree_frame = LabelFrame(tree_screen, text='tabla')
    tree_frame.grid(row=1, column=0, padx=10, pady=10)
    
    tree = Treeview(tree_frame, height=10, columns=('Concepto','Fecha','Total'),show='headings')
    tree.grid(row=1, column=0, padx=10, pady=10)
    
    tree.heading('Concepto', text='Concepto', anchor=CENTER)
    tree.heading('Fecha', text='Fecha', anchor=CENTER)
    tree.heading('Total', text='Total', anchor=CENTER)

    
    Button(tree_frame, text='Borrar').grid(row=2, column=0, sticky=W+E)
    Button(tree_frame, text='Editar').grid(row=2, column=1, sticky=W+E)
    
    tree_screen.mainloop()
    
tree()

