# Sistema de Gestão de Empresas

Este é um sistema simples para gerenciamento de empresas desenvolvido em Python. Ele permite cadastrar, listar, editar, ativar/desativar, e excluir registros de empresas, utilizando um arquivo JSON para armazenamento dos dados.

## Funcionalidades

1. **Cadastrar Empresa**:
   - Permite adicionar novas empresas com informações como nome, ramo, e-mail, telefone, endereço e status (ativo/inativo).

2. **Listar Empresas**:
   - Exibe todas as empresas cadastradas com seus detalhes, como nome, ramo, e-mail, telefone, endereço e status.

3. **Ativar Empresa**:
   - Altera o status de uma empresa para "Ativo".

4. **Desativar Empresa**:
   - Altera o status de uma empresa para "Inativo".

5. **Editar Empresa**:
   - Permite alterar os dados de uma empresa cadastrada.

6. **Apagar Empresa**:
   - Remove uma empresa da base de dados.

7. **Sair do Sistema**:
   - Encerra o programa com uma mensagem de despedida.

## Estrutura do Código

- **`carregar_dados()`**: Carrega os dados do arquivo JSON e inicializa a lista de empresas.
- **`salvar_dados()`**: Salva a lista de empresas no arquivo JSON.
- **Funções específicas**: Cada funcionalidade (cadastrar, listar, ativar, etc.) está implementada em uma função separada, garantindo modularidade.
- **`menu_principal()`**: Exibe o menu principal com as opções numeradas.
- **`escolher_opcao()`**: Realiza a navegação entre as opções do menu.
- **`main()`**: Função principal que inicializa o sistema.

## Pré-requisitos

- Python 3.6 ou superior
- Sistema operacional compatível com o comando `os.system('cls')` para limpar a tela (como Windows).

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. Execute o script Python:
   ```bash
   python nome_do_arquivo.py
   ```

## Estrutura de Arquivos

- **`empresa.json`**: Arquivo utilizado para armazenar os dados das empresas em formato JSON.
- **`nome_do_arquivo.py`**: Script principal com a implementação do sistema.

## Melhorias Futuras

- Adicionar validações mais robustas para entradas do usuário.
- Implementar um sistema de busca por empresas.
- Melhorar a interface com bibliotecas como `curses` ou `rich`.
- Tornar o sistema multiplataforma (ajustar o comando de limpar tela).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um *pull request* ou relatar problemas na seção de *issues*.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

