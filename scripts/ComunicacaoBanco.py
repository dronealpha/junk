#Autor:Diego Silva
#Data:16/07/2019
#Descrição:Script que retorna objeto para conexão com banco de dados

#importando biblioteca para comunicação com mysql
import mysql.connector

#classe de interação com banco
class ComunicacaoBaseDados:
    def __init__(self, host, database, user, passwd):
        self.__host = host
        self.__database = database
        self.__user = user
        self.__passwd = passwd
        self.__con = None

    #property para retornar objeto de conexão
    @property
    def con(self):
        con =  mysql.connector.connect(host=self.__host,
                                 database=self.__database,
                                 user=self.__user,
                                 password=self.__passwd)
        return con


#conexao = ComunicacaoBaseDados('localhost','JUNKYARD','root','meteora22')
#
#print(conexao.con)


