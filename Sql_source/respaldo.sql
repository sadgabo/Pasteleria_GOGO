-- MariaDB dump 10.19-11.1.0-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: Pasteleria
-- ------------------------------------------------------
-- Server version	11.1.0-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente` (
  `Id_Cliente` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_Cliente` varchar(35) NOT NULL,
  `Telefono` varchar(12) NOT NULL,
  `Estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  PRIMARY KEY (`Id_Cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES
(1,'Gerardo','523311510613','Activo'),
(2,'Abraham ','523327476525','Activo'),
(3,'','','Activo'),
(4,'Perla','523312278893','Activo'),
(5,'Elizabeth','523323332190','Activo'),
(6,'Adriana','523335961000','Activo'),
(7,'Perla','52331227889','Activo');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gastos`
--

DROP TABLE IF EXISTS `gastos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gastos` (
  `Id_Gasto` int(11) NOT NULL AUTO_INCREMENT,
  `Concepto` varchar(30) NOT NULL,
  `Fecha_Gasto` varchar(12) NOT NULL,
  `Tot_Comprado` int(11) NOT NULL,
  `Id_Materia` int(11) DEFAULT NULL,
  `Estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  PRIMARY KEY (`Id_Gasto`),
  KEY `Id_Materia` (`Id_Materia`),
  CONSTRAINT `gastos_ibfk_1` FOREIGN KEY (`Id_Materia`) REFERENCES `inventario` (`Id_Materia`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gastos`
--

LOCK TABLES `gastos` WRITE;
/*!40000 ALTER TABLE `gastos` DISABLE KEYS */;
INSERT INTO `gastos` VALUES
(1,'Harina','17/05/2023',5000,28,'Inactivo'),
(2,'Huevos','25/05/2023',85,31,'Inactivo'),
(3,'Vainilla','17/05/2023',200,53,'Inactivo'),
(4,'Nuez','26/05/2023',350,48,'Inactivo'),
(5,'Leche','18/05/2023',2000,32,'Inactivo'),
(6,'Cocoa','18/05/2023',500,35,'Inactivo'),
(7,'Cocoa','25/05/2023',1000,35,'Inactivo'),
(8,'huevos','25/05/2023',50,32,'Activo'),
(9,'Huevos','24/05/2023',40,31,'Activo');
/*!40000 ALTER TABLE `gastos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventario` (
  `Id_Materia` int(11) NOT NULL AUTO_INCREMENT,
  `Nom_Producto` varchar(30) NOT NULL,
  `Stock` int(11) NOT NULL,
  `Precio` float NOT NULL,
  `Tipo` varchar(20) NOT NULL,
  PRIMARY KEY (`Id_Materia`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario`
--

LOCK TABLES `inventario` WRITE;
/*!40000 ALTER TABLE `inventario` DISABLE KEYS */;
INSERT INTO `inventario` VALUES
(28,'Harina',44000,841,'gramos'),
(29,'Mantequilla',1000,62,'gramos'),
(30,'Azucar',10000,273,'gramos'),
(31,'Huevos',52,40,'Piezas'),
(32,'Leche',3000,43.5,'mililitros'),
(33,'Polvo para hornear',1000,20,'gramos'),
(34,'Vainilla',1000,89,'mililitros'),
(35,'Cocoa',2500,226,'gramos'),
(36,'Chocolate',2500,280,'gramos'),
(37,'Aceite',946,55,'mililitros'),
(38,'Bicarbonato',1000,12,'gramos'),
(39,'Vinagre',1000,17,'mililitros'),
(40,'Limon',20,18,'piezas'),
(41,'Agua',19000,40,'mililitros'),
(42,'Azucar moscabado',10000,220,'gramos'),
(43,'Zanahoria',1000,10,'gramos'),
(44,'Canela en polvo',50,15,'gramos'),
(45,'Nuez moscabado',50,30,'gramos'),
(46,'Jengibre',50,26,'gramos'),
(47,'Clavo',50,20,'gramos'),
(48,'Nuez',1000,350,'gramos'),
(49,'Queso crema',180,38.5,'gramos'),
(50,'Azucar glass',500,15.5,'gramos'),
(51,'Manteca vegetal',1000,82,'gramos'),
(52,'Merengue en polvo',250,139,'gramos'),
(53,'Vainilla',150,14.5,'mililitros'),
(54,'Leche en polvo',0,63,'gramos');
/*!40000 ALTER TABLE `inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pedidos` (
  `Id_Pedido` int(11) NOT NULL AUTO_INCREMENT,
  `Tipo_Pastel` varchar(15) NOT NULL,
  `Num_Personas` int(11) NOT NULL,
  `Fecha_Entrega` varchar(10) NOT NULL,
  `Extras` varchar(30) DEFAULT NULL,
  `Notas` varchar(50) NOT NULL,
  `Id_Cliente2` int(11) DEFAULT NULL,
  `Estado` enum('Pendiente','Liquidado') NOT NULL DEFAULT 'Pendiente',
  `Estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  PRIMARY KEY (`Id_Pedido`),
  KEY `Id_Cliente2` (`Id_Cliente2`),
  CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`Id_Cliente2`) REFERENCES `cliente` (`Id_Cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
INSERT INTO `pedidos` VALUES
(1,'Tres leches',30,'27/05/2023','Si','bonito',1,'Pendiente','Activo'),
(2,'Volteado',50,'08/05/2023','Si','se',1,'Pendiente','Activo'),
(3,'Tres leches',30,'27/05/2023','Si','bonito',1,'Pendiente','Activo'),
(4,'Tres leches',30,'27/05/2023','Si','bonito',1,'Pendiente','Activo'),
(5,'Tres leches',30,'27/05/2023','Si','bonito',1,'Liquidado','Activo'),
(6,'Tres leches',30,'27/05/2023','Si','bonito',1,'Liquidado','Activo'),
(7,'Tres leches',30,'27/05/2023','Si','bonito',1,'Liquidado','Activo');
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER update_fecha AFTER UPDATE ON Pedidos
            FOR EACH ROW
            BEGIN
                IF NEW.Fecha_Entrega > CURDATE() THEN
                    UPDATE Pedidos SET Fecha_Entrega = NEW.Fecha_Entrega WHERE Id_Pedido = NEW.Id_Pedido;
                END IF;
            END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ventas` (
  `Id_Venta` int(11) NOT NULL AUTO_INCREMENT,
  `Monto` float NOT NULL,
  `Id_Pedido2` int(11) NOT NULL,
  `Pastel` varchar(20) NOT NULL,
  `Personas` int(11) NOT NULL,
  `Estatus` enum('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
  `Fecha_Venta` varchar(10) NOT NULL,
  PRIMARY KEY (`Id_Venta`),
  KEY `Id_Pedido2` (`Id_Pedido2`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`Id_Pedido2`) REFERENCES `pedidos` (`Id_Pedido`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES
(1,410,5,'Tres leches',30,'Activo',''),
(2,410,3,'Tres leches',30,'Activo','15/05/23'),
(3,410,2,'Tres leches',30,'Activo','15/05/23'),
(4,410,7,'Tres leches',30,'Activo','15/05/23'),
(5,410,6,'Tres leches',30,'Inactivo','15/05/23'),
(6,410,5,'Tres leches',30,'Activo','15/05/23');
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-16  1:00:46
