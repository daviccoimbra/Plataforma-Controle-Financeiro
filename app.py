import json
import os
from dados import *
from visualizacoes.graficos import *
from tools import *

def menu():
    inicializar_arquivo()  # Garante que o JSON existe antes de qualquer operação

    while True:
        print("\n===== Menu  =====")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Saldo")
        print("4. Listar Transações")
        print("5. Resumo por Categoria")
        print("6. Resumo por Mês")
        print("7. Exportar Transações para CSV")
        print("8. Exportar Transações para PDF")
        print("9. Gráficos")
        print("10. Limpar transações --- temporário")
        print("11. Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            tipo = 'receita'
        elif option == "2":
            tipo = 'despesa'
        elif option == "3":
            saldo()
            continue
        elif option == "4":
            print('\n')
            listar_transacoes()
            continue
        elif option == "5":
            resumo_por_categoria()
            continue
        elif option == "6":
            resumo_por_mes()
            continue
        elif option == "7":
            exportar_transacoes_csv(f"{PASTA_PROJETO}/relatorio_transacoes.csv")
            continue
        elif option == "8":
            exportar_transacoes_pdf(os.path.join(PASTA_PROJETO, "relatorio_transacoes.pdf"))
            continue
        elif option == "9":
            grafico_option = input("\nEscolha o gráfico:\n1. Despesas por Categoria\n2. Receitas por Categoria\n 3. Voltar\nOpção: ")
            if grafico_option == "1":
                grafico_despesas_por_categoria()
                continue
            elif grafico_option == "2":
                grafico_receitas_por_categoria()
                continue
            elif grafico_option =="3":continue
        elif option == "10":
            # Limpa todas as transações (reset no JSON)
            if os.path.exists(ARQUIVO_DADOS):
                with open(ARQUIVO_DADOS, 'w') as arquivo:
                    json.dump([], arquivo)
                print('\nTransações limpadas')
            continue
        elif option == "11":
            print("\nSaindo do programa.")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")
            continue

        # Entrada dos dados de receita ou despesa
        try:
            valor = float(input("Digite o valor: "))
            categoria = input("Digite a categoria: ")
            data = input("Digite a data (YYYY-MM-DD) [Enter para hoje]: ") or datetime.now().strftime("%Y-%m-%d")
            descricao = input("Digite a descrição: ")

            adicionar_transacao(tipo, valor, categoria, data, descricao)

        except ValueError:
            print("\nErro: valor inválido.")

# Inicia o programa
menu()
