import requests #Permite fazer requests semelhantes a um data browser, mas sem o data browser
import hashlib #Permite usar a função hash
import sys
import getpass #Permite que o password entrado pelo usuário fique escondido.
#Passei o password 'password123' por uma função hash (SHA1 Hash), gerando 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'
#Agora, se eu usar a versão modificada inteira, ainda assim é possível dar um jeito de descobrir meu password na força bruta.
#Por isso, passo somente os primeiros 5 caracteres do hash criado. O nome disso é 'K anonimity'.
#Se eu rodasse o programa com o password 'password123' ou mesmo 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97', receberia '<Response [400]>',
#o que significa que algo não está bem.
#<Response [200]> é tudo bem.




def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	response = requests.get(url)
	if response.status_code != 200:
		raise RuntimeError("Deu merda tipo: {}. Dá uma checada no api e tenta de novo.".format(response.status_code))
	return response

def le_resposta(resposta):
	print(resposta.text)

def get_contagem_vazamento_password(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:	
		if h == hash_to_check:
			return count
	return 0
	
def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	sha1password_primeiros_5_caracteres, sha1password_tail = sha1password[:5], sha1password[5:]
	resposta = request_api_data(sha1password_primeiros_5_caracteres)
	return get_contagem_vazamento_password(resposta, sha1password_tail)

'''
#Usando esta versão da função, o password entrado pelo usuário fica à mostra.
def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print("O password {} foi achado {} vezes. Talvez valha a pena mudar de password.".format(password, count))
		else:
			print("{} não foi achado. Parece bom o suficiente.". format(password))


main(sys.argv[1:])
'''

def main(password):
	count = pwned_api_check(password)
	if count:
		print("Password {} has been found {} times. Maybe you should change it. Or have your nudes leaked.".format("*"*len(password), count))
	else:
		print("{} was not found. Looks good enough.". format("*"*len(password)))
			
password = getpass.getpass("Entre com password: ")

if __name__ == '__main__': #Não roda se o código for importado como biblioteca, somente se o main rodar.
	main(password)

