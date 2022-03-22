import random as rand
from construtor import criaMapa, valormapa, vertice_caminho
import numpy as np
from a_estrela import a_estrela

class Jogo:


    #Testa o objtivo para dar continuidade ao caminho
    def testarObj(self,mapa,tamArray):
        return mapa[tamArray - 1] == 0

    #Gera os caminhos apos um movimento
    def gerar_sucessores(self, estado):
      
        sucessores = []
      
        posicao = estado.index(0)
        expansoes = [self._direita, self._esquerda, self._cima, self._baixo]
        rand.shuffle(expansoes)
      
        for expa in expansoes:
            sucessor = expa(posicao, estado)
            if sucessor is not None: 
              sucessores.append(sucessor)

        return sucessores
     #gera a conta do custo ao mover a peça
    def custo(self, estado_origem, estado_destino):
      
        return estado_origem + estado_destino
      
#====================AREA DE MOVIMENTOS============================

      
    #Move para a esquerda, não deixa mover para areas bloqueadas e atualixa o mapa
      
    def _esquerda(self, posicao, estado_atual):
      
        esquerda = []
        for i in range(len(mapa)):
            if i == 0 or i % C == 0:
                esquerda.append(i)
        if posicao not in esquerda and 0 < estado_atual[posicao-1]:
            sucessor = list(estado_atual)
            sucessor[posicao] = -2
            sucessor[posicao - 1] = 0
            return (tuple(sucessor), "👈",estado_atual[(posicao - 1)])

          
    #Move para a direita, não deixa mover para areas bloqueadas e atualixa o mapa
          
    def _direita(self, posicao, estado_atual):
        direita = []
        for i in range(len(mapa)):
            if (i + 1) % C == 0 :
                direita.append(i)
        if posicao not in direita and 0 < estado_atual[posicao + 1]:      
            sucessor = list(estado_atual)
            sucessor[posicao] = -2
            sucessor[posicao + 1] = 0
            return (tuple(sucessor), "👉",estado_atual[(posicao + 1)])

          
    #Move para cima, não deixa mover para areas bloqueadas e atualixa o mapa
          
    def _cima(self, posicao, estado_atual):
        cima = []
        for i in range(len(mapa)):
            if 0 <= i < C:
                cima.append(i)
        if posicao not in cima and 0 < estado_atual[posicao-C]:
            sucesso = list(estado_atual)
            sucesso[posicao] = -2
            sucesso[posicao - C] = 0
            return (tuple(sucesso), "👆",estado_atual[(posicao - C)])

          
    #Move para baixo, não deixa mover para areas bloqueadas e atualixa o mapa
          
    def _baixo(self, posicao, estado_atual):
        baixo = []
        for i in range(len(mapa)):
            if len(mapa) % 2 == 0:
                if i >= (L * C) - L:
                    baixo.append(i)
            else:
                if i >= (L * C) - C:
                    baixo.append(i)
        if posicao not in baixo and 0 < estado_atual[posicao+L]:
            sucessor = list(estado_atual)
            sucessor[posicao] = -2
            sucessor[posicao + L] = 0
            return (tuple(sucessor), "👇",estado_atual[(posicao + L)])

    #Faz os calculos para obter a Distancia de Manhattan
    def distanciaManhattan(self,i, j):
        return abs(i-(L - 1))+abs(j-(C - 1))

    #Executa a função para realizar Manhattan
    def manhattan(self, estado):
        mapaMatriz = np.reshape(estado, (L, C))
        x = 0
        y = 0
        for i in range(len(mapaMatriz)):
            for j in range(len(mapaMatriz[i])):
                if mapaMatriz[i][j] == 0:
                    x = i
                    y = j
                    return self.distanciaManhattan(x,y)

    
#=============================Basicamente o começo==========================

if __name__ == "__main__":

    #inicia a classe
    jogo = Jogo()

    #delimita os numeros que o tabuleito vai ter (dicionario)
    terreno = {'Terra':1,'Areia': 3,'Barro': 6,'Muro':-1}

    #tamanho do tabuleiro
    L = int(input("Digite o valor para matriz quadrada: "))
  
    C = L

    #tamanho
    tamArray = L * C

    #cria o mapa de acordo com o tamanho e os numeros
    mapa = criaMapa(tamArray,terreno)

    #trnsforma o vetor do mapa em matriz
    mapaMatriz = np.reshape(mapa, (L, C))
    
    valoresMapa = tuple(valormapa(tamArray,terreno,mapa))
  
    mapaMatrizValor = np.reshape(valoresMapa, (L, C))

    #printa o mapa inicial
    print(mapaMatriz)

    #chama manhattan
    Manhattan = a_estrela(valoresMapa, jogo.testarObj, jogo.gerar_sucessores, jogo.manhattan,jogo.custo,L, C)

    if(Manhattan is None):
        print("Caminho não encontrado ou obstruido")
    else:
        print("Custo do caminho encontrado: " + str(Manhattan[0]))
        print("Direções a seguir: " + str(Manhattan[1]))