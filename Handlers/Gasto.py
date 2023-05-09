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
        cursor.execute("SELECT * FROM Gastos")
        Gastos = cursor.fetchall()
        
    pasteleria.close()
    return Gastos


def Delete_Expense(id:str):
    pasteleria = Conection()
    
    with pasteleria.cursor() as cursor:
        cursor.execute(f"SELECT Estatus FROM Gastos WHERE Id_Gasto = '{id}'")
        status = cursor.fetchone()
        
        if status[0] == 'Activo':
            cursor.execute(f"UPDATE Gastos SET Estatus = 'Inactivo' WHERE Id_Gasto = '{id}'")
        else:
            cursor.execute(f"UPDATE Gastos SET Estatus = 'Activo' WHERE Id_Gasto = '{id}' ")
    
    pasteleria.commit()
    pasteleria.close()
    
    
def Update_Expense(conc:str,date:str,tot:str,id:str):
    pastelertia = Conection()
    
    with pastelertia.cursor() as cursor: 
        cursor.execute(f"UPDATE Gastos SET Concepto = '{conc}',Fecha_Gasto = '{date}',Tot_Comprado = '{tot}' WHERE Id_Gasto = '{id}'")
        
    pastelertia.commit()
    pastelertia.close()
