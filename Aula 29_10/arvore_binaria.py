class TabelaHash:
    def __init__(self):
        self.tamanho = 5
        self.tabela = []
        for i in range(self.tamanho):
            self.tabela.append([])

    def funcao_hash(self, codigo):
        return codigo % self.tamanho

    def inserir(self, codigo, nome):
        pos = self.funcao_hash(codigo)
        self.tabela[pos].append([codigo, nome])