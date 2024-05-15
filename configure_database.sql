-- Criação do banco de dados ParkAssistent
CREATE DATABASE IF NOT EXISTS ParkAssistent;

-- Utilização do banco de dados ParkAssistent
USE ParkAssistent;

-- Tabela para armazenar informações dos clientes
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    placa VARCHAR(7) NOT NULL
);

-- Tabela para armazenar informações das empresas
CREATE TABLE empresa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_empresa VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    bairro VARCHAR(255) NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    vagas INT NOT NULL,
    tipo_preco ENUM('Por hora', 'Diária') NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    tipo ENUM('Cliente', 'Empresa') NOT NULL
);