from Handlers.data_base import Conection



def Pedido_nuevo(past: str, numPers:str , fecha: str, extra: str, Notas: str,id: str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor: 
        cursor.execute("INSERT INTO Pedidos(Tipo_Pastel,Num_Personas,Fecha_Entrega,Extras,Notas,Id_Cliente2)VALUES(%s,%s,%s,%s,%s,%s)",(past,numPers,fecha,extra,Notas,id))
        
    pasteleria.commit()
    pasteleria.close()
    
def Consultar_pedido(id:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT * FROM Pedidos WHERE Id_Pedido = '{id}'")
        pedido = cursor.fetchone()
        
    pasteleria.close()
    return pedido

def Consultar_pedidos():
    pasteleria = Conection()
    
    pedidos : list

    with pasteleria.cursor() as cursor: 
        cursor.execute("SELECT * FROM Pedidos")
        pedidos = cursor.fetchall()
    
    pasteleria.close()
    return pedidos

def Consulta_mes(mes:str):
    pasteleria = Conection()
    
    pedidos : list 
    with pasteleria.cursor() as cursor: 
        cursor.execute(f"SELECT * FROM Pedidos WHERE MONTH(Fecha_Entrega) = '{mes}'")
        pedidos = cursor.fetchall()
        
    pasteleria.close()
    return pedidos

def Update_Order(id: str, pastel:str,pers:str,fecha:str,extra:str,notas:str):
    pasteleria = Conection()
        
    with pasteleria.cursor() as cursor:
        cursor.execute(f"UPDATE Pedidos SET Tipo_Pastel = '{pastel}' , Num_Personas = '{pers}', Fecha_Entrega = '{fecha}', Extras = '{extra}', Notas = '{notas}' WHERE Id_Pedido = '{id}'")
            
    pasteleria.commit()
    pasteleria.close()
    
    
    
def delete_Order(id: str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT Estatus FROM Pedidos WHERE id_Pedido = '{id}'")
        status = cursor.fetchone()
        
        if status[0] == 'Activo':
            cursor.execute(f"UPDATE Pedidos SET Estatus = 'Inactivo' WHERE Id_Pedido = '{id}'")
        else:
            cursor.execute(f"UPDATE Pedidos SET Estatus = 'Activo' WHERE Id_Pedido = '{id}'")
            
    pasteleria.commit()
    pasteleria.close()
    
    
            
            
def Liquidar_Pedido(id:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT * FROM Pedidos WHERE Id_Pedido = '{id}'")
        estado = cursor.fetchone()
        
        if estado[0] == 'Liquidado':
            cursor.execute(f"UPDATE Pedidos SET Estado = 'Pendiente' WHERE Id_Pedido = '{id}'")
        else:
            cursor.execute(f"UPDATE Pedidos SET Estado = 'Liquidado' WHERE Id_Pedido = '{id}'")
            
    pasteleria.commit()
    pasteleria.close()
    
    
    