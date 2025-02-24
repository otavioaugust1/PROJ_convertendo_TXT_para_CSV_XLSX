# Interface utilizando o PySimpleGUI

import PySimpleGUI as sg


def criar_interface():
    layout = [
        [sg.Text('Selecione o arquivo TXT com os dados:')],
        [
            sg.Input(key='txt_path'),
            sg.FileBrowse('Procurar', file_types=(('Text Files', '*.txt'),)),
        ],
        [sg.Text('Escolha o diretório para salvar os arquivos CSV e XLSX:')],
        [sg.Input(key='save_dir'), sg.FolderBrowse('Procurar')],
        [sg.Button('Converter para CSV e XLSX')],
        [sg.Output(size=(60, 10))],
    ]
    return sg.Window('Conversor TXT para CSV/XLSX', layout)
