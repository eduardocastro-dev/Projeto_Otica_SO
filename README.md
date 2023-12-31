# Ótica SO - Sistema de Gerenciamento de Ótica

O **Projeto Ótica SO** é um sistema desenvolvido em Python utilizando a biblioteca gráfica QtDesing. Ele foi criado com o objetivo de ser uma solução de gerenciamento completo para lojas de ótica de pequeno porte.

## Funcionalidades

O sistema possui diversas funcionalidades voltadas especificamente para o gerenciamento de lojas de ótica:

- Cadastro e controle de clientes, fornecedores e produtos.
- Emissão de notas fiscais de entrada (NFCE) e controle de estoque de produtos.
- Geração de ordens de serviço para controle de reparos e vendas.
- Geração de relatórios de vendas, estoque, financeiros e de ordens de serviço.
- Possibilidade de exportar relatórios para arquivos Excel e PDF.

## Organização do Projeto

- O projeto segue uma arquitetura de camadas, separando a lógica de negócio da interface gráfica.
- É utilizado o banco de dados SQLite para armazenamento dos dados do sistema.
- A biblioteca gráfica QtDesing é utilizada para criação da interface do usuário.

## Requisitos do Sistema

- Python 3.x
- Bibliotecas: PyQt5, sqlite3, openpyxl, reportlab

## Como Executar o Projeto

1. Faça o clone do repositório: `git clone https://github.com/eduardocastro-dev/Projeto_Otica_SO.git`.
2. Certifique-se de ter o Python 3.x instalado em seu ambiente.
3. Instale as bibliotecas necessárias executando: `pip install -r requirements.txt`.
4. Navegue até o diretório do projeto: `cd Projeto_Otica_SO`.
5. Execute o arquivo principal: `python main.py`.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests, relatar problemas ou sugerir melhorias.

## Licença

Este projeto está licenciado nos termos da licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

## Aplicabilidade

O projeto é destinado a clientes de pequeno porte no nicho de lojas de ótica que buscam uma solução abrangente para o gerenciamento de sua loja. Ele foi projetado para ser uma aplicação funcional e prática, visando facilitar as operações diárias e fornecer informações necessárias para uma gestão eficiente.
