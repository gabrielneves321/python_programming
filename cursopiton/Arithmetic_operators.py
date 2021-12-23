"""
print(2 + 3)
print(2 - 1)
print(3 * 3)
print(4 / 3)
print(4 // 3) #o resultado sempre sera um numero int
print(2 ** 10) #Potencia
print(10 % 3) #modulo

a = 12
b = a

print(a + b)


#operadores relacionais
print(3>4)
print(4>=3)
print(1<2)
print(3<=1)
print(3!=4) # != QUER DIZER  "DIFERENTE"
print(3==4)
print(2=='2')# não funfa no pitão
print(34)


#operadores lógicos

True or False
print(7 != 3 and 2>3)

#tabela verdade do AND- e: basta um falso para ser "falso"
True and True
True and False
False and True
False and False

#tabela verdade do OR- ou: basta um verdadeiro para ser "verdadeiro"
True or False
True or True
False or True
False or False

#tabela verdade do XOR: tem que ser um diferente do outro para ser verdadeiro
True != True
True != False
False != True
False != False

#operador de negação (unário): número maior que 0 é igual a true e de 0 para baixo é falso
not True
not False
not 0
not 1
not not -1 #negação dupla volta ao original
not not True


saldo = 1000
salario = 4000
despesas = 3890

meta = saldo > 0 and salario-despesas>= 0.2 * salario
print(meta)


#operadores terciários

esta_chovendo = True

print('hoje estou com as roupas ' + ('molhadas.'if esta_chovendo else'secas.'))

#operadores de membro

Lista = {1,2,3,'ana','carolina'}

print(2 in Lista)
print('ana' not in Lista)

#operador de identidade
 x = 3
 y = x
 z = 3
 x is y
 y is z
 x is not z


lista_a = [1,2,3]
lista_b = lista_a
lista_c = [1,2,3]

lista_a is lista_b
lista_b is lista_c 
lista_a is not lista_c
"""
#type()

type(1)
__builtins__.type('hello world')













