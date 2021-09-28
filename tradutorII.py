from googletrans import Translator

tradutor = Translator()

try:
	with open('arquivo_traduzido', mode = 'w') as arq:
		string_a_traduzir = input("Escreva uma frase a ser traduzida: ")
		string_traduzida = tradutor.translate(string_a_traduzir)
		texto_traduzido = string_traduzida.text
		print(texto_traduzido)
		arq.write(texto_traduzido)
		
except IOError as erro:
	print("Problemas ao escrever no arquivo!")
