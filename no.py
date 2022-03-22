class No:
  def __init__(self, estado, no_pai=None, vertice=None, custo=0.0, heuristica=0.0,total=0.0):
    self.vertice = vertice
    self.no_pai = no_pai
    self.estado = estado
    self.custo = custo
    self.heuristica = heuristica
    self.total = self.custo + self.heuristica