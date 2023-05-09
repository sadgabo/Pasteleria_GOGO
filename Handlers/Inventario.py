from Handlers.data_base import Conection



def Consultar_materia(name:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT * FROM INVENTARIO WHERE Nom_Producto = '{name}'")
        materia  = cursor.fetchone()
        
    pasteleria.close()
    return materia


def Consultar_Materias():
    pasteleria = Conection()
    
    materias : list
    with pasteleria.cursor() as cursor:
        cursor.execute('SELECT * FROM INVENTARIO')
        materias = cursor.fetchall()
        
    pasteleria.close()
    return materias


def Nueva_Materia(name:str,cantidad:str,type:str,costo:str):
    pastleria = Conection()
    
    with pastleria.cursor() as cursor:
        cursor.execute(f"INSERT INTO INVENTARIO(Nom_Producto,Stock,Tipo,Precio)VALUES(%s,%s,%s,%s)",(name,cantidad,type,costo))
        
    pastleria.commit()
    pastleria.close()
    
    
def Update_Materia(id:str,name:str,cantidad:str,type:str,costo:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"UPDATE INVENTARIO SET Nom_Producto = '{name}', Stock = '{cantidad}', Tipo = '{type}' Precio = '{costo}' WHERE Id_Materia = '{id}'")
        
    pasteleria.commit()
    pasteleria.close()
    
    
def Delete_Materia(id:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"UPDATE INVENTARIO SET Stock = '0' WHERE Id_Materia = '{id}'")
    
    pasteleria.commit()
    pasteleria.close()
    
    
def Update_Stock(id:str, existencia:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"UPDATE INVENTARIO SET Stock = '{existencia}' WHERE Id_Materia = '{id}'")
    
    pasteleria.commit()
    pasteleria.close()
    