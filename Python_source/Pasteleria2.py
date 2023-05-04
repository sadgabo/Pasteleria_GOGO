from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
from tkcalendar import DateEntry



def main_screen():
    #creacion de la pantalla principal 
    window = Tk()
    window.withdraw()

    main_screen = Toplevel(window)
    main_screen.title("Registro de pedidos")
    main_screen.geometry("400x400")
    main_screen.resizable(False,False)
    
    #contenedor para los botones 

    image_frame= LabelFrame(main_screen,text='Nombre') # contenedor de la imagen , aqui pondremos el logo
    image_frame.grid(row=1,column=7,padx=20,pady=20) # colocacion del contenedor 

    Logo = PhotoImage(file ='GOGO.png' )#imagen, esta imagen debe estar en la misma carpeta del codigo
    #la imagen esta en un formtado de 100x141 pixels 
    Label(image_frame,image=Logo,bg='white').grid(row=1,column=1)#aqui se coloca y se le pone un fondo

    buton_frame = LabelFrame(main_screen,text='Actividades') #segundo contenedor donde estan alojados todos los botones
    buton_frame.grid(row= 5, column=2, columnspan=10, padx=20,pady=20)


    """
    Todos los botones , quiza falten por agregar mas o menos eso ya lo veremos despues , tanto el acomodo
    tambien puede variar, tambien hace falta agregar los comando para que nos redirigana a sus respectivas
    pantallas
    """

    Button(buton_frame,text= 'Registro de pedidos ', command=Order_Screen).grid(row=1,column=0,)

    Button(buton_frame,text='Registro gastos').grid(row=1,column=2)

    Button(buton_frame,text='Ventas',command=sales_consult).grid(row=2,column=0)

    Button(buton_frame,text='Consultar pedidos',command=Consult_Orders).grid(row=2,column=2)

    Button(buton_frame,text='Inventario').grid(row=3,column=0)
    
    Button(buton_frame,text='Consultar gastos',command=expenses_consult).grid(row=3,column=2)

    window.mainloop()

def Order_Screen():
    #pantalla para registrar pedidos,primero se registraran los datos del cliente y luego los datos de los pasteles
    window = Tk()
    window.withdraw()

    order_Screen = Toplevel(window)
    order_Screen.title("Registro de pedidos")
    order_Screen.geometry("400x400")
    order_Screen.resizable(False,False)

    #contenedor para la informacion del cliente que sera la que se mande a la tabla cliente
    customer_container = LabelFrame(order_Screen,text='Datos del cliente')
    customer_container.grid(row=1,column=0, columnspan=10,padx=10,pady=10)

    Label(customer_container,text='Nombre').grid(row=1,column=0)
    Entry(customer_container).grid(row=1, column=1)
    

    Label(customer_container, text='Telefono').grid(row=2,column=0)
    Phone_Number = Entry(customer_container)
    Phone_Number.grid(row=2,column=1)

    #contenedor del pedido 

    Order_container = LabelFrame(order_Screen,text='Informacion del pedido')
    Order_container.grid(row=4,column= 0,padx=10,pady=10)


    #tipos de pasteles
    Label(Order_container,text='Tipo de pastel').grid(row=1,column=0,padx=10,pady=10)
    Cake_type = StringVar(Order_container)
    Cake_type.set('Vainilla')
    Cake_Options = Combobox(Order_container,textvariable= Cake_type,values=['Tres leches','Chocolate','Volteado','Red velvet','Zanahoria'])
    Cake_Options.grid(row=1, column=1,padx=10,pady=10)


    Label(Order_container,text='Numero de personas').grid(row=2,column=0,padx=10,pady=10)
    Cant_Pers = StringVar(Order_container)
    Cant_Pers.set('20')
    Cant_Options = Combobox(Order_container,textvariable= Cant_Pers,values= ['20','30','50'] )
    Cant_Options.grid(row=2,column = 1,padx=10,pady=10)


    
    Label(Order_container,text='Fecha de entrega').grid(row=3,column=0,padx=10,pady=10)
    Date_entry = DateEntry(Order_container)
    


    Button(Order_container,text='+').grid(row=4,column=0,padx=10,pady=10)
    Label(Order_container,text='Bettun extra').grid(row=4,column=1,padx=10,pady=10)


    Label(Order_container,text='Notas').grid(row=5,column=0,padx=10,pady=10)
    Notes_entry = Entry(Order_container)
    Notes_entry.grid(row=5, column=1,padx=10,pady=10)
    



    Button(Order_container,text='Realizar pedido').grid(row=10,column=1,padx=10,pady=10)
    


