
USE Pasteleria


--Tabla de los clientes el cual se usa para ligarlo a los pedidos 
CREATE TABLE Cliente(
    Id_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    Nombre_Cliente VARCHAR(35) NOT NULL ,
    Telefono VARCHAR(12) NOT NULL
    Estatus ENUM('Activo','Inactivo') NOT NULL DEFAULT  'Activo'

);

--Tabla de pedidos , la cual guarda los datos del pedido , ademas de dos estados para manejar de mejor manera otras tablas 
CREATE TABLE Pedidos(
    Id_Pedido INT  AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Tipo_Pastel VARCHAR(15) NOT NULL,
    Num_Personas INT NOT NULL,
    Fecha_Entrega DATE NOT NULL,
    Extras VARCHAR(30) ,
    Notas VARCHAR(50) NOT NULL,
    Id_Cliente2 INT ,
    Estado ENUM ('Pendiente', 'Liquidado') NOT NULL DEFAULT 'Pendiente',
    Estatus ENUM('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
    FOREIGN KEY (Id_Cliente2) REFERENCES Cliente(Id_Cliente)
);


--tabla de ventas en la cual se guardan los pedidos liquidados ademas del monto total
CREATE TABLE Ventas(
    Id_Venta INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Monto FLOAT NOT NULL,
    Id_Pedido2 INT NOT NULL,
    Pastel VARCHAR(20) NOT NULL,
    Personas INT NOT NULL,
    Estatus ENUM('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
    Fecha_Venta DATE NOT NULL,
    FOREIGN KEY (Id_Pedido2) REFERENCES Pedidos(Id_Pedido)
);

--tabla que guarda elinventario de materias que se tiene 
CREATE TABLE INVENTARIO(
    Id_Materia INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Nom_Producto VARCHAR(15) NOT NULL,
    Stock INT NOT NULL,
    Precio FLOAT NOT NULL,
    Tipo VARCHAR(20) NOT NULL
);


--tabla de gastos que aumenta las existencias segun lo comprado 
CREATE TABLE Gastos(
    Id_Gasto INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Concepto VARCHAR(30) NOT NULL,
    Fecha_Gasto DATE NOT NULL,
    Tot_Comprado INT NOT NULL,
    Precio FLOAT NOT NULL,
    Id_Materia INT,
    Estatus ENUM('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
    FOREIGN KEY (Id_Materia) REFERENCES INVENTARIO(Id_Materia)
);