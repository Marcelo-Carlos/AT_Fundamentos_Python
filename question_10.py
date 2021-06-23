import pandas as pd
from datetime import datetime, date

df = pd.read_csv('./Winter_Olympics_Medals.csv')
df = df[((df["NOC"] == "SWE") | (df["NOC"] == "NOR") | (df["NOC"] == "DEN")) & (df["Year"] >= 2001)]

#Curling 
suecia = df[(df["NOC"] == "SWE") & (df["Sport"] == "Curling") & (df["Medal"] == "Gold")].count()['Medal']         
dinamarca = df[(df["NOC"] == "DEN") & (df["Sport"] == "Curling") & (df["Medal"] == "Gold")].count()['Medal']
noruega = df[(df["NOC"] == "NOR") & (df["Sport"] == "Curling") & (df["Medal"] == "Gold")].count()['Medal']

print('======================== CURLING =====================================================================')
if suecia > dinamarca and suecia > noruega:
    print(f'Suécia foi o país com maior número de medalhas de ouro: {suecia} no total')
elif dinamarca > suecia and dinamarca > noruega:
    print(f'Dinamarca foi o país com maior número de medalhas de ouro: {dinamarca} no total')
elif noruega > dinamarca and noruega > suecia:
    print(f'Noruega foi o país com maior número de medalhas de ouro: {noruega} no total')
elif noruega == dinamarca and noruega > suecia:
    print(f'Noruega e Dinamarca tiveram mesmo numero de medalhas de ouro: {noruega} no total')
elif noruega == suecia and noruega > dinamarca:
    print(f'Noruega e Suécia tiveram mesmo numero de medalhas de ouro: {noruega} para cada.')
elif noruega == suecia and noruega == dinamarca:
    print(f'Noruega, Suécia e Dinamarca tiveram mesmo numero de medalhas de ouro: {noruega} para cada.')


#Skating
suecia_skating = df[(df["NOC"] == "SWE") & (df["Sport"] == "Skating") & (df["Medal"] == "Gold")].count()['Medal']
dinamarca_skating = df[(df["NOC"] == "DEN") & (df["Sport"] == "Skating") & (df["Medal"] == "Gold")].count()['Medal']
noruega_skating = df[(df["NOC"] == "NOR") & (df["Sport"] == "Skating") & (df["Medal"] == "Gold")].count()['Medal']

print('======================== SKATING ==========================================================================')
if suecia_skating > dinamarca_skating and suecia_skating > noruega_skating:
    print(f'Suécia foi o país com maior número de medalhas de ouro: {suecia_skating} no total')
elif dinamarca_skating > suecia_skating and dinamarca_skating > noruega_skating:
    print(f'Dinamarca foi o país com maior número de medalhas de ouro: {dinamarca_skating} no total')
elif noruega_skating > dinamarca_skating and noruega_skating > suecia_skating:
    print(f'Noruega foi o país com maior número de medalhas de ouro: {noruega_skating} no total')
elif noruega_skating == dinamarca_skating and noruega_skating > suecia_skating:
    print(f'Noruega e Dinamarca tiveram mesmo numero de medalhas de ouro: {noruega_skating} no total')
elif noruega_skating == suecia_skating and noruega_skating > dinamarca_skating:
    print(f'Noruega e Suécia tiveram mesmo numero de medalhas de ouro: {noruega_skating} para cada.')
elif noruega_skating == suecia_skating and noruega_skating == dinamarca_skating:
    print(f'Noruega, Suécia e Dinamarca tiveram mesmo numero de medalhas de ouro: {noruega_skating} para cada.')

#Skiing
suecia_skiing = df[(df["NOC"] == "SWE") & (df["Sport"] == "Skiing") & (df["Medal"] == "Gold")].count()['Medal']
dinamarca_skiing = df[(df["NOC"] == "DEN") & (df["Sport"] == "Skiing") & (df["Medal"] == "Gold")].count()['Medal']
noruega_skiing = df[(df["NOC"] == "NOR") & (df["Sport"] == "Skiing") & (df["Medal"] == "Gold")].count()['Medal']

print('======================== SKIING =============================================================================')
if suecia_skiing > dinamarca_skiing and suecia_skiing > noruega_skiing:
    print(f'Suécia foi o país com maior número de medalhas de ouro: {suecia_skiing} no total')
elif dinamarca_skiing > suecia_skiing and dinamarca_skiing > noruega_skiing:
    print(f'Dinamarca foi o país com maior número de medalhas de ouro: {dinamarca_skiing} no total')
elif noruega_skiing> dinamarca_skiing and noruega_skiing > suecia_skiing:
    print(f'Noruega foi o país com maior número de medalhas de ouro: {noruega_skiing} no total')
elif noruega_skiing == dinamarca_skiing and noruega_skiing > suecia_skiing:
    print(f'Noruega e Dinamarca tiveram mesmo numero de medalhas de ouro: {noruega_skiing} no total')
elif noruega_skiing == suecia_skiing and noruega_skiing > dinamarca_skiing:
    print(f'Noruega e Suécia tiveram mesmo numero de medalhas de ouro: {noruega_skiing} para cada.')
elif noruega_skiing == suecia_skiing and noruega_skiing == dinamarca_skiing:
    print(f'Noruega, Suécia e Dinamarca tiveram mesmo numero de medalhas de ouro: {noruega_skiing} para cada.')

#Ice Hockey
suecia_ice = df[(df["NOC"] == "SWE") & (df["Sport"] == "Ice Hockey") & (df["Medal"] == "Gold")].count()['Medal']
dinamarca_ice = df[(df["NOC"] == "DEN") & (df["Sport"] == "Ice Hockey") & (df["Medal"] == "Gold")].count()['Medal']
noruega_ice = df[(df["NOC"] == "NOR") & (df["Sport"] == "Ice Hockey") & (df["Medal"] == "Gold")].count()['Medal']

print('======================== Ice Hockey =========================================================================')
if suecia_ice > dinamarca_ice and suecia_ice > noruega_ice:
    print(f'Suécia foi o país com maior número de medalhas de ouro: {suecia_ice} no total')
elif dinamarca_ice > suecia_ice and dinamarca_ice > noruega_ice:
    print(f'Dinamarca foi o país com maior número de medalhas de ouro: {dinamarca_ice} no total')
elif noruega_ice > dinamarca_ice and noruega_ice > suecia_ice:
    print(f'Noruega foi o país com maior número de medalhas de ouro: {noruega_ice} no total')
elif noruega_ice == dinamarca_ice and noruega_ice > suecia_ice:
    print(f'Noruega e Dinamarca tiveram mesmo numero de medalhas de ouro: {noruega_ice} no total')
elif noruega_ice == suecia_ice and noruega_ice > dinamarca_ice:
    print(f'Noruega e Suécia tiveram mesmo numero de medalhas de ouro: {noruega_ice} para cada.')
elif noruega_ice == suecia_ice and noruega_ice == dinamarca_ice:
    print(f'Noruega, Suécia e Dinamarca tiveram mesmo numero de medalhas de ouro: {noruega_ice} para cada.')
    
print('======================== Total de Medalhas p/ país ==========================================================')

paises = df[((df["Sport"] == "Curling") | (df["Sport"] == "Skating") | (df["Sport"] == "Ice Hockey") | (df["Sport"] == "SKIING"))]
paises = paises.assign(Quantity = 1)

p = paises.groupby(["NOC"])[["Medal"]].count()

print(p)

print('======================== Relatório detalhado ================================================================')
relatorio = paises[['NOC', 'Sport', 'Year', 'City', 'Event gender', 'Medal', 'Quantity']]

print(relatorio)



