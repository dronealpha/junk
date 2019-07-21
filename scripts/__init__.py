#Autor:Diego Lopes Da Silva
#Data:02/05/2019
#Descrição:Script para inicializar sistema

from ExecutaServico import * #contem funções de execução de serviço rest
import requests #trabalhar com serviços http
from CargaBanco import * #objetos para trabalhar com banco
import time #trabalha com time
from ComandosSQL import * #String de comandos


if __name__ == "__main__":
	while(True):
	    print("Inicializando consumo de serviço")

	    runcon = ExecutaConsumo('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=','AGRO3.SAO','R1RR0LQAC23622C9','15')
	    cod = runcon.retornaRequestJson(BaixaJson(),runcon.getRequisicao())
	    cargaacao = ComandosStringSql()

	    if(cod == 0):
	    	print("Erro ao efetuar requisição")
	    else:
	    	#pega payload de dados
	    	strtrata = literal_eval(str(runcon.payJson(cod)[0]))
	    	
	    	#carga na tabela JYD_JUNKYARD(tabela de valores de ações)
	    	sql_insert_query = cargaacao.cargaAcoesValores(strtrata["1.open"],strtrata["2.high"],strtrata["3.low"],strtrata["4.close"])
	    	banco = CargaTabelas(ComunicacaoBaseDados('localhost','JUNKYARD','root','meteora22'),sql_insert_query)
	    	
	    	#executa a carga na base de dados
	    	banco.ExecutaCarga()
	    	time.sleep(15)
	    