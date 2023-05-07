from Handlers.data_base import Conection



def consulta_materia(concepto:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT * FROM INVENTARIO WHERE Nom_Producto = '{concepto}'")
        materia = cursor.fetchone()
        
        
    pasteleria.close()
    return materia


def Consultar_materia():
    pasteleria = Conection()
    
    materias : list
    with pasteleria.cursor() as cursor:
        cursor.execute("SELECT * FROM INVENTARIO")
        materias = cursor.fetchall()
        
    pasteleria.close()
    return materias


def Nueva_Materia(nombre:str, cant: str,medida:str,costo:str):
    pasteleria = Conection()
    
    
    with pasteleria.cursor() as cursor:
        cursor.execute("INSERT INTO INVENTARIO(Nom_Producto,Stock,Tot_Comprado,Precio)VALUES (%s,%s,%s,%s)",(nombre,cant,medida,costo))
        
    pasteleria.commit()
    pasteleria.close()
    

        