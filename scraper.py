import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
#print(res)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

def ordenado_por_votos(lista):
	return sorted(lista, key = lambda k: k['votes'], reverse = True)

def create_custom_hacker_news(links, votes):
	hn = []
	for i, item in enumerate(links):
		title = links[i].getText()
		href = links[i].get('href', None) #href é o link! Então eu pego o link associado a cada título (Não havendo, retorna None).
		vote = subtext[i].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points}) #Na hora de printar, vai ser em ordem alfabérica. Então, vai aparecer link antes de title.
	return ordenado_por_votos(hn)
	

#create_custom_hacker_news(links, subtext)	
#print(create_custom_hacker_news(links, subtext))

print("\n\nPagina 1:\n\n")
pprint.pprint(create_custom_hacker_news(links, subtext))
print("\n\nPagina 2:\n\n")
pprint.pprint(create_custom_hacker_news(links2, subtext2))
