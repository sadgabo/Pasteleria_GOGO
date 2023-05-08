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
        cursor.execute(f"SELECT * FROM Cliente WHERE Telefono = '{telef}'")
        cliente = cursor.fetchone()
    
    pasteleria.close()
    return   cliente


def Consultar_Clientes():
    pasteleria = Conection()
    
    clientes: list
    with pasteleria.cursor() as cursor:
        cursor.execute("SELECT * FROM Cliente ")
        clientes = cursor.fetchall()
        
    pasteleria.close()
    return clientes  



def Update_Cliente(id:str,name:str,phone:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"UPDATE Cliente SET Nombre_Cliente = '{name}',Telefono = '{phone}' WHERE Id_Cliente = '{id}' ")
    
    pasteleria.commit()
    pasteleria.close()
    
    
def delete_cliente(id: str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT Estatus FROM Cliente WHERE Id_Cliente = '{id}' ")
        estatus = cursor.fetchone()
        
        if estatus[0] == 'Activo':
            cursor.execute(f"UPDATE Cliente SET Estatus = 'Inactivo' WHERE Id_Cliente = '{id}' ")
        else:
            cursor.execute(f"UPDATE Cliente SET Estatus = 'Activo' WHERE Id_Cliente = '{id}' ")
            
    pasteleria.commit()
    pasteleria.close()
    
        
        