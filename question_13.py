import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

url = "http://brasil.pyladies.com/about"
# Usando requests
html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")
print('========================================================')
#Conte todas as palavras no corpo da página
info = soup.find_all('p')
palavras = 0
for p in info:
  palavras += len(p.text.strip().split(" "))
print(f'São: {palavras} palavras')
print('========================================================')
# e indique quais palavras apareceram apenas uma vez.
texto = ""
for paragrafo in [t.text for t in info]:
  paragrafo = paragrafo.strip()
  texto += paragrafo.lower().replace(",", "").replace(".", "") + " "

qtd_palavras = Counter(texto.split(" "))
for key, value in qtd_palavras.items():
  if value == 1:
    print(key, value)
print('========================================================')   
#Conte quantas vezes apareceu a palavra ladies no conteúdo da página
texto = ""
for p in soup.html.body.find_all('p'):
   texto += p.get_text()
   
palavra = "ladies"
resultado = re.findall(palavra, texto)
print(f'A palavra ladies apareceu: {len(resultado)} vezes.')
print('========================================================') 

