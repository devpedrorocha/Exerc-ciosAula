from triangulo import Triangulo


triangulo1 = Triangulo(15, 15, 50)

if triangulo1.lado1 + triangulo1.lado2 > triangulo1.lado3:
    
    triangulo1.controle()
    
else:
    print('Erro, não é um Triângulo!')


