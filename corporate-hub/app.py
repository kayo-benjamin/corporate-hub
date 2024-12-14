import json as js
import os

DADOS = "empresa.json"
empresas = []

def carregar_dados():
    """
    Carrega os dados das empresas armazenados no arquivo JSON.

    - Verifica se o arquivo existe e não está vazio.
    - Lê o conteúdo do arquivo e converte em uma lista de dicionários.
    - Adiciona o campo "ativo" como False para empresas que não possuem esse campo.
    - Caso o arquivo não exista ou esteja vazio, inicializa a lista de empresas como vazia.
    """
    global empresas
    if os.path.exists(DADOS) and os.path.getsize(DADOS) > 0:
        with open(DADOS, 'r') as arquivo:
            empresas = js.load(arquivo)
            for empresa in empresas:
                if "ativo" not in empresa:
                    empresa["ativo"] = False
    else:
        empresas = []

def salvar_dados():
    """
    Salva os dados das empresas no arquivo JSON.

    - Escreve a lista de empresas no arquivo especificado com indentação para melhor legibilidade.
    """
    with open(DADOS, 'w') as arquivo:
        js.dump(empresas, arquivo, indent=4)

def exibir_sub_titulo(texto):
    """
    Exibe um subtítulo formatado.

    - Limpa a tela antes de exibir.
    - Imprime o texto com uma linha de asteriscos acima e abaixo do texto.

    Parâmetros:
        texto (str): O texto a ser exibido como subtítulo.
    """
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    """
    Exibe uma mensagem indicando que a opção escolhida é inválida.

    - Limpa a tela antes de exibir a mensagem.
    """
    os.system('cls')
    print('Opção inválida\n')

def lista_empresa():
    """
    Exibe a lista de empresas cadastradas.

    - Mostra os detalhes de cada empresa, incluindo nome, ramo, email, telefone,
      endereço e status (Ativo/Inativo).
    - Caso não existam empresas cadastradas, informa ao usuário.
    """
    exibir_sub_titulo("Lista das Empresas:")
    if not empresas:
        print("Nenhuma empresa cadastrada!\n")
    else:
        for i, empresa in enumerate(empresas, start=1):
            print(f"{i}.   Nome: {empresa['nome']}")
            print(f"     Ramo: {empresa['ramo']}")
            print(f"     Email: {empresa['email']}")
            print(f"     Telefone: {empresa['telefone']}")
            print(f"     Endereço: {empresa['endereco']}")
            status = "Ativo" if empresa["ativo"] else "Inativo"
            print(f"     Status: {status}")

def cadastro_empresa():
    """
    Realiza o cadastro de uma nova empresa.

    - Solicita as informações da empresa ao usuário.
    - Exibe os dados coletados para confirmação antes de salvar.
    - Adiciona a nova empresa à lista e salva os dados no arquivo JSON.
    """
    exibir_sub_titulo("Cadastre sua empresa abaixo:")
    nome_empresa = input("Nome ou razão social: ")
    ramo_empresa = input("Ramo: ")    
    email_impresa = input("Email: ")
    telefone_impresa = input("Telefone: ")
    endereco_impresa = input("Endereço: ")
    print("\nSeus Dados:")
    print(f"{nome_empresa}\n{ramo_empresa}\n{email_impresa}")
    print(f"{telefone_impresa}\n{endereco_impresa}")
    resp = input("Os dados da empresa estão corretos (s/n)? ")
    if resp.lower() == "s":
        empresas.append({
            "nome": nome_empresa,
            "ramo": ramo_empresa,
            "email": email_impresa,
            "telefone": telefone_impresa,
            "endereco": endereco_impresa,
            "ativo": False
        })
        salvar_dados()
        print(f"Dados armazenados. {nome_empresa} cadastrada com sucesso!\n")
    else:
        print("Refaça o cadastro.")

def ativar_empresa():
    """
    Ativa uma empresa cadastrada.

    - Exibe a lista de empresas para seleção.
    - Solicita o ID da empresa e ativa seu status caso esteja inativo.
    - Salva as alterações no arquivo JSON.
    """
    lista_empresa()
    if not empresas:
        print("Nenhuma empresa cadastrada. Escolha a opção 1 para cadastrar")
    else:
        try:
            id = int(input("Digite o ID da empresa que deseja ativar: "))
            if 1 <= id <= len(empresas):
                empresa = empresas[id - 1]
                if not empresa["ativo"]:
                    empresa["ativo"] = True
                    salvar_dados()
                    print(f"{empresa['nome']} ativado com sucesso!\n")
                else:
                    print(f"{empresa['nome']} já está ativo.")
            else:
                print("ID inválido. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Digite um número válido.\n")

