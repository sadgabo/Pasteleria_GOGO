from Handlers.data_base import Conection



def Gasto_Nuevo(concept:str, fecha:str, Total:str,id_Materia:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute("INSERT INTO Gastos(Concepto,Fecha_Gasto,Tot_Comprado,Id_Materia)VALUES(%s,%s,%s,%s) ",(concept,fecha,Total,id_Materia))
    
    pasteleria.commit()
    pasteleria.close()
    
    
def consulta_gasto(id:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor: 
        cursor.execute(f"SELECT * Cliente WHERE Id_Gasto = '{id}'")
        cliente = cursor.fetchone()
        
    pasteleria.close()
    return cliente




def Consultar_Gastos():
    pasteleria = Conection()
    
    Gastos: list
    
    with pasteleria.cursor() as cursor:
        cursor.execute("SELECT * FROM Cliente")
        clientes = cursor.fetchall()
        
    pasteleria.close()
    return clientes

