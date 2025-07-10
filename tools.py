import os
import csv
from dados import *
from datetime import datetime
from collections import defaultdict
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from visualizacoes.graficos import *


# Adiciona uma nova transação (receita ou despesa) no arquivo
def adicionar_transacao(tipo, valor, categoria, data, descricao):
    nova_transacao = {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "data": data,
        "descricao": descricao
    }

    transacoes = carregar_transacoes()
    transacoes.append(nova_transacao)
    salvar_transacoes(transacoes)
    print(f"\n{tipo.title()} registrada com sucesso!")

# Mostra o saldo atual calculando receitas - despesas
def saldo():
    transacoes = carregar_transacoes()
    saldo = 0
    for i in transacoes:
        if i['tipo'] == 'receita':
            saldo += i['valor']
        elif i['tipo'] == 'despesa':
            saldo -= i['valor']
    print(f"\nSaldo atual: R$ {saldo:.2f}")

# Lista todas as transações registradas
def listar_transacoes():
    transacoes = carregar_transacoes()

    if not transacoes:
        print("\nAinda nenhuma transação foi feita")
        return

    for i, t in enumerate(transacoes, start=1):
        print(f"{i}. {t['data']} | {t['tipo'].upper():7} | R$ {t['valor']:.2f} | {t['categoria']} - {t['descricao']}")

# Gera um resumo por categoria (agrupando receitas e despesas)
def resumo_por_categoria():
    transacoes = carregar_transacoes()
    resumo = {}

    for t in transacoes:
        categoria = t['categoria']
        valor = t['valor']
        if categoria not in resumo:
            resumo[categoria] = 0
        if t['tipo'] == 'despesa':
            resumo[categoria] -= valor
        else:
            resumo[categoria] += valor

    print("\nResumo por categoria:")
    for cat, total in resumo.items():
        print(f" - {cat}: R$ {total:.2f}")

# Gera um resumo por mês, mostrando receitas, despesas e saldo mensal
def resumo_por_mes():
    transacoes = carregar_transacoes()
    resumo = defaultdict(lambda: {"receita": 0, "despesa": 0})

    for t in transacoes:
        mes = datetime.strptime(t["data"], "%Y-%m-%d").strftime("%Y-%m")
        resumo[mes][t["tipo"]] += t["valor"]

    print("\nResumo por mês:")
    for mes, valores in resumo.items():
        saldo = valores["receita"] - valores["despesa"]
        print(f" - {mes}: Receita: R$ {valores['receita']:.2f}, Despesa: R$ {valores['despesa']:.2f}, Saldo: R$ {saldo:.2f}")

# Exporta as transações para um arquivo CSV no local indicado
def exportar_transacoes_csv(caminho_csv):
    transacoes = carregar_transacoes()

    if not transacoes:
        print("Nenhuma transação para exportar.")
        return

    with open(caminho_csv, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=transacoes[0].keys())
        escritor.writeheader()
        escritor.writerows(transacoes)
        os.sync()  # Garante que o sistema operacional salve o arquivo fisicamente

    print(f"\nTransações exportadas com sucesso para: {caminho_csv}")
    
# Exporta as transações para um arquivo PDF no local indicado
def exportar_transacoes_pdf(caminho_pdf):
    transacoes = carregar_transacoes()

    if not transacoes:
        print("Nenhuma transação para exportar.")
        return

    # Cria um novo PDF com tamanho A4
    pdf = canvas.Canvas(caminho_pdf, pagesize=A4)

    # Define posição inicial do texto no PDF (eixo Y)
    largura, altura = A4
    y = altura - 50

    # Título
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Relatório de Transações Financeiras")
    y -= 30

    # Cabeçalhos da tabela
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Data")
    pdf.drawString(120, y, "Tipo")
    pdf.drawString(180, y, "Valor")
    pdf.drawString(250, y, "Categoria")
    pdf.drawString(400, y, "Descrição")
    y -= 20

    # Linhas de dados
    pdf.setFont("Helvetica", 11)
    for t in transacoes:
        if y < 50:  # Se estiver muito no fim da página, cria nova página
            pdf.showPage()
            y = altura - 50
            pdf.setFont("Helvetica", 11)

        pdf.drawString(50, y, t['data'])
        pdf.drawString(120, y, t['tipo'].title())
        pdf.drawString(180, y, f"R$ {t['valor']:.2f}")
        pdf.drawString(250, y, t['categoria'])
        pdf.drawString(400, y, t['descricao'][:40])  # Limita descrição
        y -= 20

    # Data e hora de exportação no rodapé
    pdf.setFont("Helvetica-Oblique", 9)
    pdf.drawString(50, 30, f"Exportado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Salva o PDF
    pdf.save()

    print(f"\nTransações exportadas com sucesso para: {caminho_pdf}")

