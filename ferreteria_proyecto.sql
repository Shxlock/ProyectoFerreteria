-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-04-2024 a las 00:03:28
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ferreteria_proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria_producto`
--

CREATE TABLE `categoria_producto` (
  `id_categoria_producto` int(11) NOT NULL,
  `nombre_categoria` varchar(90) NOT NULL,
  `descripcion` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria_producto`
--

INSERT INTO `categoria_producto` (`id_categoria_producto`, `nombre_categoria`, `descripcion`) VALUES
(111, 'categoria 1', 'awdawd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `nit_cliente` int(11) NOT NULL,
  `nombre_cliente` varchar(90) NOT NULL,
  `email_cliente` varchar(90) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`nit_cliente`, `nombre_cliente`, `email_cliente`) VALUES
(1111111113, 'Cliente 1', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalles_facturas`
--

CREATE TABLE `detalles_facturas` (
  `codigo_detalles` varchar(10) NOT NULL,
  `codigo_factura` int(11) NOT NULL,
  `codigo_producto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_unitario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalles_facturas`
--

INSERT INTO `detalles_facturas` (`codigo_detalles`, `codigo_factura`, `codigo_producto`, `cantidad`, `precio_unitario`) VALUES
('28AA22AA', 4280, 1111, 2, 2500),
('CEFF44A9', 3301, 1111, 2, 2500),
('DFCF92A9', 4747, 1111, 5, 2500),
('E69F3068', 6029, 1111, 5, 2500);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `cedula_empleado` int(11) NOT NULL,
  `nombre_empleado` varchar(191) NOT NULL,
  `telefono` int(12) NOT NULL,
  `email` varchar(255) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `direccion` varchar(120) NOT NULL,
  `fecha_insercion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`cedula_empleado`, `nombre_empleado`, `telefono`, `email`, `apellido`, `direccion`, `fecha_insercion`) VALUES
(1111111111, 'Euclides', 2147483647, 'awdawd@gmail.com', 'wadawd', 'awdawd', '2024-04-03 21:54:58');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `codigo_factura` int(11) NOT NULL,
  `tipo_de_pago` varchar(90) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `turno` varchar(49) NOT NULL,
  `fecha` date NOT NULL,
  `nit_cliente` int(11) NOT NULL,
  `cedula_empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `factura`
--

INSERT INTO `factura` (`codigo_factura`, `tipo_de_pago`, `email`, `turno`, `fecha`, `nit_cliente`, `cedula_empleado`) VALUES
(3301, 'Efectivo', NULL, 'Mañana', '2024-04-03', 1111111113, 1111111111),
(4280, 'Efectivo', NULL, 'Mañana', '2024-04-03', 1111111113, 1111111111),
(4747, 'Efectivo', NULL, 'Mañana', '2024-04-03', 1111111113, 1111111111),
(6029, 'Efectivo', NULL, 'Mañana', '2024-04-03', 1111111113, 1111111111);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `codigo_producto` int(11) NOT NULL,
  `nombre_producto` varchar(90) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `precio_unitario` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `nit_proveedor` int(11) NOT NULL,
  `fecha_vencimiento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`codigo_producto`, `nombre_producto`, `cantidad`, `descripcion`, `precio_unitario`, `id_categoria`, `nit_proveedor`, `fecha_vencimiento`) VALUES
(1111, 'producto 1', 3, 'awdawd', 2500, 111, 111, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `nit_proveedor` int(11) NOT NULL,
  `nombre_proveedor` varchar(90) NOT NULL,
  `telefono_proveedor` int(11) NOT NULL,
  `email_proveedor` varchar(90) NOT NULL,
  `direccion_proveedor` varchar(90) NOT NULL,
  `ciudad_proveedor` varchar(90) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`nit_proveedor`, `nombre_proveedor`, `telefono_proveedor`, `email_proveedor`, `direccion_proveedor`, `ciudad_proveedor`) VALUES
(111, 'proveedor1 ', 2147483647, 'proveedor1@gmail.com', 'awdwad', 'Cúcuta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `user` varchar(191) NOT NULL,
  `password` varchar(191) NOT NULL,
  `salt` varchar(255) NOT NULL,
  `rol` varchar(50) NOT NULL,
  `cedula_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`user_id`, `user`, `password`, `salt`, `rol`, `cedula_usuario`) VALUES
(1, 'admin1', '$2b$12$fZMckAhEkVzJOizoBOlvjert6bmQrSqo2dcpPQI8OHT/jSbywvOCu', '$2b$12$fZMckAhEkVzJOizoBOlvje', 'Administrador', 1111111111);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria_producto`
--
ALTER TABLE `categoria_producto`
  ADD PRIMARY KEY (`id_categoria_producto`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`nit_cliente`);

--
-- Indices de la tabla `detalles_facturas`
--
ALTER TABLE `detalles_facturas`
  ADD PRIMARY KEY (`codigo_detalles`),
  ADD KEY `codigo_factura` (`codigo_factura`),
  ADD KEY `codigo_producto` (`codigo_producto`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`cedula_empleado`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`codigo_factura`),
  ADD KEY `nit_cliente` (`nit_cliente`),
  ADD KEY `cedula_empleado` (`cedula_empleado`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`codigo_producto`),
  ADD KEY `id_categoria` (`id_categoria`),
  ADD KEY `nit_proveedor` (`nit_proveedor`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`nit_proveedor`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `cedula_usuario` (`cedula_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `detalles_facturas`
--
ALTER TABLE `detalles_facturas`
  ADD CONSTRAINT `detalles_facturas_ibfk_1` FOREIGN KEY (`codigo_factura`) REFERENCES `factura` (`codigo_factura`) ON DELETE CASCADE,
  ADD CONSTRAINT `detalles_facturas_ibfk_2` FOREIGN KEY (`codigo_producto`) REFERENCES `producto` (`codigo_producto`) ON DELETE CASCADE;

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`nit_cliente`) REFERENCES `cliente` (`nit_cliente`) ON DELETE CASCADE,
  ADD CONSTRAINT `factura_ibfk_2` FOREIGN KEY (`cedula_empleado`) REFERENCES `empleado` (`cedula_empleado`) ON DELETE CASCADE;

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categoria_producto` (`id_categoria_producto`) ON DELETE CASCADE,
  ADD CONSTRAINT `producto_ibfk_2` FOREIGN KEY (`nit_proveedor`) REFERENCES `proveedor` (`nit_proveedor`) ON DELETE CASCADE;

--
-- Filtros para la tabla `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`cedula_usuario`) REFERENCES `empleado` (`cedula_empleado`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
