import random as rand

def valormapa(array_size,dictionary,mapa):
  
    mapa_val = [None] * array_size
  
    for i in range(array_size):
      
        if i == 0:
          
            mapa_val[i] = 0
          
        else:
          
            mapa_val[i] = dictionary.get(mapa[i])
          
    return mapa_val



def criaMapa(array_size,dictionary):
  
    mapa = [None] * array_size
    key_list = list(dictionary.keys())
    for i in range(array_size):
      
        if i == array_size - 1:
          
            mapa[i] = key_list[rand.randrange(0,3)]
            return mapa
          
        else:
          
            if i == 0:
              
                mapa[i] = "J"
              
            else:    
              
                mapa[i]= key_list[rand.randrange(0,4)]

              
def vertice_caminho(no):
  caminho = []
  
  while no.no_pai is not None:
    
    no = no.no_pai
    
    if no.vertice is not None: 
      caminho.append(no.vertice)
      
  caminho.reverse()
  
  return caminho