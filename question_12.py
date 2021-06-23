import requests
from bs4 import BeautifulSoup
import re

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
# Usando requests
html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")

#Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
for i in soup.html.body.find_all('div', {"class": "tabela"}):
    	print(i.text)

#Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações
# correspondentes na tabela. O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não 
# devem aparecer. Não esqueça de checar se a sigla pertence à região.

lista = []
for t in soup.html.body.find_all('div', {"class": "linha"}):
	lista.append(t.text)

print('===================================================================')
print('DF - Distrito Federal')
print('GO - Goiás')
print('MT - Mato Grosso')
print('MS - Mato Grosso do Sul')
print('===================================================================')
opcao = ''
opcao = input('Digite a sigla de um estado da região centro-oeste: ').lower()
if opcao.lower() == "df":
    print(lista[0])
elif opcao.lower() == "go":
    print(lista[1])
elif opcao.lower() == "mt":
    print(lista[2])
elif opcao.lower() == "ms":
    print(lista[3])
else:
    print('ERROR - Essa sigla não pertence a região centro-oeste!')

    	

