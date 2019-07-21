#Autor:Diego Lopes Da Silva
#Data:02/05/2019
#Descrição:Script princial para execução de metodos e classes

from PegaJson import *
from TrataJson import *
from TrataString import *
import json
from ast import literal_eval
class ServicoConsumir:
    
    def __init__(self, linkjson,empresa,chave, tempo):
        self.__linkjson = linkjson
        self.__empresa = empresa
        self.__chave = chave
        self.__tempo = tempo

    def getLink(self):
        return self.__linkjson

    def getEmpresa(self):
        return self.__empresa

    def getChave(self):
        return self.__chave

    def getTempo(self):
        return self.__tempo
        
        

  
class  ExecutaConsumo(ServicoConsumir):
    def __init__(self,linkjson,empresa,chave,tempo):
        super().__init__(linkjson,empresa,chave,tempo)

    def getRequisicao(self):
        return LinkJson(self.getLink(),self.getEmpresa(),self.getChave(),self.getTempo())

    def retornaRequestJson(self, downjson, pega):

        #instanciando classe para gerar link da utl bolsa
        #linkbolsa = LinkJson('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=','AGRO3.SAO','R1RR0LQAC23622C9','15')

        #instanciando classe para pegar json
        return downjson.VerificaLinkBolsa(pega.getLinkWebService())

    def payJson(self, cod):
        #valida se se foi bem sucedida a requisição ou apresentou erros https
        if(cod.status_code==200):
            resp = JsonRequisicao(cod, TrataTexto())
            return resp.JsonPayload()
        else:
            return 0
           


