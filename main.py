from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
from tkcalendar import DateEntry

from Handlers.Pedido import *
from Handlers.Clientes import *
from Handlers.Gasto import *
from Handlers.Ventas import *
from Handlers.Inventario import *




def main_screen():
    #creacion de la pantalla principal 
    window = Tk()
    window.withdraw()

    main_screen = Toplevel(window)
    main_screen.title("Pagina Principal")
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

    global Nombre_Entry,Phone_Entry,Cake_Options,Cant_Options,Date_entry,betun_options,Notes_entry
    #contenedor para la informacion del cliente que sera la que se mande a la tabla cliente
    customer_container = LabelFrame(order_Screen,text='Datos del cliente')
    customer_container.grid(row=1,column=0, columnspan=10,padx=10,pady=10)

    Label(customer_container,text='Nombre').grid(row=1,column=0)
    Nombre_Entry = Entry(customer_container)
    Nombre_Entry.grid(row=1, column=1)
    

    Label(customer_container, text='Telefono').grid(row=2,column=0)
    Phone_Entry = Entry(customer_container)
    Phone_Entry.grid(row=2,column=1)


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
    Date_entry = DateEntry(Order_container,date_pattern='dd/mm/yyyy')
    Date_entry.grid(row=3,column= 1,padx=10,pady=10)


    Label(Order_container,text='Bettun extra').grid(row=4,column=0,padx=10,pady=10)
    betun_extra = StringVar(Order_container)
    betun_extra.set('Si')
    betun_options = Combobox(Order_container,textvariable=betun_extra,values=['Si','No'])
    betun_options.grid(row=4,column=1,padx=10,pady=10)

    

    Label(Order_container,text='Notas').grid(row=5,column=0,padx=10,pady=10)
    Notes_entry = Entry(Order_container)
    Notes_entry.grid(row=5, column=1,padx=10,pady=10)

    Button(Order_container,text='Realizar pedido',command=Send_Order).grid(row=10,columnspan=3,sticky= W + E)
    
    Button(Order_container,text='Regresar').grid(row=11,columnspan=3,sticky= W + E)

def Send_Order():

    name = Nombre_Entry.get()
    Phone = Phone_Entry.get()
    pastel = Cake_Options.get()
    personas = Cant_Options.get()
    fecha = Date_entry.get()
    betun = betun_options.get()
    notas = Notes_entry.get()
    
    existe = consulta_cliente(Phone)
    if not existe:
        cliente_nuevo(name,Phone)
         
    longitud = len(Phone)
    if name != '' and longitud ==12 and pastel != '' and personas != '' and fecha != '' and betun != '' and notas != '':
        existe = consulta_cliente(Phone)
        Pedido_nuevo(pastel,personas,fecha,betun,notas,existe[0]) 
       
    else:
        print('Datos no validos')
     
def Consult_Orders():

    global months_options,orders,months_options
    window = Tk()
    window.withdraw()

    Consult_Screen = Toplevel(window)
    Consult_Screen.title("Consulta de pedidos")
    Consult_Screen.geometry("1200x600")
    Consult_Screen.resizable(False,False)

    Consult = LabelFrame(Consult_Screen,text='Pedidos pendientes')
    Consult.grid(row=1,column=0)


    Label(Consult,text='Mes').grid(row=1,column=0,padx=10,pady=10)
    months = StringVar(Consult)
    months.set('Enero')
    months_options = Combobox(Consult,textvariable=months,values=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])
    months_options.grid(row=1,column=1,padx=10,pady=10)

    Button(Consult,text='Buscar',command=Consult_Function).grid(row=1,column=2,padx=10,pady=10)

    orders_frame = LabelFrame(Consult_Screen,text='Pedidos')
    orders_frame.grid(row=2,column=0,padx=10,pady=10)
    

    orders = Treeview(orders_frame,columns=("Column1","Column2","Column3","Column4","Column5"),show="headings")
    orders.grid(row=2,column=0,columnspan=3)

    orders.heading("Column1",text='Id Pedido')
    orders.heading("Column2",text='Fecha ')
    orders.heading("Column3",text='Pastel')
    orders.heading("Column4",text='Numero de personas')
    orders.heading("Column5",text='Estado')
            
    Button(orders_frame,text='Editar',command=update_Order_screen).grid(row=5,column=0,sticky= W + E)
    Button(orders_frame,text='Eliminar',command=Delete_Order).grid(row=5,column=1,sticky= W + E)
    Button(orders_frame,text='Liquidar',command=Liquidar_orden).grid(row=5,column=2,sticky= W + E)
    Button(orders_frame,text='Regresar').grid(row=6,columnspan=3,sticky= W + E )
    
