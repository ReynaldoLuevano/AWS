-- MySQL dump for clientes table
-- Database: sample_db

CREATE DATABASE IF NOT EXISTS sample_db;
USE sample_db;

DROP TABLE IF EXISTS `clientes`;

CREATE TABLE `clientes` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `clientes` (`customer_id`, `customer_name`, `last_name`, `address`, `phone`) VALUES
(1, 'Juan', 'García', 'Calle Principal 123, Madrid', '+34-91-123-4567'),
(2, 'María', 'López', 'Av. Libertador 456, Barcelona', '+34-93-234-5678'),
(3, 'Carlos', 'Martínez', 'Plaza Mayor 789, Valencia', '+34-96-345-6789'),
(4, 'Ana', 'Rodríguez', 'Calle Sol 321, Sevilla', '+34-95-456-7890'),
(5, 'Luis', 'Fernández', 'Av. Constitución 654, Bilbao', '+34-94-567-8901');