#Este programa ilustra a utilização das bibliotecas Random e Sys no Pyhont. Esta permine que parâmetros dados no momento da compilação sejam #passados como dado para o programa.
# 

import random
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]



iterando = 0

print("Tente advinhar o numero entre os limites {} e {}: ".format(arg1, arg2))

while True:
	
	numero_gerado = random.randint(int(arg1), int(arg2))
	
	try: #Aqui, resolvo o problema da possibilidade de o usuário entrar com algo que não seja um int
		x = int(input())
	
		if not int(arg1) <= x <= int(arg2):
			print("Numero fora dos limites! Digite novamente: ")
			continue
		elif x == numero_gerado:
			if iterando == 0:
				print("Caralho, muito genio.")
			print("Parabens, acertou")
			break	
		else:
			print("Tente novamente: ")	
		iterando += 1
	except ValueError: #Caso entrada != int
		print("Escreve um numero, caralho!")
		continue
	

