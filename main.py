import PySimpleGUI as sg  # Adicione esta linha

from src.controller.main_controller import executar_conversao
from src.views.interface import criar_interface


def main():
    window = criar_interface()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Converter para CSV e XLSX':
            resultado = executar_conversao(
                values['txt_path'], values['save_dir']
            )
            print(resultado)

    window.close()


if __name__ == '__main__':
    main()
