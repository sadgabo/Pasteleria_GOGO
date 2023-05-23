from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import tkinter.font as tkFont
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import messagebox

import pymysql


from Handlers.Pedido import *
from Handlers.Clientes import *
from Handlers.Gasto import *
from Handlers.Ventas import *
from Handlers.Inventario import *
global monto 
monto : str = ''


def main_screen():
    # Creación de la pantalla principal
    window = Tk()
    window.withdraw()

    main_screen = Toplevel(window)
    main_screen.title("Pagina Principal")
    main_screen.geometry("500x500")
    main_screen.resizable(False, False)
    main_screen.configure(bg="#FFB6C1")  # Configuración del fondo de color rosa pastel

    # Contenedor para los botones
    image_frame = LabelFrame(main_screen, text='Nombre', bg="#FFB6C1")  # Contenedor de la imagen
    image_frame.pack(padx=20, pady=20)  # Colocación del contenedor

    Logo = PhotoImage(file='GOGO.png')  # Imagen
    # La imagen se centra utilizando un label
    image_label = Label(image_frame, image=Logo, bg='grey')
    image_label.pack(pady=10)  # Colocación del label con la imagen

    button_frame = LabelFrame(main_screen, text='Actividades', bg="#FFB6C1")  # Segundo contenedor para los botones
    button_frame.pack(padx=20, pady=20)  # Colocación del contenedor

    # Estilos para los botones
    button_style = {'background': '#87CEFA', 'foreground': 'black', 'font': ('Arial', 12)}

    Button(button_frame, text='Registro de pedidos', command=Order_Screen, **button_style).grid(row=0, column=0, pady=10)
    Button(button_frame, text='Registro gastos', command=expenses_register, **button_style).grid(row=0, column=1, pady=10)
    Button(button_frame, text='Ventas', command=sales_consult, **button_style).grid(row=1, column=0, pady=10)
    Button(button_frame, text='Consultar pedidos', command=Consult_Orders, **button_style).grid(row=1, column=1, pady=10)
    Button(button_frame, text='Inventario', command=Inventario, **button_style).grid(row=2, column=0, pady=10)
    Button(button_frame, text='Consultar gastos', command=expenses_consult, **button_style).grid(row=2, column=1, pady=10)

    window.mainloop()



