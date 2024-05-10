from os import system



system('cls')
print(9 % 3)


num1 = 0
num2 = 1
fibo = [0]

for i in range(1, 5):
    num1 = num1 + num2
    fibo.append(num1)
    num2 = num1 + num2
    fibo.append(num2)
  

print(fibo)

#0+1 1
#1+1 2
#1+2 3
#2+3 5




#texto = 'Por ejemplo aqui hay un texto'
#lista = [letra.lower() for letra in texto if letra.lower() != ' ']
#print(lista)

#pares = [numero for numero in range(1, 101) if numero % 2 == 0]
#impares = [numero for numero in range(1, 101) if numero % 2 == 1]

#print(*pares)
#print(*impares)
