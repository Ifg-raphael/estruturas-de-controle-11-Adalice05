#Exercício 2

#Entrada de dados
a= int(input("Insira o primeiro valor: "))
b= int(input("Insira o segundo valor: "))
c= int(input("Insira o terceiro valor: "))

'''O primeiro if Verifica se é um triângulo,ou seja, se o comprimento de cada lado de um triângulo 
é menor do que a soma dos comprimentos dos outros dois lados,se sim parte para classificar o triângulo'''

if  a < b+c and b < a+c and c < a+b: 
    if a==b==c:  #Verifica se o triangulo é equilátero(todos lados iguais)
        print("equilátero")
    elif a==b!=c or a==c!=b or c==b!=a: #Verifica se o triangulo é isósceles(dois lados iguais)
        print("isóceles")
    else:
        print("escaleno") #Se não for equilátero,nem isósceles,logo é classificado como escaleno(todos lados diferentes)
else:
    print("Não forma triângulo") #Exibe a mensagem caso a condição para se formar um triangulo não seja atendida


    