def Order_Screen():
    #pantalla para registrar pedidos,primero se registraran los datos del cliente y luego los datos de los pasteles
    window = Tk()
    window.withdraw()
    
    global order_Screen, Nombre_Entry, Phone_Entry, Cake_Options, Cant_Options, Date_entry, betun_options, Notes_entry

    order_Screen = Toplevel(window)
    order_Screen.title("Registro de pedidos")
    order_Screen.geometry("500x500")
    order_Screen.resizable(False, False)
    order_Screen.configure(bg='#7F7FFF')

    # Establecer la fuente para toda la interfaz
    font_style = tkFont.Font(family="Arial", size=14)

    # contenedor para la informacion del cliente que sera la que se mande a la tabla cliente
    customer_container = LabelFrame(order_Screen, text='Datos del cliente', bg='#7F7FFF')
    customer_container.grid(row=1, column=0, columnspan=10, padx=10, pady=10)

    #labels de ingreso de datos del cliente 
    Label(customer_container, text='Nombre', font=font_style).grid(row=1, column=0)
    Nombre_Entry = Entry(customer_container, font=font_style)
    Nombre_Entry.grid(row=1, column=1)

    Label(customer_container, text='Telefono', font=font_style).grid(row=2, column=0)
    Phone_Entry = Entry(customer_container, font=font_style)
    Phone_Entry.grid(row=2, column=1)

    Order_container = LabelFrame(order_Screen, text='Informacion del pedido')
    Order_container.grid(row=4, column=0, padx=10, pady=10)

    # tipos de pasteles
    Label(Order_container, text='Tipo de pastel', font=font_style).grid(row=1, column=0, padx=10, pady=10)
    Cake_type = StringVar(Order_container)
    Cake_type.set('Vainilla')
    Cake_Options = Combobox(Order_container, textvariable=Cake_type, values=['Tres leches', 'Chocolate', 'Volteado','Red velvet', 'Zanahoria'],font=font_style)
    Cake_Options.grid(row=1, column=1, padx=10, pady=10)

    #seleccionador de cantidad de personas
    Label(Order_container, text='Numero de personas', font=font_style).grid(row=2, column=0, padx=10, pady=10)
    Cant_Pers = StringVar(Order_container)
    Cant_Pers.set('20')
    Cant_Options = Combobox(Order_container, textvariable=Cant_Pers, values=['20', '30', '50'], font=font_style)
    Cant_Options.grid(row=2, column=1, padx=10, pady=10)

    #calendario para ingresar la fecha que se desea entregar 
    Label(Order_container, text='Fecha de entrega', font=font_style).grid(row=3, column=0, padx=10, pady=10)
    Date_entry = DateEntry(Order_container, date_pattern='yyyy/mm/dd', font=font_style)
    Date_entry.grid(row=3, column=1, padx=10, pady=10)

    #seleccionador para betun extra 
    Label(Order_container, text='Bettun extra', font=font_style).grid(row=4, column=0, padx=10, pady=10)
    betun_extra = StringVar(Order_container)
    betun_extra.set('Si')
    betun_options = Combobox(Order_container, textvariable=betun_extra, values=['Si', 'No'], font=font_style)
    betun_options.grid(row=4, column=1, padx=10, pady=10)

    #pequeña caja para notas extras
    Label(Order_container, text='Notas', font=font_style).grid(row=5, column=0, padx=10, pady=10)
    Notes_entry = Entry(Order_container, font=font_style)
    Notes_entry.grid(row=5, column=1, padx=10, pady=10)

    button_style = {'background': '#87CEFA', 'foreground': 'black', 'font': ('Arial', 12)}

    Button(Order_container, text='Realizar pedido', command=Send_Order, **button_style).grid(row=10, columnspan=3, sticky='w'+'e')

    

def Send_Order():
    #funcion que filtra los datos y los envia a la base de datos 
    global delete
    name = Nombre_Entry.get()
    Phone = Phone_Entry.get()
    pastel = Cake_Options.get()
    personas = Cant_Options.get()
    fecha = Date_entry.get()
    betun = betun_options.get()
    notas = Notes_entry.get()
    
    #pequeño muestreo de datos 
    print(name, Phone, pastel, personas, fecha, betun, notas)
    
    #revisa si ya existe el cliente mediante el numero de telefono , si no existe crea un nuevo cliene en la tabla cliente
    existe = consulta_cliente(Phone)
    if not existe:
        cliente_nuevo(name, Phone)

    # validacion de datos no vacios y de longitud correcta,
    try:
        longitud = len(Phone)
        if name != '' and longitud == 12 and pastel != '' and personas != '' and fecha != '' and betun != '' and notas != '':
            existe = consulta_cliente(Phone)
            Pedido_nuevo(pastel, personas, fecha, betun, notas, existe[0])
    except pymysql.err.OperationalError as error:
        #excepcion que se lanza si se activa el trigger
        if error.args[0] == 1644:
            show_warning_message('Error', 'La fecha de entrega debe tener una diferencia de una semana con respecto al día actual')
        else:
            show_warning_message('Error', 'Error al enviar el pedido a la base de datos')
        
        
def show_warning_message(title, message):
    #pantalla de aviso que se lanza si se activo el triger
    window = Tk()
    window.withdraw()
    messagebox.showwarning(title, message)    
            
