import os

restaurantes = [{'nome': 'Praça', 'categoria':'german', 'ativo':False},
                {'nome':'PizzaSup', 'categoria':'italiana', 'ativo':True},
                { 'nome':'CantinaItaly', 'categoria':'restaurante', 'ativo':False}
]

def exibir_nome_programa():
    '''Essa função é responsável por exibir o nome do Programa'''
    print("""
    
█▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 █▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
▀▀█ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 █▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ▀▀▀ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
""")

def exibir_opcoes(): 
    '''Essa função é responsável por exibir o painel de opções do usuário'''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print('4. Finalizar o App')

def finalizar_app():
    '''Essa função é responsável por exibir a finalização do app.'''
    exibir_subtitulo('App finalizado')


def voltar_menu_principal():
    '''Essa função é responsável por levar o usuário de volta para o menu principal após selecionar
    alguma opção. '''
    input('Digite uma tecla para voltar ao menu: ')
    main()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir os subtítulos de cada sessão
    quando chamada. '''
    os.system("cls")
    linha = "*"  * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def opcao_invalida():
    '''Essa função é responsável por exibir na tela "Opção inválida
    e levar o usuário para o menu principal.
    '''
    print("Opção Inválida")
    voltar_menu_principal()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante e voltar ao menu principal'''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_restaurantes = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False} #como regra de negócio, todo restaurante cadastrado terá o ativo como False
    restaurantes.append(dados_restaurantes)
    print(f"Restaurante {nome_do_restaurante} foi adicionado com sucesso. ")

    voltar_menu_principal()

def altenar_estado_restaurante():
    ''' Essa função é responsável por alternar o Status do restaurante
    entre Ativado e Desativado '''
    exibir_subtitulo("Alterando o Estado do Restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_escontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_escontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_escontrado:
        print("Restaurante não encontrado. ")

    voltar_menu_principal()

def listar_restaurantes():
    ''' Essa função é responsável por  listar os restaurantes '''
    # os restaurantes só ficam armazenados durante a execução do programa.
    exibir_subtitulo("Restaurantes cadastrados: ")
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        situacao = 'ativado' if restaurante['ativo'] else 'desativado' #utilizando operador ternário
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {situacao.ljust(20)}")

    voltar_menu_principal()



def escolher_opcao():
    ''' essa função tem como fito permitir que o usuário escolha a opção desejada
    e seja direcionado para a respectiva sessão da opção. '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match(opcao_escolhida):
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                altenar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()