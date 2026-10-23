class no:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)
    
    def _buscar(self):
    
raiz = no(50)
raiz.esq = no(30)
raiz.dir = no(70)