def Consult_Orders():
    global months_options, orders, months_options
    window = Tk()
    window.withdraw()

    Consult_Screen = Toplevel(window)
    Consult_Screen.title("Consulta de pedidos")
    Consult_Screen.geometry("1200x600")
    Consult_Screen.resizable(False, False)
    Consult_Screen.configure(bg='#9797FF')

    # Establecer la fuente para toda la interfaz
    font_style = tkFont.Font(family="Arial", size=14)

    Consult = LabelFrame(Consult_Screen, text='Pedidos pendientes', bg='#9797FF')
    Consult.grid(row=1, column=0)

    Label(Consult, text='Mes', font=font_style,bg='#9797FF').grid(row=1, column=0, padx=10, pady=10)
    months = StringVar(Consult)
    months.set('Enero')
    months_options = Combobox(Consult, textvariable=months, values=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'], font=font_style)
    months_options.grid(row=1, column=1, padx=10, pady=10)

    button_style = {'background': '#87CEFA', 'foreground': 'black', 'font': ('Arial', 12)}

    Button(Consult, text='Buscar', command=Consult_Function2, **button_style).grid(row=1, column=2, padx=10, pady=10)

    orders_frame = LabelFrame(Consult_Screen, text='Pedidos', bg='#9797FF')
    orders_frame.grid(row=2, column=0, padx=10, pady=10)

    #tabla para mostrar los distintos pediso +
    orders = Treeview(orders_frame, columns=("Column1", "Column2", "Column3", "Column4", "Column5"), show="headings")
    orders.grid(row=2, column=0, columnspan=3)

    orders.heading("Column1", text='Id Pedido')
    orders.heading("Column2", text='Fecha ')
    orders.heading("Column3", text='Pastel')
    orders.heading("Column4", text='Numero de personas')
    orders.heading("Column5", text='Estado')

    Button(orders_frame, text='Editar', command=update_Order_screen, **button_style).grid(row=5, column=0, sticky='w'+'e')
    Button(orders_frame, text='Eliminar', command=Delete_Order, **button_style).grid(row=5, column=1, sticky='w'+'e')
    Button(orders_frame, text='Liquidar', command=Liquidar_orden, **button_style).grid(row=5, column=2, sticky='w'+'e')

def Delete_Order():
    try:
        orders.item(orders.selection())['values']
    except IndexError as e:
        return
    id = orders.item(orders.selection())['values'][0]
    delete_Order(id)
     
    
def Consult_Function2():
    
    pedidos = orders.get_children()
    for elementos in pedidos:
            orders.delete(elementos)
            
    
    if months_options.get() == 'Enero':
        num_mes = '1'
    elif months_options.get() == 'Febrero':
        num_mes = '2'
    elif months_options.get() == 'Marzo':
        num_mes = '3'
    elif months_options.get() == 'Abril':
        num_mes = '4'
    elif months_options.get() == 'Mayo':
        num_mes = '5'
    elif months_options.get() == 'Junio':
        num_mes = '6'    
    elif months_options.get() == 'Julio':
        num_mes = '7'
    elif months_options.get() == 'Agosto':
        num_mes = '8'    
    elif months_options.get() == 'Septiembre':
        num_mes = '9'
    elif months_options.get() == 'Octubre':
        num_mes = '10'
    elif months_options.get() == 'Noviembre':
        num_mes = '11'
    elif months_options.get() == 'Diciembre':
        num_mes = '12'
        
    pedidos = Consulta_mes(num_mes)
    for columna in pedidos:
        if columna[8] == 'Activo' and columna[7] == 'Pendiente':
            orders.insert('',0, values= (columna[0],columna[3],columna[1],columna[2],columna[7]))
    
    
def update_Order_screen():
    
    window = Tk()
    window.withdraw()

    order_Screen = Toplevel(window)
    order_Screen.title("Editar pedidos")
    order_Screen.geometry("400x400")
    order_Screen.resizable(False,False)
    order_Screen.configure(bg='#9797FF')
    
    global Upd_Cake_Options,Upd_Cant_Options,Upd_Date_entry,Upd_betun_options,Upd_Notes_entry,elemento
    button_style = {'background': '#87CEFA', 'foreground': 'black', 'font': ('Arial', 12)}
    
    elemento = orders.item(orders.selection())['values'][0]
    
    #contenedor para la informacion del cliente que sera la que se mande a la tabla cliente
    Order_container = LabelFrame(order_Screen,text='Informacion del pedido')
    Order_container.grid(row=1,column= 0,padx=10,pady=10)

    #tipos de pasteles
    Label(Order_container,text='Tipo de pastel').grid(row=1,column=0,padx=10,pady=10)
    Cake_type = StringVar(Order_container)
    Upd_Cake_Options = Combobox(Order_container,textvariable= Cake_type,values=['Tres leches','Chocolate','Volteado','Red velvet','Zanahoria'])
    Upd_Cake_Options.grid(row=1, column=1,padx=10,pady=10)

    Label(Order_container,text='Numero de personas').grid(row=2,column=0,padx=10,pady=10)
    Cant_Pers = StringVar(Order_container)
    Upd_Cant_Options = Combobox(Order_container,textvariable= Cant_Pers,values= ['20','30','50'] )
    Upd_Cant_Options.grid(row=2,column = 1,padx=10,pady=10)

    
    Label(Order_container,text='Fecha de entrega').grid(row=3,column=0,padx=10,pady=10)
    Upd_Date_entry = DateEntry(Order_container,date_pattern='yyyy/mm/dd')
    Upd_Date_entry.grid(row=3,column= 1,padx=10,pady=10)


    Label(Order_container,text='Bettun extra').grid(row=4,column=0,padx=10,pady=10)
    betun_extra = StringVar(Order_container)
    betun_extra.set('Si')
    Upd_betun_options = Combobox(Order_container,textvariable=betun_extra,values=['Si','No'])
    Upd_betun_options.grid(row=4,column=1,padx=10,pady=10)


    Label(Order_container,text='Notas').grid(row=5,column=0,padx=10,pady=10)
    Upd_Notes_entry = Entry(Order_container)
    Upd_Notes_entry.grid(row=5, column=1,padx=10,pady=10)

    Button(Order_container,text='Actualizar',command=Update_order_Function,**button_style).grid(row=10,columnspan=3,sticky= W + E)
    
          
def Update_order_Function():
    pastel = Upd_Cake_Options.get()
    pers = Upd_Cant_Options.get()
    date = Upd_Date_entry.get()
    betun = Upd_betun_options.get()
    nota = Upd_Notes_entry.get()
    
    if pastel != '' and pers != '' and date != '' and betun != '' and nota != '':  
        Update_Order(elemento,pastel,pers,date,betun,nota)
    
def Liquidar_orden():
    global monto
    try:
        orders.item(orders.selection())['values']
    except IndexError as e: 
        return
    id = orders.item(orders.selection())['values'][0]
    Liquidar_Pedido(id)
    
    pedidos : list 
    pedidos = Consultar_pedidos()

    ventas : list = []
    for pedido in pedidos:
        if pedido[7] == 'Liquidado':
            ventas.append(pedido)
            
    for venta in ventas: 
        if id == venta[0]:
            pastel = venta[1]
            personas = venta[2]
            betun = venta[4]
    fecha = datetime.now().date()
    fechaFormateada = fecha.strftime("%d/%m/%y")
    
    personas = str(personas)

    if pastel == 'Zanahoria' and personas == '20' and betun == 'Si':
        monto = '700'
    elif  pastel == 'Zanahoria' and personas == '20' and betun == 'No':
        monto = '650'
    elif pastel == 'Zanahoria' and personas == '30' and betun == 'Si':
        monto = '980'
    elif pastel == 'Zanahoria' and personas == '30' and betun == 'No':
        monto = '930'
    elif pastel == 'Zanahoria' and personas == '50' and betun == 'Si':
        monto = '1750'
    elif pastel == 'Zanahoria' and personas == '50' and betun == 'No':
        monto = '1700'
    elif pastel == 'Chocolate' and personas == '20' and betun == 'Si':
        monto = '350'
    elif  pastel == 'Chocolate' and personas == '20' and betun == 'No':
        monto = '300'
    elif pastel == 'Chocolate' and personas == '30' and betun == 'Si':
        monto = '650'
    elif pastel == 'Chocolate' and personas == '30' and betun == 'No':
        monto = '600'
    elif pastel == 'Chocolate' and personas == '50' and betun == 'Si':
        monto = '1050'
    elif pastel == 'Chocolate' and personas == '50' and betun == 'No':
        monto = '1000' 
    elif pastel == 'Volteado' and personas == '20' and betun == 'Si':
        monto = '730'
    elif  pastel == 'Volteado' and personas == '20' and betun == 'No':
        monto = '680'
    elif pastel == 'Volteado' and personas == '30' and betun == 'Si':
        monto = '900'
    elif pastel == 'Volteado' and personas == '30' and betun == 'No':
        monto = '850'
    elif pastel == 'Volteado' and personas == '50' and betun == 'Si':
        monto = '1550'
    elif pastel == 'Volteado' and personas == '50' and betun == 'No':
        monto = '1500'  
    elif pastel == 'Tres leches' and personas == '20' and betun == 'Si':
        monto = '350'
    elif  pastel == 'Tres leches' and personas == '20' and betun == 'No':
        monto = '300'
    elif pastel == 'Tres leches' and personas == '30' and betun == 'Si':
        monto = '410'
    elif pastel == 'Tres leches' and personas == '30' and betun == 'No':
        monto = '360'
    elif pastel == 'Tres leches' and personas == '50' and betun == 'Si':
        monto = '700'
    elif pastel == 'Tres leches' and personas == '50' and betun == 'No':
        monto = '650'
    elif pastel == 'Red velvet' and personas == '20' and betun == 'Si':
        monto = '510'
    elif  pastel == 'Red velvet' and personas == '20' and betun == 'No':
        monto = '460'
    elif pastel == 'Red velvet' and personas == '30' and betun == 'Si':
        monto = '650'
    elif pastel == 'Red velvet' and personas == '30' and betun == 'No':
        monto = '600'
    elif pastel == 'Red velvet' and personas == '50' and betun == 'Si':
        monto = '980'
    elif pastel == 'Red velvet' and personas == '50' and betun == 'No':
        monto = '930'
    

    if pastel != '' and personas != '' and monto !='' :
        print('test 3')
        print(pastel,monto,personas,fechaFormateada)
        Venta_Nueva(monto,pastel,personas,fechaFormateada,id)
        print('venta exitosa')
           
def sales_consult(): #Pagina  para consultar las ventas por mes 
    window = Tk()
    window.withdraw()

    global tablaVentas, months_options3

    sales_screen = Toplevel(window)
    sales_screen.title("VENTAS")
    sales_screen.geometry("1100x600")
    sales_screen.resizable(False, False)
    sales_screen.configure(bg='#9797FF')

    button_style = {'background': '#87CEFA', 'foreground': 'black', 'font': ('Arial', 12)}
    
    contenedorVenta = LabelFrame(sales_screen, text="Consulta", bg='#9797FF')
    contenedorVenta.grid(row=1, column=0)

    Label(contenedorVenta, text='Mes', bg='#9797FF').grid(row=1, column=0, padx=10, pady=10)
    months = StringVar(contenedorVenta)
    months.set('Enero')
    months_options3 = Combobox(contenedorVenta, textvariable=months, values=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
    months_options3.grid(row=1, column=1, padx=10, pady=10)

    Button(contenedorVenta, text='Buscar', command=sales_consult_function,**button_style).grid(row=1, column=2, padx=10, pady=10)

    Ventas = LabelFrame(sales_screen, text="Ventas", bg='#9797FF')
    Ventas.grid(row=2, column=0, padx=10, pady=10)

    tablaVentas = Treeview(Ventas, columns=("column1", "column2", "column3", "column4", "column5"), show="headings")
    tablaVentas.grid(row=2, column=0, columnspan=3)

    tablaVentas.heading("column1", text='Id Venta', anchor='center')
    tablaVentas.heading("column2", text='Monto', anchor='center')
    tablaVentas.heading("column3", text='Pastel', anchor='center')
    tablaVentas.heading("column4", text='Numero de personas', anchor='center')
    tablaVentas.heading("column5", text='Fecha de venta', anchor='center')

    Button(Ventas, text='Borrar', command=Delete_sales, **button_style).grid(row=3, columnspan=3, sticky= W + E)

                       
def sales_consult_function():
    
    elementos = tablaVentas.get_children()
    for elemento in elementos:
        tablaVentas.delete(elemento)
    
 
    if months_options3.get() == 'Enero':
        num_mes = '01'
    elif months_options3.get() == 'Febrero':
        num_mes = '02'
    elif months_options3.get() == 'Marzo':
        num_mes = '03'
    elif months_options3.get() == 'Abril':
        num_mes = '04'
    elif months_options3.get() == 'Mayo':
        num_mes = '05'
    elif months_options3.get() == 'Junio':
        num_mes = '06'    
    elif months_options3.get() == 'Julio':
        num_mes = '07'
    elif months_options3.get() == 'Agosto':
        num_mes = '08'    
    elif months_options3.get() == 'Septiembre':
        num_mes = '09'
    elif months_options3.get() == 'Octubre':
        num_mes = '10'
    elif months_options3.get() == 'Noviembre':
        num_mes = '11'
    elif months_options3.get() == 'Diciembre':
        num_mes = '12'
        
    ventas = Consulta_Venta_Mes(num_mes)
    
    for columna in ventas:
        if columna[5] == 'Activo':
            tablaVentas.insert('',0, values= (columna[0],columna[1],columna[3],columna[4],columna[6]))
    
def expenses_consult():
    window = Tk()
    window.withdraw()
    
    global gastos_Tabla, months_options2
    sales_screen = Toplevel(window)
    sales_screen.title("Gastos")
    sales_screen.geometry("1100x600")
    sales_screen.resizable(False,False)
    sales_screen.configure(bg='#9797FF')
    
    button_style = {'background': '#87CEFA', 'foreground': 'black', 'font': ('Arial', 12)}
    
    contenedorGasto = LabelFrame(sales_screen,text="Consulta",bg='#9797FF')
    contenedorGasto.grid(row=1,column=0)
    
    Label(contenedorGasto,text='Mes',bg='#9797FF').grid(row=1,column=0,padx=10,pady=10)
    months = StringVar(contenedorGasto)
    months.set('Enero')
    months_options2 = Combobox(contenedorGasto,textvariable=months,values=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])
    months_options2.grid(row=1,column=1,padx=10,pady=10)

    
    Button(contenedorGasto,text='Buscar',command=Consult_expense_function,**button_style).grid(row=1,column=2,padx=10,pady=10)

    tabla = LabelFrame(sales_screen,text='Gastos')
    tabla.grid(row=2,column=0,padx=10,pady=10)
    
    #concepto, fecha , total  
    gastos_Tabla =  Treeview(tabla,height=10,columns=('Id Gasto','Concepto','Fecha','Total','Precio'),show='headings')
    gastos_Tabla.grid(row=2,column=0,columnspan=3)
    
    gastos_Tabla.heading('Id Gasto',text='Id Gasto',anchor=CENTER)
    gastos_Tabla.heading('Concepto',text='Concepto',anchor=CENTER)
    gastos_Tabla.heading('Fecha',text='Fecha',anchor=CENTER)
    gastos_Tabla.heading('Total',text='Total',anchor=CENTER)
    gastos_Tabla.heading('Precio',text='Precio',anchor=CENTER)
    
    
    
    Button(tabla,text='Borrar',command=delete_expense,**button_style).grid(row=3,columnspan = 3,sticky= W + E)
    
    Button(tabla,text='Editar',command=update_expense_scree,**button_style).grid(row=4,columnspan = 3,sticky= W + E)
     
def Inventario():
    
    window = Tk()
    window.withdraw()
    Inventario_Screen = Toplevel(window)
    Inventario_Screen.title('Insumos')
    Inventario_Screen.geometry('900x500')
    Inventario_Screen.resizable(False,False)
    Inventario_Screen['bg'] = '#AC99F2'

    global tabla_insumos
    
    button_style = {'background': '#87CEFA', 'foreground': 'black', 'font': ('Arial', 12)}
    
    Inventario_container = LabelFrame(Inventario_Screen,text='Inventario')
    Inventario_container.grid(row=1,column=0,padx=10,pady=10)
    
    tabla_insumos = Treeview(Inventario_container,columns=('column1','column2','column3','column4'),show='headings')
    tabla_insumos.grid(row=1,column=0,padx=10,pady=10 )
    
    tabla_insumos.heading('column1',text='Materia',anchor=CENTER)
    tabla_insumos.heading('column2',text='Existencias',anchor=CENTER)
    tabla_insumos.heading('column3',text='Cantidad',anchor=CENTER)
    tabla_insumos.heading('column4',text='Precio',anchor=CENTER)
    
    tabla =tabla_insumos.get_children()
    for elementos in tabla:
        tabla_insumos.delete(elementos)
    
    materias : list
    materias  = Consultar_Materias()
        
    materias_existentes : list = []
    for productos in materias:
        if productos[2] != 0:
            materias_existentes.append(productos)
            
    for productos in materias_existentes:
        tabla_insumos.insert('',0, values=(productos[1],productos[2],productos[4],productos[3]))
        
    Button(Inventario_container,text='Editar',**button_style).grid(row=2,column=0,sticky=W + E)
    Button(Inventario_container,text='Eliminar',command=delete_materia,**button_style).grid(row=3,column=0,sticky= W + E)
   
def delete_materia():
    try:
        tabla_insumos.item(tabla_insumos.selection())['values']
    except IndexError as e: 
        return
    name = tabla_insumos.item(tabla_insumos.selection())['values'][0]
    id= Consultar_materia(name)
    Delete_Materia(id[0])
              
def expenses_register():
    window = Tk()
    window.withdraw()
    
    global concept_Entrty,Date_entry,total_Entry,price_entry
    
    expenses_window = Toplevel()
    expenses_window.title('Registro de pedidos')
    expenses_window.geometry('300x300')
    expenses_window.resizable(False,False)
    expenses_window.configure(bg='#AC99F2')
    
    button_style = {'background': '#87CEFA', 'foreground': 'black', 'font': ('Arial', 12)}
    
    expense_container = LabelFrame(expenses_window,text='Registro de gastos')
    expense_container.grid(row=1,column=1,padx=10,pady=10)
    
    Label(expense_container,text='Concepto ').grid(row=1,column=0,padx=10,pady=10)
    concept_Entrty = Entry(expense_container)
    concept_Entrty.grid(row=1,column=1,padx=10,pady=10)
    
    Label(expense_container,text='Fecha de Gasto').grid(row=2,column=0,padx=10,pady=10)
    Date_entry = DateEntry(expense_container,date_pattern='yyyy/mm/dd')
    Date_entry.grid(row=2,column= 1,padx=10,pady=10)
    
    Label(expense_container,text='Total comprado').grid(row=3,column=0,padx=10,pady=10)
    total_Entry = Entry(expense_container)
    total_Entry.grid(row=3,column=1,padx=10,pady=10)
    
    Label(expense_container,text='Precio').grid(row=4,column=0,padx=10,pady=10)
    price_entry = Entry(expense_container)
    price_entry.grid(row=4,column=1,padx=10,pady=10)
    
    
    Button(expense_container, text='Ingresar gasto', command=send_expense, **button_style).grid(row=5, column=0, padx=10, pady=10)

    
    
def send_expense():
    concepto = concept_Entrty.get()
    fecha = Date_entry.get()
    total = total_Entry.get()
    precio = price_entry.get()
    materias = Consultar_Materias()
    concepto_format = concepto.capitalize()[0] + concepto.lower()[1:]
    
    #ciclo para aumentar las existencias del inventario con respecto al gasto ingresado y lo comprado
    for materia in materias:
        if concepto_format == materia[1]:
            nuevo_stock = materia[2] + int(total)
            
    #ciclo para recuperar el id de la materia con respecto al concepto del gasto    
    for materia in materias:
        if concepto_format == materia[1]:
            id_mat = materia[0]
    
    #pequeña validacion para saber si los datos no estan vacios 
    if concepto != '' and fecha != '' and total != '':
        Update_Stock(id_mat, nuevo_stock)
        Gasto_Nuevo(concepto_format,fecha,total,precio,id_mat)
    
def Consult_expense_function():
    
    expenses = gastos_Tabla.get_children()
    for elementos in expenses:
        gastos_Tabla.delete(elementos)
    
    if months_options2.get() == 'Enero':
        num_mes = '01'
    elif months_options2.get() == 'Febrero':
        num_mes = '02'
    elif months_options2.get() == 'Marzo':
        num_mes = '03'
    elif months_options2.get() == 'Abril':
        num_mes = '04'
    elif months_options2.get() == 'Mayo':
        num_mes = '05'
    elif months_options2.get() == 'Junio':
        num_mes = '06'    
    elif months_options2.get() == 'Julio':
        num_mes = '07'
    elif months_options2.get() == 'Agosto':
        num_mes = '08'    
    elif months_options2.get() == 'Septiembre':
        num_mes = '09'
    elif months_options2.get() == 'Octubre':
        num_mes = '10'
    elif months_options2.get() == 'Noviembre':
        num_mes = '11'
    elif months_options2.get() == 'Diciembre':
        num_mes = '12'
        
    Gasto_Mes = Consulta_Gasto_mes(num_mes)

    for columna in Gasto_Mes:
        if columna[5] == 'Activo':
            print(columna[0],columna[1],columna[2],columna[3],columna[4])
            #gastos_Tabla.insert('',0,values=(columna[0],columna[1],columna[2],columna[3],columna[4]))
        
def delete_expense():
    try:
        gastos_Tabla.item(gastos_Tabla.selection())['values']
    except IndexError as e:
        return
    id = gastos_Tabla.item(gastos_Tabla.selection())['values'][0]
    Delete_Expense(id)
    
def update_expense_scree():
    
    window = Tk()
    window.withdraw()
    
    upd_expense_screen = Toplevel(window)
    upd_expense_screen.title('Modificar gasto')
    upd_expense_screen.geometry('400x400')
    upd_expense_screen.resizable(False,False)
    
    global upd_Date_entry_expense,upd_concept_Entrty,upd_total_Entry,id_expense
    
    id_expense = gastos_Tabla.item(gastos_Tabla.selection())['values'][0]
    
    expense_container = LabelFrame(upd_expense_screen,text='Actualizacion de gastos')
    expense_container.grid(row=1,column=1,padx=10,pady=10)
    
    Label(expense_container,text='Concepto ').grid(row=1,column=0,padx=10,pady=10)
    upd_concept_Entrty = Entry(expense_container)
    upd_concept_Entrty.grid(row=1,column=1,padx=10,pady=10)
    
    Label(expense_container,text='Fecha de Gasto').grid(row=2,column=0,padx=10,pady=10)
    upd_Date_entry_expense = DateEntry(expense_container,date_pattern='yyyy/mm/dd')
    upd_Date_entry_expense.grid(row=2,column= 1,padx=10,pady=10)
    
    Label(expense_container,text='Total comprado').grid(row=3,column=0,padx=10,pady=10)
    upd_total_Entry = Entry(expense_container)
    upd_total_Entry.grid(row=3,column=1,padx=10,pady=10)
    
    Button(expense_container,text='Actualizar',command=Update_expense_function).grid(row=4,column=0,padx=10,pady=10)
    
    
    
def Update_expense_function():
    concept = upd_concept_Entrty.get()
    date_expense = upd_Date_entry_expense.get()
    total_expense = upd_total_Entry.get()
    
    if concept != '' and date_expense != '' and total_expense != '':
        Update_Expense(concept,date_expense,total_expense,id_expense)
            
def Delete_sales():
    try:
        tablaVentas.item(tablaVentas.selection())['values']
    except IndexError as e: 
        return
    id = tablaVentas.item(tablaVentas.selection())['values'][0]
    print(id)
    Delete_Venta(id)
    


main_screen()


