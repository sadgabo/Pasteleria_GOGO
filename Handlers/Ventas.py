from Handlers.data_base import Conection



def Venta_Nueva(monto:str,pastel:str,personas:str,fecha:str,id:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"INSERT INTO Ventas(Monto,Pastel,Personas,Fecha_Venta,Id_Pedido2)VALUES(%s,%s,%s,%s,%s)",(monto,pastel,personas,fecha,id))
        
    pasteleria.commit()
    pasteleria.close()
    

def Consultar_ventas():
    pasteleria = Conection()
    
    ventas : list
    with pasteleria.cursor() as cursor:
        cursor.execute("SELECT * FROM Ventas")
        ventas = cursor.fetchall()
        
    pasteleria.close()
    return ventas

def Consultar_Venta(id:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT * WHERE Id_Pedido2 = '{id}'")
        venta= cursor.fetchone()
    
    pasteleria.close()
    return venta

def Consulta_Venta_Mes(mes: str):
    pasteleria = Conection()
    
    ventas = list
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT * FROM Ventas WHERE MONTH(Fecha_Venta) = '{mes}'")
        ventas = cursor.fetchall()
        
    pasteleria.close()
    return ventas

def Delete_Venta(id:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT Estatus FROM Ventas WHERE Id_Venta = '{id}'")
        estatus = cursor.fetchone()
        
        if estatus[0] == 'Activo':
            cursor.execute(f"UPDATE Ventas SET Estatus = 'Inactivo' WHERE Id_Venta = '{id}'")
        else:
            cursor.execute(f"UPDATE Ventas SET Estatus = 'Activo' WHERE Id_Venta = '{id}'")
            
    pasteleria.commit()
    pasteleria.close()