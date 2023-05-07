from Handlers.data_base import Conection



def Pedido_nuevo(past: str, numPers:str , fecha: str, extra: str, Notas: str,id: str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor: 
        cursor.execute("INSERT INTO Pedidos(Tipo_Pastel,Num_Personas,Fecha_Entrega,Extras,Notas,Id_Cliente2)VALUES(%s,%s,%s,%s,%s,%s)",(past,numPers,fecha,extra,Notas,id))
        
    pasteleria.commit()
    pasteleria.close()
    
    

def Consultar_pedidos():
    pasteleria = Conection()
    
    pedidos : list

    with pasteleria.cursor() as cursor: 
        cursor.execute("SELECT * FROM Pedidos")
        pedidos = cursor.fetchall()
    
    pasteleria.close()
    return pedidos