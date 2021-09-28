from PIL import Image
import sys

def abre_arquivo_com_imagens(default = "imagens_lista", *args):
	try:
		with open(default, *args) as arquivo_imagens:
			print("As imagens abertas foram:")
			while True:
				linha_arquivo_imagens = arquivo_imagens.readline()				
				if linha_arquivo_imagens != "":
					print(linha_arquivo_imagens.strip("\n"))
					imagem = Image.open(linha_arquivo_imagens.strip("\n"))
					imagem.show()
				else:
					break 
		
	except IOError as erro:
		print("Deu merda na hora de abrir o arquivo com a lista de imagens.")

if len(sys.argv) > 1:
	abre_arquivo_com_imagens(sys.argv[1])	
else:
	abre_arquivo_com_imagens()