def desativar_empresa():
    """
    Desativa uma empresa cadastrada.

    - Exibe a lista de empresas para seleção.
    - Solicita o ID da empresa e desativa seu status caso esteja ativo.
    - Salva as alterações no arquivo JSON.
    """
    lista_empresa()
    if not empresas:
        print("Nenhuma empresa cadastrada. Escolha a opção 1 para cadastrar")
    else:
        try:
            id = int(input("Digite o ID da empresa que deseja desativar: "))
            if 1 <= id <= len(empresas):
                empresa = empresas[id - 1]
                if empresa["ativo"]:
                    empresa["ativo"] = False
                    salvar_dados()
                    print(f"{empresa['nome']} desativado com sucesso!\n")
                else:
                    print(f"{empresa['nome']} já está desativado.\n")
            else:
                print("ID inválido. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Digite um número válido.\n")

def apagar_empresa():
    """
    Apaga uma empresa cadastrada.

    - Exibe a lista de empresas para seleção.
    - Solicita o ID da empresa e a remove da lista.
    - Salva as alterações no arquivo JSON.
    """
    os.system('cls')
    lista_empresa()
    if not empresas:
        print("Escolha a opção 1 para cadastrar")
    else:
        try:
            id = int(input("Digite o número da empresa que deseja apagar: "))
            if 1 <= id <= len(empresas):
                del empresas[id - 1]
                salvar_dados()
                print("Empresa apagada com sucesso!")
            else:
                print(f"Empresa com ID {id} não encontrada.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.\n")

def editar_empresa():
    """
    Edita os dados de uma empresa cadastrada.

    - Exibe a lista de empresas para seleção.
    - Solicita o ID da empresa e permite alterar seus dados.
    - Atualiza os dados no arquivo JSON.
    """
    os.system('cls')
    lista_empresa()
    if not empresas:
        print("Escolha a opção 1 para cadastrar")
    else:
        try:
            id = int(input("Digite o número da empresa que deseja editar: "))
            if 1 <= id <= len(empresas):
                print("\n\tEditar empresa: \n")
                nome = input("Nome: ")
                ramo = input("Ramo: ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                endereco = input("Endereço: ")
                empresas[id - 1]["nome"] = nome
                empresas[id - 1]["ramo"] = ramo
                empresas[id - 1]["email"] = email
                empresas[id - 1]["telefone"] = telefone
                empresas[id - 1]["endereco"] = endereco
                salvar_dados()
                print("Empresa editada com sucesso!")
            else:
                print("Empresa não encontrada!")
        except ValueError:
            print("Entrada inválida. Digite um número válido.\n")

def finalizar_app():
    """
    Encerra o aplicativo.

    - Exibe uma mensagem de saída antes de finalizar o programa.
    """
    exibir_sub_titulo('Saindo...')
    exit()

def menu_principal():
    """
    Exibe o menu principal com as opções disponíveis.

    - Mostra as opções numeradas para interagir com o sistema.
    """
    print('\t𝑪𝒐𝒓𝒑𝒐𝒓𝒂𝒕𝒆𝑯𝒖𝒃\n')
    print('1. Cadastrar Empresa')
    print('2. Listar Empresas')
    print('3. Ativar Empresa')
    print('4. Desativar Empresa')
    print('5. Apagar Empresa')
    print('6. Editar Empresa')
    print('7. Sair\n')

def escolher_opcao():
    """
    Lida com a navegação do menu principal.

    - Permite ao usuário escolher uma opção do menu.
    - Direciona para a função correspondente à escolha.
    - Mantém o loop até que o usuário escolha a opção de sair.
    """
    while True:
        try:
            opcao = int(input('Escolha uma opção: '))
            match opcao:
                case 1:
                    cadastro_empresa()
                case 2:
                    lista_empresa()
                case 3:
                    ativar_empresa()
                case 4:
                    desativar_empresa()
                case 5:
                    apagar_empresa()
                case 6:
                    editar_empresa()
                case 7:
                    finalizar_app()
                case _:
                    opcao_invalida()
        except ValueError:
            opcao_invalida()
        input('\nPressione qualquer tecla para voltar ao menu principal ')
        os.system('cls')
        menu_principal()

def main():
    """
    Função principal do programa.

    - Carrega os dados das empresas antes de iniciar.
    - Exibe o menu principal e lida com as interações do usuário.
    """
    carregar_dados()
    os.system('cls')
    menu_principal()
    escolher_opcao()

if __name__ == '__main__':
    main()
