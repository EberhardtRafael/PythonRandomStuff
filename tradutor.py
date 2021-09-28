from googletrans import Translator #esse é um serviço online
#from translate import Translator #não consegue traduzir quase nada.

try:
	with open('arquivo_leitura') as arq:
		#translator = Translator(to_lang='ko')
		translator = Translator()
		
		while True:
			linha = arq.read() #Teu cu, isto não lê somente a linha, arigó.
			if linha != '':
				traducao = translator.translate(linha)
				print(traducao.text)				
			else:
				break
		
	

except FileNotFoundError as erro:
	print("Arquivo nao existente!")
	raise erro
except IOError as erro:
	print("Erro de leitura!")
	raise error
