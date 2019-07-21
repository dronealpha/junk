#Autor:Diego Silva
#Data:20/07/2019
#Descrição:Classe que retorna os comandos SQL de interação com tabelas

class ComandosStringSql:

	#metodo retorna comando montado para carga na tabela de ações
	def cargaAcoesValores(self, acOpen,acAlta,acBaixa,acFechada):
		sql_insert_query = """INSERT INTO JYD_ACTIONS(COMPANIES_ID,OPEN_ACTIONS,HIGH_ACTIONS,LOW_ACTIONS,CLOSE_ACTIONS)"""
		sql_insert_query = sql_insert_query + 'VALUES(1'+','+acOpen+','+acAlta+','+acBaixa+','+acFechada+');'
		print(sql_insert_query)
		return sql_insert_query