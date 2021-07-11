from time import sleep


def menu():
    print('-=' * 30) 
    print(f'{"Menu de Opções":^60}')
    print('-=' * 30)
    print('[1] - Adicionar Contato\n[2] - Remover Contato\n[3] - Alterar Contato\n[4] - Listar Contatos\n[5] - Localizar Contato\n[0] - Sair')
    print('-=' * 30)

def sair():
    print('Encerrando o programa...')
    sleep(1)
    print('Obrigado e volte sempre!')
