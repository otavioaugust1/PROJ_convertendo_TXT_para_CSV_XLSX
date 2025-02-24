import os

from src.models.processador import processar_arquivo, salvar_csv, salvar_xlsx


def executar_conversao(txt_path, save_dir):
    if not txt_path or not save_dir:
        return 'Por favor, selecione o arquivo TXT e o diretório para salvar os arquivos.'

    try:
        df_sistemas = processar_arquivo(txt_path)
        csv_path = os.path.join(save_dir, 'sistemas.csv')
        xlsx_path = os.path.join(save_dir, 'sistemas.xlsx')

        salvar_csv(df_sistemas, csv_path)
        salvar_xlsx(df_sistemas, xlsx_path)

        return f'Arquivos CSV e XLSX criados com sucesso!\nCSV: {csv_path}\nXLSX: {xlsx_path}'
    except Exception as e:
        return f'Ocorreu um erro: {e}'