import re

import pandas as pd


def processar_arquivo(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    sistemas = re.split(r'\n{2,}', conteudo.strip())
    dados_sistemas = []

    for sistema in sistemas:
        linhas = sistema.strip().split('\n')
        info = {
            'SIGLA': linhas[0].strip(),
            'SISTEMA': linhas[1].strip(),
            'DESCRIÇÃO': linhas[2].strip(),
        }

        for linha in linhas[3:]:
            chave_valor = linha.split(':', 1)
            if len(chave_valor) == 2:
                chave = chave_valor[0].strip()
                valor = chave_valor[1].strip()

                if chave == 'Classificação':
                    info['CLASSIFICAÇÃO'] = valor
                elif chave == 'Tipo do Produto':
                    info['TIPO DE PRODUTO'] = valor
                elif chave == 'Secretaria':
                    info['SECRETARIA'] = valor
                elif chave == 'Unidade Responsável':
                    info['UNIDADE RESPONSÁVEL'] = valor
                elif chave == 'Linguagem de Programação':
                    info['LINGUAGEM DE PROGRAMAÇÃO'] = valor
                elif chave == 'Banco de Dados':
                    info['BANCO DE DADOS'] = valor

        dados_sistemas.append(info)

    colunas = [
        'SIGLA', 'SISTEMA', 'DESCRIÇÃO', 'CLASSIFICAÇÃO', 'TIPO DE PRODUTO',
        'SECRETARIA', 'UNIDADE RESPONSÁVEL', 'LINGUAGEM DE PROGRAMAÇÃO', 'BANCO DE DADOS'
    ]
    return pd.DataFrame(dados_sistemas, columns=colunas)

def salvar_csv(df, csv_path):
    df.to_csv(csv_path, index=False, encoding='utf-8')

def salvar_xlsx(df, xlsx_path):
    with pd.ExcelWriter(xlsx_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sistemas')