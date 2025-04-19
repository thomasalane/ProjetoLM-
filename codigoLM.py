import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('faturamento.csv', low_memory=False).dropna()

#//////////////////////////////////////////////////////////////////

vendas_totais = dataframe['VlrBruto']
quantidade = dataframe['Qtd']

plt.figure(figsize=(12, 10))

plt.scatter(vendas_totais, quantidade)

plt.xlabel('Valor Bruto das Vendas (R$)')

plt.ylabel('Quantidade de Produtos Vendidos')

plt.title('Valor Bruto x Quantidade de Produtos')

plt.grid(True)

plt.show()

#//////////////////////////////////////////////////////////////////

top_marcas = dataframe.groupby('CodMarca')['VlrBruto'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 10))

plt.bar(top_marcas.index.astype(str), top_marcas.values, color='skyblue')

plt.xlabel('Código da Marca')

plt.ylabel('Valor Bruto das Vendas (R$)')

plt.title('Top 10 Marcas com Maior Volume de Vendas')

plt.xticks(rotation=45) 

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

plt.show()

#//////////////////////////////////////////////////////////////////

top_produtos = dataframe.groupby('Produto')['Qtd'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 10))

plt.bar(top_produtos.index, top_produtos.values)

plt.xlabel('ID do Produto')

plt.ylabel('Quantidade de Produtos Vendidos')

plt.title('Top 10 Produtos Mais Vendidos')

plt.xticks(rotation=45, ha='right') 

plt.tight_layout() 

plt.show()

#//////////////////////////////////////////////////////////////////

categoria_vendas = dataframe['Familia Produto'].value_counts().head(6)

plt.figure(figsize=(12, 10))

plt.pie(categoria_vendas, labels=categoria_vendas.index, autopct='%1.1f%%', startangle=140)

plt.title('Distribuição de Vendas das Top 6 Categorias')

plt.show()

#//////////////////////////////////////////////////////////////////

vendas_regiao = dataframe.groupby('Regiao')['VlrBruto'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 10))

plt.barh(vendas_regiao.index, vendas_regiao.values)

plt.xlabel('Valor Bruto das Vendas')

plt.ylabel('Região')

plt.title('Vendas por Região')

plt.show()

#//////////////////////////////////////////////////////////////////

dataframe['Data Faturamento'] = pd.to_datetime(dataframe['Data Faturamento'], format='%d/%m/%Y')

dataframe['Ano'] = dataframe['Data Faturamento'].dt.year
dataframe['Mês'] = dataframe['Data Faturamento'].dt.month

vendas_mensais = dataframe.groupby(['Ano', 'Mês'])['VlrBruto'].sum().reset_index()

plt.figure(figsize=(12, 10))

for ano in vendas_mensais['Ano'].unique():
    vendas_ano = vendas_mensais[vendas_mensais['Ano'] == ano]
    plt.plot(vendas_ano['Mês'], vendas_ano['VlrBruto'], label=f'Ano {ano}')

plt.xlabel('Mês')

plt.ylabel('Valor Bruto das Vendas')

plt.title('Vendas Mensais por Ano')

plt.xticks(range(1, 13))  

plt.legend()

plt.grid(True)

plt.show()

#//////////////////////////////////////////////////////////////////

ticket_medio_categoria = dataframe.groupby('Familia Produto')[['VlrBruto', 'Qtd']].sum()\
    .assign(TicketMedio=lambda x: x['VlrBruto'] / x['Qtd'])['TicketMedio'].sort_values(ascending=False)

ticket_medio_categoria_top = ticket_medio_categoria.head(10)

plt.figure(figsize=(12, 10))

plt.bar(ticket_medio_categoria_top.index, ticket_medio_categoria_top.values)

plt.xlabel('Categoria de Produto')

plt.ylabel('Ticket Médio (R$)')

plt.title('Ticket Médio das Top 10 Categorias')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()

#//////////////////////////////////////////////////////////////////

dataframe['Data Faturamento'] = pd.to_datetime(dataframe['Data Faturamento'], format='%d/%m/%Y')

dataframe['Ano'] = dataframe['Data Faturamento'].dt.year
dataframe['Mês'] = dataframe['Data Faturamento'].dt.month

vendas_regiao_tempo = dataframe.groupby(['Regiao', 'Ano', 'Mês'])['VlrBruto'].sum().reset_index()

plt.figure(figsize=(12, 10))

for regiao in vendas_regiao_tempo['Regiao'].unique():
    dados_regiao = vendas_regiao_tempo[vendas_regiao_tempo['Regiao'] == regiao]
    datas = pd.to_datetime(dados_regiao.rename(columns={'Ano': 'year', 'Mês': 'month'}).assign(day=1)[['year', 'month', 'day']])
    plt.plot(datas, dados_regiao['VlrBruto'], label=regiao)

plt.xlabel('Período (Ano-Mês)')

plt.ylabel('Valor Bruto das Vendas (R$)')

plt.title('Evolução das Vendas por Região')

plt.legend(title='Região')

plt.grid(True)

plt.tight_layout()

plt.show()

#//////////////////////////////////////////////////////////////////


