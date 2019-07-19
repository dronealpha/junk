#Autor:Diego Silva
#Data:16/07/2019
#Descrição:Classe para carga em banco de dados

#importando biblioteca para comunicação com mysql
import mysql.connector

#biblioteca para lidar com erros de conexão com banco 
from mysql.connector import Error

#importando modulos
from ComunicacaoBanco import ComunicacaoBaseDados

#classe mãe que recebe dados de conexão
class BancoConexao:

	def __init__(self, conBanco, comandoInsert):
		self.__conBanco = conBanco
		self.__comandoInsert = comandoInsert

	#retorna objeto com conexão do banco
	def getCon(self):
		return self.__conBanco

	#retorna comando sql
	def getCom(self):
		return self.__comandoInsert

#classe para carga em banco de dados
class CargaTabelas(BancoConexao):
	def __init__ (self, conBanco, comandoInsert):
		super().__init__(conBanco,comandoInsert)
	
	def ExecutaCarga(self):
		try:
			com = self.getCon()
			conexao = com.con
			if conexao.is_connected():
				print("Comunicando com base de dados")
				cursor = conexao.cursor()
				result  = cursor.execute(self.getCom())
				conexao.commit()
		except Error as e :
			print ("Erro de comunicação com banco de dados", e)
		finally:
		#closing database conexao.
		    if(conexao.is_connected()):
		    	cursor.close()
		    	conexao.close()
		    	print("Conexão finalizada")

#sql_insert_query = """INSERT INTO JYD_ACTIONS(COMPANIES_ID,OPEN_ACTIONS,HIGH_ACTIONS,LOW_ACTIONS,CLOSE_ACTIONS) VALUES(1,16.8500,16.8500,16.8500,16.8500);"""
#banco = CargaTabelas(ComunicacaoBaseDados('localhost','JUNKYARD','root','meteora22'),sql_insert_query)
#banco.ExecutaCarga()
