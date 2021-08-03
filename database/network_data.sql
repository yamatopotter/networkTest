-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 28/02/2021 às 04:59
-- Versão do servidor: 10.3.27-MariaDB-0+deb10u1
-- Versão do PHP: 7.3.27-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `network_data`
--
CREATE DATABASE IF NOT EXISTS `network_data` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `network_data`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `desconexao`
--

DROP TABLE IF EXISTS `desconexao`;
CREATE TABLE `desconexao` (
  `id` int(11) NOT NULL,
  `data` datetime NOT NULL DEFAULT current_timestamp(),
  `interface` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `ping_avg`
--

DROP TABLE IF EXISTS `ping_avg`;
CREATE TABLE `ping_avg` (
  `id` int(11) NOT NULL,
  `perda` tinyint(4) NOT NULL,
  `sucesso` float NOT NULL,
  `recebidos` tinyint(4) NOT NULL,
  `data` datetime NOT NULL DEFAULT current_timestamp(),
  `server` varchar(20) NOT NULL,
  `interface` tinyint(4) NOT NULL COMMENT '0 - ETH | 1 - WLAN'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `ping_total`
--

DROP TABLE IF EXISTS `ping_total`;
CREATE TABLE `ping_total` (
  `id` int(11) NOT NULL,
  `perda` int(11) NOT NULL,
  `sucesso` float NOT NULL,
  `recebidos` int(11) NOT NULL,
  `data` datetime NOT NULL DEFAULT current_timestamp(),
  `server` varchar(20) NOT NULL,
  `interface` int(11) NOT NULL COMMENT '0 - ETH | 1 - WLAN'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `traceroute_avg`
--

DROP TABLE IF EXISTS `traceroute_avg`;
CREATE TABLE `traceroute_avg` (
  `id` int(11) NOT NULL,
  `data` datetime NOT NULL DEFAULT current_timestamp(),
  `host` varchar(20) NOT NULL,
  `sucesso` tinyint(1) NOT NULL DEFAULT 0,
  `interface` tinyint(4) NOT NULL COMMENT '0 - ETH | 1 - WLAN'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;

-- --------------------------------------------------------

--
-- Estrutura para tabela `traceroute_total`
--

DROP TABLE IF EXISTS `traceroute_total`;
CREATE TABLE `traceroute_total` (
  `id` int(11) NOT NULL,
  `data` datetime NOT NULL DEFAULT current_timestamp(),
  `host` varchar(20) NOT NULL,
  `sucesso` tinyint(1) NOT NULL DEFAULT 0,
  `interface` tinyint(4) NOT NULL COMMENT '0 - ETH | 1 - WLAN'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura para tabela `velocidade`
--

DROP TABLE IF EXISTS `velocidade`;
CREATE TABLE `velocidade` (
  `id` int(11) NOT NULL,
  `data` datetime NOT NULL DEFAULT current_timestamp(),
  `download` float NOT NULL,
  `upload` float NOT NULL,
  `jitter` float NOT NULL,
  `delay` float NOT NULL,
  `isp` varchar(60) NOT NULL,
  `server` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `desconexao`
--
ALTER TABLE `desconexao`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `ping_avg`
--
ALTER TABLE `ping_avg`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `ping_total`
--
ALTER TABLE `ping_total`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `traceroute_avg`
--
ALTER TABLE `traceroute_avg`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `traceroute_total`
--
ALTER TABLE `traceroute_total`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `velocidade`
--
ALTER TABLE `velocidade`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `desconexao`
--
ALTER TABLE `desconexao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de tabela `ping_avg`
--
ALTER TABLE `ping_avg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT de tabela `ping_total`
--
ALTER TABLE `ping_total`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=327;
--
-- AUTO_INCREMENT de tabela `traceroute_avg`
--
ALTER TABLE `traceroute_avg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de tabela `traceroute_total`
--
ALTER TABLE `traceroute_total`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
--
-- AUTO_INCREMENT de tabela `velocidade`
--
ALTER TABLE `velocidade`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
