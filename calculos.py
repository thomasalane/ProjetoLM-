import pandas as pd

dataframe = pd.read_csv('faturamento.csv', low_memory=False).dropna()


vendas_por_categoria = dataframe.groupby('Familia Produto')['VlrBruto'].sum()

total_vendas = vendas_por_categoria.sum()

total_categorias = len(vendas_por_categoria)

top6 = vendas_por_categoria.sort_values(ascending=False).head(6)

percentual_top6 = (top6.sum() / total_vendas) * 100

#grafico_distribuicao_vendas_top_categorias

print(f"As Top 6 categorias representam {percentual_top6:.2f}% do valor total de vendas, dentre as {total_categorias} categorias.")
print()

#//////////////////////////////////////////////////////////////////

vendas_por_produto = dataframe.groupby('Produto')['VlrBruto'].sum()

top10_produtos = vendas_por_produto.sort_values(ascending=False).head(10)

percentual_top10_produtos = (top10_produtos.sum() / total_vendas) * 100

total_produtos = vendas_por_produto.shape[0]

#grafico_top_produtos

print(f"Os Top 10 produtos mais vendidos representam {percentual_top10_produtos:.2f}% da receita total, dentre os {total_produtos} produtos.")
print()

#//////////////////////////////////////////////////////////////////

vendas_por_marca = dataframe.groupby('CodMarca')['VlrBruto'].sum()

top10_marcas = vendas_por_marca.sort_values(ascending=False).head(10)

percentual_top10_marcas = (top10_marcas.sum() / total_vendas) * 100

total_marcas = vendas_por_marca.shape[0]

#grafico_top_marcas

print(f"As Top 10 marcas com maior volume de vendas representam {percentual_top10_marcas:.2f}% da receita total, dentre as {total_marcas} marcas.")
print()

#//////////////////////////////////////////////////////////////////

top_10_marcas = [203, 225, 319, 125, 46, 112, 30, 74, 111, 33]

top_10_produtos = ['HHOTTR', 'HIJZFR', 'HIJZFB', 'HIURRO', 'HHORZJ', 'HIFTBH', 'HHFJZU', 'HITOOT', 'HITROR', 'HHFZUR']

produtos_filtrados = dataframe[dataframe['Produto'].isin(top_10_produtos)]

produtos_top10_marcas = produtos_filtrados[produtos_filtrados['CodMarca'].isin(top_10_marcas)]

resultado = produtos_top10_marcas[['Produto', 'CodMarca']].drop_duplicates()

print("Produtos que pertencem as Top 10 Marcas:")
print()
print(resultado)
print()

#grafico_top_marcas, grafico_top_produtos

#//////////////////////////////////////////////////////////////////

dataframe['Data Faturamento'] = pd.to_datetime(dataframe['Data Faturamento'], format='%d/%m/%Y')

dataframe['Ano'] = dataframe['Data Faturamento'].dt.year

vendas_ano = dataframe.groupby('Ano')['VlrBruto'].sum()

valor_2023 = vendas_ano.get(2023, 0)
valor_2024 = vendas_ano.get(2024, 0)

if valor_2023 == 0:
    print("Não há vendas registradas para 2023.")
else:
    if valor_2024 == 0:
        print("Não há vendas registradas para 2024.")
    else:
        crescimento = ((valor_2024 - valor_2023) / valor_2023) * 100
        print(f"De 2023 para 2024, o crescimento foi de {crescimento:.2f}%")

#grafico_vendas_mensais

#//////////////////////////////////////////////////////////////////