from Handlers import Conection



def Venta_Nueva(id:str,monto:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"INSERT INTO Ventas(Id_Venta,Monto)VALUES(%s,%s)",(id,monto))
        
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


def Delete_Venta(id:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT Estatus FROM Ventas WHERE Id_Pedido2 = '{id}'")
        estatus = cursor.fetchone()
        
        if estatus[0] == 'Activo':
            cursor.execute(f"UPDATE Ventas SET Estatus = 'Inactivo' WHERE Id_Pedido2 = '{id}'")
        else:
            cursor.execute(f"UPDATE Ventas SET Estatus = 'Activo' WHERE Id_Pedido2 = '{id}'")
            
    pasteleria.commit()
    pasteleria.close()