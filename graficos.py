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
    
def grafico_receita_despesa_por_mes():
    transacoes = carregar_transacoes()
    resumo = defaultdict(lambda: {"receita": 0, "despesa": 0})
    
    for t in transacoes:
        mes = datetime.strptime(t['data'], "%Y-%m-%d").strftime("%Y-%m")
        resumo[mes][t['tipo']]+=t['valor']
        
    if not resumo:
        print("Nenhuma transação encontrada.")
        return
    
    meses = sorted(resumo.keys())
    receitas = [resumo[m]['receita'] for m in meses]
    despesas = [resumo[m]['despesa'] for m in meses]
    
    x = range(len(meses))
    
    plt.figure(figsize=(10, 6))
    plt.bar(x, receitas, width=0.4, label="Receitas", align='center')
    plt.bar(x, despesas, width=0.4, label="Despesas", align='edge')
    plt.xticks(x, meses, rotation=45)
    plt.ylabel("Valor (R$)")
    plt.title("Receitas e Despesas por Mês")
    plt.legend()
    plt.tight_layout()
    plt.show()