def Delete_Order():
    try:
        orders.item(orders.selection())['values']
    except IndexError as e:
        return
    id = orders.item(orders.selection())['values'][0]
    delete_Order(id)
     
def Consult_Function():
    
    pedidos = orders.get_children()
    for elementos in pedidos:
            orders.delete(elementos)
            
    ordenes: list
    ordenes = Consultar_pedidos()
    
    if months_options.get() == 'Enero':
        num_mes = '01'
    elif months_options.get() == 'Febrero':
        num_mes = '02'
    elif months_options.get() == 'Marzo':
        num_mes = '03'
    elif months_options.get() == 'Abril':
        num_mes = '04'
    elif months_options.get() == 'Mayo':
        num_mes = '05'
    elif months_options.get() == 'Junio':
        num_mes = '06'    
    elif months_options.get() == 'Julio':
        num_mes = '07'
    elif months_options.get() == 'Agosto':
        num_mes = '08'    
    elif months_options.get() == 'Septiembre':
        num_mes = '09'
    elif months_options.get() == 'Octubre':
        num_mes = '10'
    elif months_options.get() == 'Noviembre':
        num_mes = '11'
    elif months_options.get() == 'Diciembre':
        num_mes = '12'
        
    pedidos_filtrados : list = []
    for pedido in ordenes:
        if num_mes == pedido[3][3:5]:
            pedidos_filtrados.append(pedido)
    
  
    for columna in pedidos_filtrados:
        if columna[8] == 'Activo' and columna[7] == 'Pendiente':
            orders.insert('',0, values= (columna[0],columna[3],columna[1],columna[2],columna[7]))
    
def update_Order_screen():
    
    window = Tk()
    window.withdraw()

    order_Screen = Toplevel(window)
    order_Screen.title("Editar pedidos")
    order_Screen.geometry("400x400")
    order_Screen.resizable(False,False)

    global Upd_Cake_Options,Upd_Cant_Options,Upd_Date_entry,Upd_betun_options,Upd_Notes_entry,elemento
    
    
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
    Upd_Date_entry = DateEntry(Order_container,date_pattern='dd/mm/yyyy')
    Upd_Date_entry.grid(row=3,column= 1,padx=10,pady=10)


    Label(Order_container,text='Bettun extra').grid(row=4,column=0,padx=10,pady=10)
    betun_extra = StringVar(Order_container)
    betun_extra.set('Si')
    Upd_betun_options = Combobox(Order_container,textvariable=betun_extra,values=['Si','No'])
    Upd_betun_options.grid(row=4,column=1,padx=10,pady=10)


    Label(Order_container,text='Notas').grid(row=5,column=0,padx=10,pady=10)
    Upd_Notes_entry = Entry(Order_container)
    Upd_Notes_entry.grid(row=5, column=1,padx=10,pady=10)

    Button(Order_container,text='Actualizar',command=Update_order_Function).grid(row=10,columnspan=3,sticky= W + E)
    
    Button(Order_container,text='Regresar').grid(row=11,columnspan=3,sticky= W + E)
          
def Update_order_Function():
        pastel = Upd_Cake_Options.get()
        pers = Upd_Cant_Options.get()
        date = Upd_Date_entry.get()
        betun = Upd_betun_options.get()
        nota = Upd_Notes_entry.get()
        
        if pastel != '' and pers != '' and date != '' and betun != '' and nota != '':  
                Update_Order(elemento,pastel,pers,date,betun,nota)
    
