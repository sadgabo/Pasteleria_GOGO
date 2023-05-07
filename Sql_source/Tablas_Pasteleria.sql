CREATE TABLE Cliente(
    Id_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    Nombre_Cliente VARCHAR(35) NOT NULL ,
    Telefono VARCHAR(12) NOT NULL

);

CREATE TABLE Pedidos(
    Id_Pedido INT  AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Tipo_Pastel VARCHAR(10) NOT NULL,
    Num_Personas INT NOT NULL,
    Fecha_Entrega VARCHAR(10) NOT NULL,
    Extras VARCHAR(30) ,
    Notas VARCHAR(50) NOT NULL,
    Id_Cliente2 INT ,
    FOREIGN KEY (Id_Cliente2) REFERENCES Cliente(Id_Cliente)
);


CREATE TABLE Ventas(
    Monto FLOAT NOT NULL,
    Id_Pedido2 INT,
    FOREIGN KEY (Id_Pedido2) REFERENCES Pedidos(Id_Pedido)
);

CREATE TABLE INVENTARIO(
    Id_Materia INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Nom_Producto VARCHAR(15) NOT NULL,
    Stock INT NOT NULL,
    Precio FLOAT NOT NULL
);

CREATE TABLE Gastos(
    Id_Gasto INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Concepto VARCHAR(30) NOT NULL,
    Fecha_Gasto VARCHAR(12) NOT NULL,
    Tot_Comprado INT NOT NULL,
    Id_Materia INT,
    FOREIGN KEY (Id_Materia) REFERENCES INVENTARIO(Id_Materia)
);