class Pessoa:
    def __init__(self, nome, idade, falando = False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        
    def falar(self):
        print('Entrou no falar')
        if self.falando:
            print(f'{self.nome} já esta falando!')
            return 
        print(f'{self.nome} agora está falando!.')
    
    def parar_falar(self):
        if not self.falando:
            print(f'Não estou falando!')
            return
        print('Parei de falar.')
        
        
    def imprime_dados(self):
        print(f'{self.nome} tem {self.idade} anos. \n{self.nome} está falando? {self.falando}')