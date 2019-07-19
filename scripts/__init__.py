#Autor:Diego Lopes Da Silva
#Data:02/05/2019
#Descrição:Script para inicializar sistema

from ExecutaServico import *
import requests
from CargaBanco import *
import time 
if __name__ == "__main__":
	while(10):

	    print("Inicializando consumo de serviço")
	    runcon = ExecutaConsumo('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=','AGRO3.SAO','R1RR0LQAC23622C9','15')
	    cod = runcon.retornaRequestJson(BaixaJson(),runcon.getRequisicao())
	    
	    if(cod is None):
	    	print("Erro ao efetuar requisição")
	    else:
	    	#pega payload de 
	    	strtrata = literal_eval(str(runcon.payJson(cod)[0]))
	    	sql_insert_query = """INSERT INTO JYD_ACTIONS(COMPANIES_ID,OPEN_ACTIONS,HIGH_ACTIONS,LOW_ACTIONS,CLOSE_ACTIONS)"""
	    	sql_insert_query = sql_insert_query + 'VALUES(1'+','+strtrata["1.open"]+','+strtrata["2.high"]+','+strtrata["3.low"]+','+strtrata["4.close"]+');'
	    	print(sql_insert_query)
	    	#strtrata = literal_eval(str(runcon.payJson(cod)[0]))
	    	
	    	banco = CargaTabelas(ComunicacaoBaseDados('localhost','JUNKYARD','root','meteora22'),sql_insert_query)
	    	
	    	banco.ExecutaCarga()
	    	time.sleep(15)
	    