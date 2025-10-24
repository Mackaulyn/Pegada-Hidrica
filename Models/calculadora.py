class Pegadahidrica:
    def __init__(self, banho, roupas, torneira): 
        self.banho = 0 
        self.roupas = 0
        self.torneira = 0
        self.familiares = 0
        
    def get_banho(self):
        return self.banho
        
    def get_roupas(self):
        return self.roupas    
        
    def get_torneira(self):
        return self.torneira
        
    def set_familiares(self):
        self.familiares = int(input("Digite o número de pessoas na sua família: "))
        
    def set_banho(self):
    def set_roupas(self):
    def set_torneira(self):

pegada = Pegadahidrica(0, 0 , 0)

print("--- Configuração dos Gastos ---")
pegada.set_familiares()
pegada.set_banho() 
pegada.set_roupas()
pegada.set_torneira()


