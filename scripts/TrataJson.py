#Autor:Diego Lopes Da Silva
#Data:02/05/2019
#Descrição:Trata informações json para input em banco
import json

#classe json para retornar json
class JsonRequisicao:
    def __init__(self, dadosjson, subst):
        self.dadosjson = dadosjson
        self.subst = subst
    
    #retorna lista contendo json metadados
    def JsonMetadadosDados(self):
        listaMetaData = []
        data = self.dadosjson.content
        strdata = str(data[1:308].decode())
        
        strdata = self.subst.getTextoReplace(strdata,'{','')
        strdata = self.subst.getTextoReplace(strdata,'}','')
        strdata = self.subst.getTextoReplace(strdata,'\n','')
        strdata = self.subst.getTextoReplace(strdata,' ','')
        for linha in strdata.split(':'):
            listaMetaData.append(linha)
        return listaMetaData
    
    #retorna lita com json payload
    def JsonPayload(self):
        listaPayload = []
        data = self.dadosjson.content
        strpay = str(data[366:548].decode())
        strpay = self.subst.getTextoReplace(strpay,'},','}')
        strpay = self.subst.getTextoReplace(strpay,'\n','')
        strpay = self.subst.getTextoReplace(strpay,' ','')
        listaPayload.append(strpay)
        return listaPayload
    
    