def Liquidar_orden():
    try:
        orders.item(orders.selection())['values']
    except IndexError as e: 
        return
    id = orders.item(orders.selection())['values'][0]
    Liquidar_Pedido(id)
    
def sales_consult(): #Pagina  para consultar las ventas por mes 
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
    
    ventas.heading("column1",text='Fecha',anchor=CENTER)
    ventas.heading("column2",text='Monto', anchor=CENTER)
    ventas.heading("column3",text='Informacion',anchor=CENTER)
    
    Button(tabla,text='Borrar').grid(row=3,column=0,sticky= W + E)
    
    Button(tabla,text='Editar').grid(row=3,column=1,sticky= W + E)
    
    Button(tabla,text='Regresar').grid(row=4,columnspan=3,sticky=W + E)

def Sales_Function():
    pedidos :list
    pedidos = Consultar_pedidos()
    
    ventas : list 
    for pedido in pedido:
        if pedido[7] == 'Liquidado':
            ventas.append(pedido)
            
def sales_consult_function():
    
    pedidos : list
    pedidos = Consultar_pedidos()
    
    ventas : list
    for pedido in pedidos:
        if pedido[7] == 'Liquidado':
            ventas.append(pedido)
    
    if months_options.get() == 'Enero':
        num_mes = '01'
    elif months_options.get() == 'Febrero':
        num_mes = '02'
    elif months_options.get() == 'Marzo':
        num_mes = '03'
    elif months_options.get() == 'Abril':
        num_mes = '04'
    elif months_options.get() == 'Mayo':
        num_mes = '05'
    elif months_options.get() == 'Junio':
        num_mes = '06'    
    elif months_options.get() == 'Julio':
        num_mes = '07'
    elif months_options.get() == 'Agosto':
        num_mes = '08'    
    elif months_options.get() == 'Septiembre':
        num_mes = '09'
    elif months_options.get() == 'Octubre':
        num_mes = '10'
    elif months_options.get() == 'Noviembre':
        num_mes = '11'
    elif months_options.get() == 'Diciembre':
        num_mes = '12'
        
    ventas_filtradas : list= []
    
def expenses_consult():
    window = Tk()
    window.withdraw()
    
    global gastos_Tabla, months_options2
    sales_screen = Toplevel(window)
    sales_screen.title("Gastos")
    sales_screen.geometry("900x600")
    sales_screen.resizable(False,False)
    
    contenedorGasto = LabelFrame(sales_screen,text="Consulta")
    contenedorGasto.grid(row=1,column=0)
    
    Label(contenedorGasto,text='Mes').grid(row=1,column=0,padx=10,pady=10)
    months = StringVar(contenedorGasto)
    months.set('Enero')
    months_options2 = Combobox(contenedorGasto,textvariable=months,values=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])
    months_options2.grid(row=1,column=1,padx=10,pady=10)

    
    Button(contenedorGasto,text='Buscar',command=Consult_expense_function).grid(row=1,column=2,padx=10,pady=10)

    tabla = LabelFrame(sales_screen,text='Gastos')
    tabla.grid(row=2,column=0,padx=10,pady=10)
    
    #concepto, fecha , total  
    gastos_Tabla =  Treeview(tabla,height=10,columns=('Id Gasto','Concepto','Fecha','Total'),show='headings')
    gastos_Tabla.grid(row=2,column=0,columnspan=3)
    
    gastos_Tabla.heading('Id Gasto',text='Id Gasto',anchor=CENTER)
    gastos_Tabla.heading('Concepto',text='Concepto',anchor=CENTER)
    gastos_Tabla.heading('Fecha',text='Fecha',anchor=CENTER)
    gastos_Tabla.heading('Total',text='Total',anchor=CENTER)
    
    
    
    Button(tabla,text='Borrar',command=delete_expense).grid(row=3,column=0,sticky= W + E)
    
    Button(tabla,text='Editar',command=update_expense_scree).grid(row=3,column=1,sticky= W + E)
    
    Button(tabla,text='Regresar').grid(row=4,columnspan=3,sticky= W + E)
     
