/*
Autor:Diego Silva
Data:07/05/2019
Descrição:Script para criação de base de dados
*/

--CRIANDO BASE DE DADOS
CREATE DATABASE JUNKYARD;

--CARREGANDO TABELAS
USE JUNKYARD;


--CRIANDO TABELA PARA NOME DE EMPRESAS
CREATE TABLE JYD_COMPANIES(
	ID_COMPANIES INT NOT NULL AUTO_INCREMENT,
	NAME_COMPANIES VARCHAR(255) NOT NULL,
	NICK_NAME_COMPANIES VARCHAR(255) NOT NULL,
	PRIMARY KEY(ID_COMPANIES)
);

--CRIANDO TABELA DE AÇÕES
CREATE TABLE JYD_ACTIONS(
	ID_ACTIONS INT NOT NULL AUTO_INCREMENT,
	COMPANIES_ID INT NOT NULL,
	OPEN_ACTIONS DECIMAL(18,4),
	HIGH_ACTIONS DECIMAL(18,4),
	LOW_ACTIONS DECIMAL(18,4),
	CLOSE_ACTIONS DECIMAL(18,4),
	PRIMARY KEY(ID_ACTIONS)
);

--CRIANDO RELACIONAMENTO ENTRE TABELAS
ALTER TABLE JYD_ACTIONS ADD FOREIGN KEY (COMPANIES_ID) REFERENCES JYD_COMPANIES(ID_COMPANIES); 

COMMIT;

--CARGA COM NOME DA EMPRESAS COM AÇÕES NA BOLSA
INSERT INTO JYD_COMPANIES(NAME_COMPANIES,NICK_NAME_COMPANIES) VALUES('AGRO3.SAO','BRASILAGRO ON');
INSERT INTO JYD_COMPANIES(NAME_COMPANIES,NICK_NAME_COMPANIES) VALUES('ABCB4.SAO','ABC BRASIL PN');
INSERT INTO JYD_COMPANIES(NAME_COMPANIES,NICK_NAME_COMPANIES) VALUES('ABEV3.SAO','AMBEV S/A ON');
INSERT INTO JYD_COMPANIES(NAME_COMPANIES,NICK_NAME_COMPANIES) VALUES('CPLE6.SAO','COPEL PNB');
INSERT INTO JYD_COMPANIES(NAME_COMPANIES,NICK_NAME_COMPANIES) VALUES('EQTL3.SAO','EQUATORIAL ON');
INSERT INTO JYD_COMPANIES(NAME_COMPANIES,NICK_NAME_COMPANIES) VALUES('LIGT3.SAO','LIGHT S/A ON');
INSERT INTO JYD_COMPANIES(NAME_COMPANIES,NICK_NAME_COMPANIES) VALUES('PETR3.SAO','PETROBRAS ON');

COMMIT;


--TABELA PARA ARMAZ
CREATE TABLE JYD_HISTORY_SCRIPT(
	ID_HISTORY INT NOT NULL AUTO_INCREMENT,
	DESC_HISTORY_SCRIPT VARCHAR(255) NOT NULL,
	SCRIPT_HISTORY VARCHAR(255) NOT NULL,
	PRIMARY KEY(ID_HISTORY)
);

INSERT INTO JYD_HISTORY_SCRIPT(DESC_HISTORY_SCRIPT,SCRIPT_HISTORY) VALUES('SCRIPT DE CRIAÇÃO DE TABELAS BASICAS','1.0.0.0');

COMMIT;




