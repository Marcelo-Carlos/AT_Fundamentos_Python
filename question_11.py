import pandas as pd

df = pd.read_csv('./Video_Games_Sales_as_at_22_Dec_2016.csv')
df = df[((df["Genre"] == "Action") | (df["Genre"] == "Shooter") | (df["Genre"] == "Platform"))]

print('==================== Jogos publicados (Marcas e quantidades) ====================================================')
publicados = df.groupby('Developer')['Publisher'].count().sort_values(ascending=False)[0:3]
print(publicados)

print('==================== Jogos vendidos (Marcas e receita) ==========================================================')
vendidos = df.groupby('Developer')['Global_Sales'].sum().sort_values(ascending=False)[0:3]
print(vendidos)

print('=================================================================================================================')

print('==================== Jogos vendidos no Japão (10 ultimos anos) (Marca e receita) ================================')

print('============================ AÇÃO ===============================================================================')
action = df[(df["Genre"] == "Action") & (df["Year_of_Release"] >= 2011)]
pub_japao_action = action.groupby('Developer')['JP_Sales'].sum().sort_values(ascending=False)[0:1]
print(pub_japao_action)

print('============================ Tiro ===============================================================================')
shooter = df[(df["Genre"] == "Shooter") & (df["Year_of_Release"] >= 2011)]
pub_japao_shooter = shooter.groupby('Developer')['JP_Sales'].sum().sort_values(ascending=False)[0:1]
print(pub_japao_shooter)

print('============================ Plataforma =========================================================================')
platform = df[(df["Genre"] == "Platform") & (df["Year_of_Release"] >= 2011)]
pub_japao_platform = platform.groupby('Developer')['JP_Sales'].sum().sort_values(ascending=False)[0:1]
print(pub_japao_platform)
print('==================================================================================================================')

