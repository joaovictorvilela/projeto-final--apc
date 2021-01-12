# importando o módulo sleep do python para dar um efeito na função sair
from time import sleep


# função que irá exibir as opções disponíveis para o usuário
def menu():
    print('-=' * 30) 
    print(f'{"Menu de Opções":^60}')
    print('-=' * 30)
    print('[1] - Adicionar Contato\n[2] - Remover Contato\n[3] - Alterar Contato\n[4] - Listar Contatos\n[5] - Localizar Contato\n[0] - Sair')
    print('-=' * 30)

# função que irá exibir uma mensagem para o usuário quando ele escolher sair
def sair():
    print('Encerrando o programa...')
    # aqui entra o sleep ele irá esperar um tempo para mostrar o próximo print
    sleep(1)
    print('Obrigado e volte sempre!')
