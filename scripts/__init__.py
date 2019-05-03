#Autor:Diego Lopes Da Silva
#Data:02/05/2019
#Descrição:Script para inicializar sistema

from ExecutaServico import *

if __name__ == "__main__":
    print("Inicializando consumo de serviço")
    rodarservico = ServicoConsumir()
    rodarservico.Servico()
    