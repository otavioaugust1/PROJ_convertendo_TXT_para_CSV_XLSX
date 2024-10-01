# PROJ_convertendo_TXT_para_CSV_XLSX
![img](https://github.com/otavioaugust1/PROJ_convertendo_TXT_para_CSV_XLSX/blob/main/BASE/convert.png)

# Conversor de Arquivo TXT para CSV/XLSX

Este projeto é uma ferramenta que converte arquivos de texto (TXT) formatados em tabelas para arquivos CSV e XLSX, utilizando uma interface gráfica simples. A interface permite que o usuário selecione um arquivo TXT, escolha o local para salvar os arquivos de saída e execute a conversão com um clique.

## Funcionalidades

* Conversão de arquivos de texto formatados para **CSV** e **XLSX**.
* Interface gráfica amigável com o uso da biblioteca **PySimpleGUI**.
* Suporte para salvar os arquivos convertidos em qualquer diretório escolhido.

## Tecnologias Utilizadas

* **Python 3**
* **Pandas**: Utilizado para manipulação de dados e criação de DataFrames.
* **XlsxWriter**: Utilizado para exportar os dados para arquivos XLSX.
* **PySimpleGUI**: Utilizado para criar a interface gráfica.
* **Re**: Utilizado para processamento de strings com expressões regulares.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos atendidos:

* Python 3 instalado
* As bibliotecas necessárias instaladas. Você pode instalá-las com os seguintes comandos:

```bash
pip install pandas
pip install xlsxwriter
pip install PySimpleGUI
```

# Como Usar
## Clone o repositório:
```
git clone https://github.com/seuusuario/conversor-txt-csv-xlsx.git
cd conversor-txt-csv-xlsx
```
## Execute o script:
```
python conversor.py
```
## Utilize a interface gráfica:
* Na janela, clique no botão "Procurar" para selecionar o arquivo TXT que deseja converter.
* Escolha a pasta de destino onde os arquivos CSV e XLSX serão salvos.
* Clique no botão "Converter para CSV e XLSX" para realizar a conversão.
* A mensagem de sucesso aparecerá na tela com o caminho dos arquivos gerados.

# Estrutura do Projeto
* `conversor.py`: Script principal que contém a lógica para a interface gráfica, leitura do arquivo TXT e geração dos arquivos CSV e XLSX.
* `README.md`: Este arquivo, contendo as instruções para uso do projeto.

# Formato Esperado do Arquivo TXT
O arquivo TXT deve seguir o seguinte formato:
```
SIGLA DO SISTEMA
Nome do Sistema
Descrição do Sistema
Classificação: Saúde
Tipo do Produto: Sistema
Secretaria: Nome da Secretaria
Unidade Responsável: Nome da Unidade
Linguagem de Programação: Linguagem utilizada
Banco de Dados: Banco de dados utilizado

```
Exemplo:
```
ACADEMIA DA SAÚDE
Sistema de Monitoramento do Programa Academia da Saúde
O Sistema é parte da estratégia para acompanhamento e apoio a implantação e implementação do Programa pelos municípios.
Classificação: Saúde
Tipo do Produto: Sistema
Secretaria: Secretaria de Atenção à Saúde
Unidade Responsável: Departamento de Atenção Básica
Linguagem de Programação: PHP
Banco de Dados: ORACLE 11G

```

# Possíveis Erros
* O arquivo TXT não está no formato correto: Verifique se o arquivo segue o formato esperado.
* Bibliotecas não instaladas: Verifique se as bibliotecas mencionadas nos pré-requisitos foram instaladas corretamente.
* Arquivo não encontrado: Certifique-se de que o caminho do arquivo TXT ou o diretório de destino estejam corretos.

# Contribuição
Se quiser contribuir com o projeto, sinta-se à vontade para abrir issues ou fazer pull requests!

# Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Esse `README.md` fornece uma visão geral do projeto, instruções sobre como usá-lo e outras informações relevantes. Você pode ajustá-lo conforme as necessidades do seu projeto!

