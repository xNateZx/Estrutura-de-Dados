class TabelaHash:
    def __init__(self):
        self.tamanho = 7
        self.tabela = []
        for i in range(self.tamanho):
            self.tabela.append([])
            
    def funcao_hash(self, ra):
        return ra % self.tamanho
    
    def inserir(self, ra, nome):
        pos = self.funcao_hash(ra)
        self.tabela[pos].append([ra, nome])
        
    def buscar(Self, ra):
        pos = Self.funcao_hash(ra)
        for aluno in Self.tabela[pos]:
            if aluno[0] == ra:
                return aluno[1]
            return None
        
    def exibir(self):
        for i in range(self.tamanho):
            print(f"[{i}]", self.tabela[i])
            
