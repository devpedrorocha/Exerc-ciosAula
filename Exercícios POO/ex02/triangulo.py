class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def controle(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3 and self.lado2 == self.lado3:
            print('Triângulo Equilátero')
            return
        
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado3 == self.lado2:
            print('Triângulo Isósceles')
            return
        
        else:
            print('Triângulo Escaleno')
        ## Triângulo Escalenoself.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 == self.lado3:
            
        










