#Autor:Diego Lopes Da Silva
#Data:02/05/2019
#Descrição:Pega json via rest

import requests

#classe para montar request json
class LinkJson:
	#construtor passando url, empresa , chave e tempo de requisição desejado
	def __init__(self, url, empresa, chave, time):
		self.__url = url
		self.__empresa = empresa
		self.__chave = chave
		self.__time = time

    #método get retorna link pronto
	def getLinkWebService(self):
		return str(self.__url+self.__empresa+'&interval='+self.__time+'min&apikey='+self.__chave)

#classe para baixar arquivos json
class BaixaJson:
	#método retorna objeto json com os dados da 
	def VerificaLinkBolsa(self, url):
		return requests.get(url)
