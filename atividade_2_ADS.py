# 1) Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.
nome = input('Qual seu nome? ')
idade_dias = float(input('Digite quantos dias de vida você tem: '))
ano = int(idade_dias / 365)
resto = float(idade_dias % 365)
mes = int(resto / 30)
dia = int(idade_dias % 365) % 30
print(nome,'Você tem ',ano, 'anos', mes, 'meses e ', dia, 'dias')



# 2) Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo. Supor que os valores
# lidos são inteiros e positivos. Caso os valores formem um triângulo, calcular e escrever a área deste triângulo.
# Senão formam triângulo escrever os valores lidos.

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

if (a + b > c and a + c > b and b + c > a):
    print('Formam um trialgulo')
    if (a == b and a == c):
        print('Equilátero\n')
    elif (a == b or a == c or b == c):
        print('Isóceles\n')
    else: print('escaleno\n')

else: print('Não formam um triangulo\n ')

altura = int(input('Qual dos tres valores representa a altura do triangulo: '))
base = int(input('Qual dos tres valores representa a base do triangulo: '))
area =float(altura * base / 2)
print('A área do triangulo é: ', area)


#Questão 3) Faça um programa que leia 3 números inteiros e mostre o menor deles.

nome = input('Olá, digite seu nome: ')
n1 = int(input('Informe o prmeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

resultado = n1
if n2 < n1 and n2 < n3:
    resultado = n2
if n3 < n1 and n3 < n2:
    resultado = n3

print(nome, "O menor número entre os três informados foi", resultado)


#4) Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.

for n1 in range(1, 101):
    div = 0

    for n2 in range(1,n1+1):
        if n1%n2==0:
            div+=1
    if div<=2:
        print('Verdadeiro', n1, 'é um numero primo')
    else:
        print('Falso', n1, 'Não é um numero primo')


#5) Escreva uma função que: a) Receba uma frase como parâmetro. b) Retorne uma nova frase com cada palavra com as letras invertidas.

print('######## FRASE INVERTIDA ########')
frase = input('Digite  uma frase: \n')
print('Frase normal: \n', frase)
print('Frase invertida \n', frase [::-1])