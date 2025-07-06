import matplotlib.pyplot as plt
from dados import carregar_transacoes
from collections import defaultdict
from datetime import datetime

def grafico_despesas_por_categoria():
    transacoes = carregar_transacoes()
    categorias = defaultdict(float)
    
    for t in transacoes:
        if t['tipo'] == 'despesa':
            categorias[t['categoria']] += t['valor']
        
    if not categorias:
            print("Nenhuma despesa registrada.")
            return
    plt.figure(figsize=(8, 6))
    plt.pie(categorias.values(), labels=categorias.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Despesas por Categoria')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()
    plt.show()
    
def grafico_receitas_por_categoria():
    transacoes = carregar_transacoes()
    categorias = defaultdict(float)
    
    for t in transacoes:
        if t['tipo'] == 'receita':
            categorias[t['categoria']] += t['valor']
        
    if not categorias:
            print("Nenhuma receita registrada.")
            return
    plt.figure(figsize=(8, 6))
    plt.pie(categorias.values(), labels=categorias.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Receitas por Categoria')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()
    plt.show()