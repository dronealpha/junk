#Autor:Diego Lopes Da Silva
#Data:02/05/2019
#Descrição:Script princial para execução de metodos e classes

from PegaJson import *
from TrataJson import *
from TrataString import *

class ServicoConsumir:
    
    def Servico(self):

        #instanciando classe para gerar link da utl bolsa
        linkbolsa = LinkJson('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=','AGRO3.SAO','R1RR0LQAC23622C9','15')

        #instanciando classe para pegar json
        pega = BaixaJson()
        cod = pega.VerificaLinkBolsa(linkbolsa.getLinkWebService())

        #valida se se foi bem sucedida a requisição ou apresentou erros https
        if(cod.status_code==200):

            resp = JsonRequisicao(cod, TrataTexto())
            print("Metadata")
            print(resp.JsonMetadadosDados())
            print("\nPayload\n")
            print(resp.JsonPayload())
            print("Codigo: {}".format(str(cod.status_code)))
            print("\nRequição bem sucedida!!!\n")

        elif(cod.status_code==404):#erro quando não existe(encontra) pagina

            print("Codigo: {}".format(cod.status_code))
            print("\nRota não localizada\n")

        else:#outros erros

            print("Codigo: {}".format(cod.status_code))
            print("\nErro na aplicação\n")