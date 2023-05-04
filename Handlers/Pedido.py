from Handlers.data_base import Conection



def cliente_nuevo(name: str, telefono: str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute("INSERT INTO Cliente(Nombre_Cliente,Telefono)VALUES(%s,%s)",(name, telefono))
        
    pasteleria.commit()
    pasteleria.close()
    
    
def consulta_cliente(telef: str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT id_Cliente FROM Cliente WHERE Telefono = '{telef}'")
        id = cursor.fetchone()
    
    pasteleria.close()
    return   id





def Pedido_nuevo(past: str, numPers:int , fecha: str, extra: str, Notas: str,id: int):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor: 
        cursor.execute("INSERT INT Pedidos(Tipo_Pastel,Num_Personas,Fecha_Entrega,Extras,Notas,Id_Cliente)VALUES(%s,%s,%s,%s,%s,%s)",(past,numPers,fecha,extra,Notas,id))
        
    pasteleria.commit()
    pasteleria.close()
    
    
    
