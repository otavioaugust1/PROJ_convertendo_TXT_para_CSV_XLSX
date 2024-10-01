
# Importação das Bibliotecas 
import pandas as pd
import re
import xlsxwriter
import PySimpleGUI as sg
import os

# Função para processar o conteúdo do arquivo e gerar um DataFrame
def processar_arquivo(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Dividir o conteúdo em blocos separados por uma linha em branco
    sistemas = re.split(r'\n{2,}', conteudo.strip())

    # Lista para armazenar os dados dos sistemas
    dados_sistemas = []

    for sistema in sistemas:
        # Separar cada linha do bloco
        linhas = sistema.strip().split('\n')

        # Criar um dicionário para armazenar as informações de cada sistema
        info = {}

        # Preencher o dicionário com as informações
        info['SIGLA'] = linhas[0].strip()  # Primeira linha é a SIGLA
        info['SISTEMA'] = linhas[1].strip()  # Segunda linha é o nome do SISTEMA
        info['DESCRIÇÃO'] = linhas[2].strip()  # Terceira linha é a DESCRIÇÃO

        # Loop para pegar as demais informações que seguem o formato 'Chave: Valor'
        for linha in linhas[3:]:
            chave_valor = linha.split(':', 1)  # Dividir na primeira ocorrência de ':'
            if len(chave_valor) == 2:  # Verificar se a linha está no formato correto
                chave = chave_valor[0].strip()  # Pegar a chave (antes dos dois pontos)
                valor = chave_valor[1].strip()  # Pegar o valor (depois dos dois pontos)

                # Renomear as chaves para corresponder aos nomes das colunas desejadas
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

        # Adicionar o dicionário à lista de sistemas
        dados_sistemas.append(info)

    # Criar um DataFrame com as colunas desejadas
    colunas = ['SIGLA', 'SISTEMA', 'DESCRIÇÃO', 'CLASSIFICAÇÃO', 'TIPO DE PRODUTO',
               'SECRETARIA', 'UNIDADE RESPONSÁVEL', 'LINGUAGEM DE PROGRAMAÇÃO', 'BANCO DE DADOS']
    df = pd.DataFrame(dados_sistemas, columns=colunas)

    return df

# Função para salvar o DataFrame em um arquivo CSV
def salvar_csv(df, csv_path):
    df.to_csv(csv_path, index=False, encoding='utf-8')

# Função para salvar o DataFrame em um arquivo XLSX
def salvar_xlsx(df, xlsx_path):
    writer = pd.ExcelWriter(xlsx_path, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sistemas')
    writer.close()  # Use 'close' em vez de 'save'


# Layout da interface gráfica usando PySimpleGUI
layout = [
    [sg.Text('Selecione o arquivo TXT com os dados:')],
    [sg.Input(key='txt_path'), sg.FileBrowse('Procurar', file_types=(("Text Files", "*.txt"),))],
    [sg.Text('Escolha o diretório para salvar os arquivos CSV e XLSX:')],
    [sg.Input(key='save_dir'), sg.FolderBrowse('Procurar')],
    [sg.Button('Converter para CSV e XLSX')],
    [sg.Output(size=(60, 10))]
]

# Criar a janela
window = sg.Window('Conversor TXT para CSV/XLSX', layout)

# Loop de eventos para a interface
while True:
    event, values = window.read()

    # Fechar a janela
    if event == sg.WINDOW_CLOSED:
        break

    # Se o botão "Converter para CSV e XLSX" for clicado
    if event == 'Converter para CSV e XLSX':
        txt_path = values['txt_path']
        save_dir = values['save_dir']

        if not txt_path or not save_dir:
            print("Por favor, selecione o arquivo TXT e o diretório para salvar os arquivos.")
        else:
            try:
                # Processar o arquivo TXT e gerar o DataFrame
                df_sistemas = processar_arquivo(txt_path)

                # Caminhos para salvar os arquivos CSV e XLSX
                csv_path = os.path.join(save_dir, 'sistemas.csv')
                xlsx_path = os.path.join(save_dir, 'sistemas.xlsx')

                # Salvar os arquivos CSV e XLSX
                salvar_csv(df_sistemas, csv_path)
                salvar_xlsx(df_sistemas, xlsx_path)

                print(f"Arquivos CSV e XLSX criados com sucesso!\nCSV: {csv_path}\nXLSX: {xlsx_path}")

            except Exception as e:
                print(f"Ocorreu um erro: {e}")

# Fechar a janela
window.close()
