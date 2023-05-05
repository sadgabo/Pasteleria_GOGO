from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
from tkcalendar import DateEntry

#from Handlers.Pedido import Pedido_nuevo
#from Handlers.Pedido import cliente_nuevo



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

    Button(buton_frame,text='Registro gastos',command=expenses_register).grid(row=1,column=2)

    Button(buton_frame,text='Ventas',command=sales_consult).grid(row=2,column=0)

    Button(buton_frame,text='Consultar pedidos',command=Consult_Orders).grid(row=2,column=2)

    Button(buton_frame,text='Inventario',command= Inventario).grid(row=3,column=0)
    
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
    Nombre_Entry = Entry(customer_container)
    Nombre_Entry.grid(row=1, column=1)
    

    Label(customer_container, text='Telefono').grid(row=2,column=0)
    Phone_Entry = Entry(customer_container)
    Phone_Entry.grid(row=2,column=1)
    
    Name = Nombre_Entry.get()
    Phone = Phone_Entry.get()

    #contenedor del pedido 

    Order_container = LabelFrame(order_Screen,text='Informacion del pedido')
    Order_container.grid(row=4,column= 0,padx=10,pady=10)


    #tipos de pasteles
    Label(Order_container,text='Tipo de pastel').grid(row=1,column=0,padx=10,pady=10)
    Cake_type = StringVar(Order_container)
    Cake_type.set('Vainilla')
    Cake_Options = Combobox(Order_container,textvariable= Cake_type,values=['Tres leches','Chocolate','Volteado','Red velvet','Zanahoria'])
    Cake_Options.grid(row=1, column=1,padx=10,pady=10)
    cake = Cake_Options.get()


    Label(Order_container,text='Numero de personas').grid(row=2,column=0,padx=10,pady=10)
    Cant_Pers = StringVar(Order_container)
    Cant_Pers.set('20')
    Cant_Options = Combobox(Order_container,textvariable= Cant_Pers,values= ['20','30','50'] )
    Cant_Options.grid(row=2,column = 1,padx=10,pady=10)
    Personas = Cant_Options.get()

    
    Label(Order_container,text='Fecha de entrega').grid(row=3,column=0,padx=10,pady=10)
    Date_entry = DateEntry(Order_container)
    Date_entry.grid(row=3,column= 1,padx=10,pady=10)
    date = Date_entry.get()


    Label(Order_container,text='Bettun extra').grid(row=4,column=0,padx=10,pady=10)
    betun_extra = StringVar(Order_container)
    betun_extra.set('Si')
    betun_options = Combobox(Order_container,textvariable=betun_extra,values=['Si','No'])
    betun_options.grid(row=4,column=1,padx=10,pady=10)
    betun = betun_options.get()


    Label(Order_container,text='Notas').grid(row=5,column=0,padx=10,pady=10)
    Notes_entry = Entry(Order_container)
    Notes_entry.grid(row=5, column=1,padx=10,pady=10)
    Notes = Notes_entry.get()

    Button(Order_container,text='Realizar pedido',command=Send_Order(Name,Phone)).grid(row=10,padx=10,pady=10)
    