def Inventario():
    
    window = Tk()
    window.withdraw()
    Inventario_Screen = Toplevel(window)
    Inventario_Screen.title('Insumos')
    Inventario_Screen.geometry('900x500')
    Inventario_Screen.resizable(False,False)
    Inventario_Screen['bg'] = '#AC99F2'

    global tabla_insumos

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
        
    Button(Inventario_container,text='Editar').grid(row=2,column=0,sticky=W + E)
    Button(Inventario_container,text='Eliminar',command=(delete_materia)).grid(row=2,column=1,sticky= W + E)
    Button(Inventario_container,text='Regresar').grid(row=3,columnspan=3,sticky= W + E)
   
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
    
    global concept_Entrty,Date_entry,total_Entry
    
    expenses_window = Toplevel()
    expenses_window.title('Registro de pedidos')
    expenses_window.geometry('600x600')
    expenses_window.resizable(False,False)
    
    
    expense_container = LabelFrame(expenses_window,text='Registro de gastos')
    expense_container.grid(row=1,column=1,padx=10,pady=10)
    
    Label(expense_container,text='Concepto ').grid(row=1,column=0,padx=10,pady=10)
    concept_Entrty = Entry(expense_container)
    concept_Entrty.grid(row=1,column=1,padx=10,pady=10)
    
    Label(expense_container,text='Fecha de Gasto').grid(row=2,column=0,padx=10,pady=10)
    Date_entry = DateEntry(expense_container,date_pattern='dd/mm/yyyy')
    Date_entry.grid(row=2,column= 1,padx=10,pady=10)
    
    Label(expense_container,text='Total comprado').grid(row=3,column=0,padx=10,pady=10)
    total_Entry = Entry(expense_container)
    total_Entry.grid(row=3,column=1,padx=10,pady=10)
    
    Button(expense_container,text='Ingresar gasto',command=send_expense).grid(row=4,column=0,padx=10,pady=10)
    
    Button(expense_container,text='Regresar').grid(row=4,column=1,padx=10,pady=10)
    
def send_expense():
    concepto = concept_Entrty.get()
    fecha = Date_entry.get()
    total = total_Entry.get()
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
        Gasto_Nuevo(concepto_format,fecha,total,id_mat)
    
def Consult_expense_function():
    
    expenses = gastos_Tabla.get_children()
    for elementos in expenses:
        gastos_Tabla.delete(elementos)
    
    gastos  : list
    gastos = Consultar_Gastos()
    
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
        
    gastos_filtrados: list = []
    
    for gasto in gastos:
        if num_mes == gasto[2][3:5]:
            gastos_filtrados.append(gasto)

    for columna in gastos_filtrados:
        if columna[5] == 'Activo':
            gastos_Tabla.insert('',0,values=(columna[0],columna[1],columna[2],columna[3]))
        
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
    upd_Date_entry_expense = DateEntry(expense_container,date_pattern='dd/mm/yyyy')
    upd_Date_entry_expense.grid(row=2,column= 1,padx=10,pady=10)
    
    Label(expense_container,text='Total comprado').grid(row=3,column=0,padx=10,pady=10)
    upd_total_Entry = Entry(expense_container)
    upd_total_Entry.grid(row=3,column=1,padx=10,pady=10)
    
    Button(expense_container,text='Actualizar',command=Update_expense_function).grid(row=4,column=0,padx=10,pady=10)
    
    Button(expense_container,text='Regresar').grid(row=4,column=1,padx=10,pady=10)
    
def Update_expense_function():
    concept = upd_concept_Entrty.get()
    date_expense = upd_Date_entry_expense.get()
    total_expense = upd_total_Entry.get()
    
    if concept != '' and date_expense != '' and total_expense != '':
        Update_Expense(concept,date_expense,total_expense,id_expense)


            

main_screen()


