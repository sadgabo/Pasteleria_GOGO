from tkinter import *
from tkcalendar import DateEntry

class Aplicacion:
    
    def __init__(self,window):
        self.wind = window
        self.wind.title("Pagina Principal ")
        '''self.wind.geometry('500x500')
        self.wind.resazible(False, False)
        '''
        
        
        #contenedor para los botones 

        image_frame= LabelFrame(self.wind,text='Nombre') # contenedor de la imagen , aqui pondremos el logo
        image_frame.grid(row=1,column=7,padx=20,pady=20) # colocacion del contenedor 

        self.Logo = PhotoImage(file ='GOGO.png' )#imagen, esta imagen debe estar en la misma carpeta del codigo
        #la imagen esta en un formtado de 100x141 pixels 
        Label(image_frame,image=self.Logo,bg='white').grid(row=1,column=1)#aqui se coloca y se le pone un fondo

        buton_frame = LabelFrame(self.wind,text='Actividades') #segundo contenedor donde estan alojados todos los botones
        buton_frame.grid(row= 5, column=2, columnspan=10, padx=20,pady=20)


        """
        Todos los botones , quiza falten por agregar mas o menos eso ya lo veremos despues , tanto el acomodo
        tambien puede variar, tambien hace falta agregar los comando para que nos redirigana a sus respectivas
        pantallas
        """

        Button(buton_frame,text= 'Registro de pedidos ').grid(row=1,column=0,)

        Button(buton_frame,text='Registro gastos').grid(row=1,column=2)

        Button(buton_frame,text='Ventas').grid(row=2,column=0)

        Button(buton_frame,text='Consultar pedidos').grid(row=2,column=2)

        Button(buton_frame,text='Inventario').grid(row=3,column=0)
        
        Button(buton_frame,text='Consultar gastos').grid(row=3,column=2)






if __name__ == '__main__':  #creacion de la pantalla 
    window = Tk()
    app = Aplicacion(window)
    window.mainloop()




def Order_Screen(self):
    #pantalla para registrar pedidos,primero se registraran los datos del cliente y luego los datos de los pasteles
    self.wind.withdraw()

    order_Screen = Tk.Toplevel(self.wind)
    order_Screen.title("Registro de pedidos")
    order_Screen.geometry("400x400")
    order_Screen.resazible(False,False)

    #contenedor para la informacion del cliente que sera la que se mande a la tabla cliente
    customer_container = LabelFrame(order_Screen,text='Datos del cliente')
    customer_container.grid(row=1,column=0, columnspan=10,padx=10,pady=10)

    Label(customer_container,text='Nombre').grid(row=1,column=0)
    self.Name  = Entry(customer_container)
    self.Name.grid(row=1, column=1)

    Label(customer_container, text='Telefono')
    self.Phone_Number = Entry(customer_container)
    self.Phone_Number.grid(row=2,column=1)


    #contenedor del pedido 

    Order_container = LabelFrame(self,text='Informacion del pedido')
    Order_container.grid(row=5,column=2,columnspan=10,padx=10,pady=10)


    #tipos de pasteles
    Label(Order_container,Text='Tipo de pastel').grid(row=1,column=0,padx=10,pady=10)
    self.Cake_Type = Tk.StringVar(self)
    self.Cake_Type.set('Vainilla')
    self.Cake_Options = Tk.Combobox(self,textvariable= self.Cake_Type,values=['Vainilla','Zanahoria', 'Chocolate', 'Tres leches'] )
    self.Cake_Options.grid(row=2,column=1,padx=10,pady=10)


    # Cantida de personas
    Label(Order_container,text='Numero de personas').grid(row=3,column=0,padx=10,pady=10)
    self.Cant_Pers = Tk.StringVar(self)
    self.Cant_Pers.set('20')
    self.Cant_Options = Tk.Combobox(self,textvariable=self.Cant_Options,values=['20','30','50'])
    self.Cant_Options.grid(row=3,column=1,padx=10,pady=10)


    #Fecha de entrega

    Label(order_Screen,text="Fecha de entrega").grid(row=4,column=0,padx=20,pady=20)
    self.date_entry = DateEntry(Order_container,date_pattern = "dd/mm/yyyy")
    self.date_entry.grid(row=4, column= 1,padx=20,pady=20)


    #contenedor de los extras y notas 

    Extras_Container = LabelFrame(order_Screen,text='Extras')
    Extras_Container.grid(row=9,column=1,padx=20,pady=20)

    #Botones para añadir los extras que sean necesarios

    Button(Extras_Container,text='+').grid(row=1,column=0,padx=20,pady=20)
    Label(Extras_Container,text='Bettun extra').grid(row=1,column=1,padx=20,pad=20)


    #input para notas
    Label(Extras_Container,text='Notas').grid(row=6,column=0,padx=20,pady=20)
    self.notes_entry= Entry(Extras_Container)
    self.notes_entry.grid(row=7,column=0,padx=20,pady=20)

