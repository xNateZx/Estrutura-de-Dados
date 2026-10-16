class TabelaHash:
    def __init__(self):
        self.tamanho = 5
        self.tabela = []
        
    def adicionar(self):
            self.tabela.append([])
            
    def buscar_posicao(self, ra):
        posicao = ra % self.tamanho
        return posicao
    
    def inserir(self, ra, nome):
        posicao = self.buscar_posicao(ra)
        self.tabela[posicao].append([ra, nome])
        
    def buscar(self, ra):
        posicao = self.buscar_posicao(ra)
        for aluno in self.tabela[posicao]:
            if aluno [0] == ra:
                return aluno[1]
        return None
          
tabela = TabelaHash()
for i in range(tabela.tamanho):
    tabela.adicionar()

tabela.inserir(207, "Marina")
tabela.inserir(412, "Julia")

print(tabela.tabela)

busca = tabela.buscar(412)
print(busca)