def Consult_Orders():

    window = Tk()
    window.withdraw()

    Consult_Screen = Toplevel(window)
    Consult_Screen.title("Consulta de pedidos")
    Consult_Screen.geometry("1000x600")
    Consult_Screen.resizable(False,False)

    Consult = LabelFrame(Consult_Screen,text='Pedidos pendientes')
    Consult.grid(row=1,column=0)


    Label(Consult,text='Mes').grid(row=1,column=0,padx=10,pady=10)
    months = StringVar(Consult)
    months.set('Enero')
    months_options = Combobox(Consult,textvariable=months,values=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])
    months_options.grid(row=1,column=1,padx=10,pady=10)

    Button(Consult,text='Buscar').grid(row=1,column=2,padx=10,pady=10)

    orders_frame = LabelFrame(Consult_Screen,text='Pedidos')
    orders_frame.grid(row=2,column=0,padx=10,pady=10)

    orders = Treeview(orders_frame,columns=("column1","column2","column3","column4","column5"),show="headings")
    orders.grid(row=2,column=0,columnspan=3)

    orders.heading("column1",text='Fecha de entrega')
    orders.heading("column2",text='Pastel ')
    orders.heading("column3",text='Numero de personas')
    orders.heading("column4",text="Liquidar")
    orders.heading("column5",text="Realizar cambios")
    
    
    Button(orders_frame,text='Regresar').grid(row=5,column=2,padx=10,pady=10)



def sales_consult():
    window = Tk()
    window.withdraw()
    
    sales_screen = Toplevel(window)
    sales_screen.title("VENTAS")
    sales_screen.geometry("800x600")
    sales_screen.resizable(False,False)
    
    contenedorVenta = LabelFrame(sales_screen,text="Consulta")
    contenedorVenta.grid(row=1,column=0)
    
    Label(contenedorVenta,text='Mes').grid(row=1,column=0,padx=10,pady=10)
    months = StringVar(contenedorVenta)
    months.set('Enero')
    months_options = Combobox(contenedorVenta,textvariable=months,values=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])
    months_options.grid(row=1,column=1,padx=10,pady=10)

    Button(contenedorVenta,text='Buscar').grid(row=1,column=2,padx=10,pady=10)

    tabla = LabelFrame(sales_screen,text="Ventas")
    tabla.grid(row=2,column=0,padx=10,pady=10)
    
    ventas = Treeview(tabla,columns=("column1","column2","column3"),show="headings")
    ventas.grid(row=2,column=0,columnspan=3)
    
    ventas.heading("column1",text='Fecha')
    ventas.heading("column2",text='Monto')
    ventas.heading("column3",text='Informacion')
    
    
    
def expenses_consult():
    window = Tk()
    window.withdraw()
    
    sales_screen = Toplevel(window)
    sales_screen.title("Gastos")
    sales_screen.geometry("900x600")
    sales_screen.resizable(False,False)
    
    contenedorGasto = LabelFrame(sales_screen,text="Consulta")
    contenedorGasto.grid(row=1,column=0)
    
    Label(contenedorGasto,text='Mes').grid(row=1,column=0,padx=10,pady=10)
    months = StringVar(contenedorGasto)
    months.set('Enero')
    months_options = Combobox(contenedorGasto,textvariable=months,values=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])
    months_options.grid(row=1,column=1,padx=10,pady=10)

    Button(contenedorGasto,text='Buscar').grid(row=1,column=2,padx=10,pady=10)

    tabla = LabelFrame(sales_screen,text='Gastos')
    tabla.grid(row=2,column=0,padx=10,pady=10)
    
    #concepto, fecha , total  
    gastos =  Treeview(tabla,columns= ("column1","column2","column3"))
    gastos.grid(row=2,column=0,columnspan=3)
    
    gastos.heading("column1",text='Concepto')
    gastos.heading("column2",text='Fecha')
    gastos.heading("column3",text='Total')
    
    

main_screen()


