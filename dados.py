import json
import os

# Define o caminho da pasta do projeto como a mesma onde está o arquivo .py
PASTA_PROJETO = os.path.dirname(__file__)

# Caminho completo do arquivo de dados JSON
ARQUIVO_DADOS = os.path.join(PASTA_PROJETO, "transacoes.json")

# Cria a pasta do projeto, se não existir (boa prática de segurança)
os.makedirs(PASTA_PROJETO, exist_ok=True)

# Cria o arquivo transacoes.json se ainda não existir (inicializa com lista vazia)
def inicializar_arquivo():
    if not os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'w') as arquivo:
            json.dump([], arquivo)

# Carrega todas as transações do arquivo JSON
def carregar_transacoes():
    with open(ARQUIVO_DADOS, 'r') as arquivo:
        return json.load(arquivo)

# Salva a lista de transações no JSON, com indentação para facilitar leitura
def salvar_transacoes(transacoes):
    with open(ARQUIVO_DADOS, 'w') as arquivo:
        json.dump(transacoes, arquivo, indent=4)
