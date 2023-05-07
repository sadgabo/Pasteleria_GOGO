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
