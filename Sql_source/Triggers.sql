USE Pasteleria

DELIMITER $$
CREATE TRIGGER check_fecha_entrega BEFORE INSERT ON Pedidos
FOR EACH ROW
BEGIN
    DECLARE allowed_date DATE;
    SET allowed_date = DATE_ADD(CURDATE(), INTERVAL 7 DAY);
    
    IF NEW.Fecha_Entrega < allowed_date THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La fecha de entrega debe tener una diferencia de una semana con respecto al día actual';
    END IF;
END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER prevent_fecha_entrega BEFORE INSERT ON Pedidos
FOR EACH ROW
BEGIN
    IF NEW.Fecha_Entrega < CURDATE() THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La fecha de entrega no puede ser menor al día actual';
    END IF;
END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER prevent_update_fecha BEFORE UPDATE ON Pedidos
FOR EACH ROW
BEGIN
    DECLARE allowed_date DATE;
    SET allowed_date = DATE_ADD(CURDATE(), INTERVAL 7 DAY); -- Cambiar 7 por el número de días permitidos
    
    IF NEW.Fecha_Entrega < allowed_date THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se permite actualizar a una fecha anterior a la fecha actual más 7 días';
    END IF;
END$$
DELIMITER ;
