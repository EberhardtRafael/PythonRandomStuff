try:

	arq = open('teste') #seria melhor usar 'with open(teste) as arq', pois aí não precisa fechar o arquivo depois.	
	arq2 = open('arquivo_criado', mode = 'w')

	while True:
		linha = arq.readline()
		if 'a' in linha:
			arq2.write(linha)
		elif linha == '':
			break
except FileNotFoundError as erro:
	print("Arquivo nao existe!")
	raise erro
except IOError as erro:
	print("Problema de leitura!")  
	raise erro
		
arq.close() 
arq2.close()



	
	