def Send_Order(name: str,phone: str):
    #cliente_nuevo(name,phone)
    #Pedido_nuevo(cake,pers,date,betun,notes)
    print(f"NOMBRE: {name}")
    print(f"TELEFONO: {phone}")


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
    
    
def Inventario():
    window = Tk()
    window.withdraw()
    ws = Toplevel(window)
    ws.title('Insumos')
    ws.geometry('500x500')
    ws['bg'] = '#AC99F2'


    Inventario = LabelFrame(ws,text='Inventario')
    Inventario.grid(row=1,column=0,padx=10,pady=10)
    
    my_game = Treeview(Inventario)
    my_game.grid(row=1,column=0,padx=10,pady=10)
    
    my_game['columns'] = ('Material', 'Cantidad', 'Medidas', 'Costos')

    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Material",anchor=CENTER, width=80)
    my_game.column("Cantidad",anchor=CENTER,width=80)
    my_game.column("Medidas",anchor=CENTER,width=80)
    my_game.column("Costos",anchor=CENTER,width=80)


    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("Material",text="Insumo",anchor=CENTER)
    my_game.heading("Cantidad",text="Cantidad",anchor=CENTER)
    my_game.heading("Medidas",text="Medidas",anchor=CENTER)
    my_game.heading("Costos",text="Costo",anchor=CENTER)

    my_game.insert(parent='',index='end',iid=0,text='',
    values=('Harina','44000','gramos','841'))

    my_game.insert(parent='',index='end',iid=1,text='',
    values=('Mantequilla','1000','gramos','62'))

    my_game.insert(parent='',index='end',iid=2,text='',
    values=('Azucar','10000','gramos','273'))

    my_game.insert(parent='',index='end',iid=3,text='',
    values=('Huevos','12','Piezas','40'))

    my_game.insert(parent='',index='end',iid=4,text='',
    values=('Leche','3000','mililitros','43.5'))

    my_game.insert(parent='',index='end',iid=5,text='',
    values=('Polvo para hornear','1000','gramos','20'))

    my_game.insert(parent='',index='end',iid=6,text='',
    values=('Vainilla','1000','mililitros','89'))


    my_game.insert(parent='',index='end',iid=7,text='',
    values=('Cocoa','2500','gramos','226'))

    my_game.insert(parent='',index='end',iid=8,text='',
    values=('Chocolate','2500','gramos','280'))


    my_game.insert(parent='',index='end',iid=9,text='',
    values=('Aceite','946','mililitros','55'))

    my_game.insert(parent='',index='end',iid=10,text='',
    values=('Bicarbonato','1000','gramos','12'))

    my_game.insert(parent='',index='end',iid=11,text='',
    values=('Vinagre','1000','mililitros','17'))

    my_game.insert(parent='',index='end',iid=12,text='',
    values=('Limon','20','piezas','18'))

    my_game.insert(parent='',index='end',iid=13,text='',
    values=('Agua','19000','mililitros','40'))

    my_game.insert(parent='',index='end',iid=14,text='',
    values=('Azucar Moscabado','10000','gramos','220'))

    my_game.insert(parent='',index='end',iid=15,text='',
    values=('Zanahoria','1000','gramos','10'))

    my_game.insert(parent='',index='end',iid=16,text='',
    values=('Canela en Polvo','50','gramos','15'))

    my_game.insert(parent='',index='end',iid=17,text='',
    values=('Nuez moscabado','50','gramos','30'))

    my_game.insert(parent='',index='end',iid=18,text='',
    values=('Jengibre','50','gramos','26'))

    my_game.insert(parent='',index='end',iid=19,text='',
    values=('Clavo','50','gramos','20'))

    my_game.insert(parent='',index='end',iid=20,text='',
    values=('Nuez','1000','gramos','350'))

    my_game.insert(parent='',index='end',iid=21,text='',
    values=('Queso Crema','180','gramos','38.5'))

    my_game.insert(parent='',index='end',iid=22,text='',
    values=('Azucar Glass','500','gramos','15.5'))

    my_game.insert(parent='',index='end',iid=23,text='',
    values=('Manteca vegetal','1000','gramos','82'))

    my_game.insert(parent='',index='end',iid=24,text='',
    values=('Merengue en polvo','250','gramos','139'))

    my_game.insert(parent='',index='end',iid=25,text='',
    values=('Vainilla','150','mililitros','14.5'))

    my_game.insert(parent='',index='end',iid=26,text='',
    values=('Leche en polvo','460','gramos','63'))

    Button(Inventario,text='Regresar',command=main_screen).grid(row=8,column=1,padx=10,pady=10)
        
        
        
        
def expenses_register():
    window = Tk()
    window.withdraw()
    
    
    expenses_window = Toplevel()
    expenses_window.title('Registro de pedidos')
    expenses_window.geometry('600x600')
    expenses_window.resizable(False,False)
    
    
    expense_container = LabelFrame(expenses_window,text='Registro de gastos')
    expense_container.grid(row=1,column=1,padx=10,pady=10)
    
    Label(expense_container,text='Concepto ').grid(row=1,column=0,padx=10,pady=10)
    concept = Entry(expense_container)
    concept.grid(row=1,column=1,padx=10,pady=10)
    
    Label(expense_container,text='Fecha de Gasto').grid(row=2,column=0,padx=10,pady=10)
    Date_entry = DateEntry(expense_container)
    Date_entry.grid(row=2,column= 1,padx=10,pady=10)
    
    Label(expense_container,text='Total comprado').grid(row=3,column=0,padx=10,pady=10)
    total = Entry(expense_container)
    total.grid(row=3,column=1,padx=10,pady=10)
    
    Button(expense_container,text='Ingresar gasto').grid(row=4,column=0,padx=10,pady=10)
    
    Button(expense_container,text='Regresar').grid(row=4,column=1,padx=10,pady=10)
    
    
    

main_screen()


