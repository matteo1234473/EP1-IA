from no import No
import heapq
import numpy as np
from construtor import criaMapa, valormapa, vertice_caminho

#Cria a classe prioridade para colocar as jogadas em ordem decrescente em uma fila
class Prioridade:
  def __init__(self):
    self.queue = []
  def push(self, item):
    heapq.heappush(self.queue, item)
  def pop(self):
    if(self.lista_vazia()):
        return None
    else:
        return heapq.heappop(self.queue)
  def lista_vazia(self):
    return len(self.queue) == 0


#Printa os estados dos mapas e o respectivo custo da jogada feita anteriormente
def printa_mapa(estado, L, C, custo):
  print("\n")
  print("Custo da Jogada: ", custo)
  print(np.reshape(estado, (L, C)))


#Funcao A* que através da heuristica e dos custos escolhe a """MELHOR""" jogada (menos custosa)
def a_estrela(estado_inicial, testar_objetivo, gerar_sucessores, heuristica, custo,L , C):
  queue = Prioridade()     #cria a fila                                                                
  queue.push(No(estado_inicial, None, None, 0.0, heuristica(estado_inicial),0.0))  #coloca um novo nó na fila

  #custos das heuristicas
  custo_absoluto = [0,[]]
  custo_total = 0

  #Looping de jogadas enquanto a lista não acabar OU o der invalidações nos caminhos
  while not queue.lista_vazia():
    no_atual = queue.pop()            #Apaga todo antigo estado
    estado_atual = no_atual.estado    #A cada jogada q passa, o estado atual recebe o primeiro nó que está na lista

    #Printa o mapa
    printa_mapa(estado_atual, L, C, custo_total)

    #Confere se o objetivo foi concluido
    if(testar_objetivo(estado_atual,len(estado_atual))):
      return custo_absoluto

    #Lógica para gerar estados sucessores e confereir a melhor possibilidade de acordo com o custo + heuristica
    estados_vertices_sucessores = gerar_sucessores(estado_atual)
    mov_peca = None
    heuristica_values=[]

    for estados_vertices_sucessor in estados_vertices_sucessores:
      no = No(estados_vertices_sucessor[0], no_atual, estados_vertices_sucessor[1],estados_vertices_sucessor[2], heuristica(estados_vertices_sucessor[0]))
      heuristica_values.append(no.total)
      if mov_peca == None: 
        mov_peca = no
      else:
        if no.heuristica == 0:
          mov_peca = no
        else:
          if no.total < mov_peca.total:
            mov_peca = no

    #Try catch ultilizado para caso o Joselindo fique preso e não quebre o programa
    try:
      custo_total += mov_peca.custo
      custo_absoluto[0] = custo_total
      custo_absoluto[1].append(mov_peca.vertice)
      queue.push(mov_peca)
    except:
      return None
    
  return None

