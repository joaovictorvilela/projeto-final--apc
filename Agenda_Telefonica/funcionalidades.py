# importando as validações de dados
from validacao_de_dados import *

# criando a lista/dicionário que salvará os contatos
lista_contato = []
contatos = {}

# função que irá verificar a existência do nome na lista
def existeNome(lista_contato,nome):
    # primeiro eu verifico se a o tamanho da lista é maior que zero 
    # (se existe contatos cadastrados)
    if len(lista_contato) > 0:
        # se a condição for satisfeite eu percorro o dicionário e 
        # verifico a chave nome se existe o nome
        for contato in lista_contato:
            if contato['Nome'] == nome:
                return True
                # se existir ele retorna verdadeiro caso contrário ele retorna falso
    return False
    
# essa função adiciona o contato
def AdicionarContato(lista_contato):
    # invoco a função existe nome e verifico se o nome já existe
    while True:
        nome = validar_nome('Nome: ')
        if not existeNome(lista_contato,nome): # se ele não estiver na lista eu adiciono ele no dicionário e peço as demais informações e encerro o loop
            contatos['Nome'] = nome
            break
        # caso contrário eu imprimo uma mensagem
        else:
            print('Nome já utilizado, tente um nome diferente!')
    
    # quando o laço anterior acabar eu peço as outras informações 
    contatos['E-mail'] = validar_email('E-mail: ')
    contatos['Tel'] = validar_numero('Número: ')

    # mensagem que confirma a operação
    print(f'\nNovo contato cadastrado: {contatos["Nome"]}')

    # adiciono uma cópia dos diconário
    lista_contato.append(contatos.copy())
    # limpo o dicionário
    contatos.clear()


def RemoverContato():
    # verifico o tamanho da lista
    if len(lista_contato) > 0:
        nome = validar_nome('Nome: ')
        # peço o nome que o usuário que remover
        if existeNome(lista_contato,nome):
            # faço um for enumerate e exibo as informações 
            for i,v in enumerate(lista_contato):
                if v['Nome'] == nome:
                    print(f'ID: {i+1}')
                    print(f'\tNome: {v["Nome"].title()}\n\tE-mail: {v["E-mail"]}\n\tCell: {v["Tel"]}')

                    # deleto o contato na posição do i
                    del lista_contato[i]
                    print('O contato foi excluído com sucesso!')
        else:
            # se o nome não existir
            print('Não existe contatos com esse nome!')
    else:
        # se o tamanho for igual a 0
        print(f'Não existe contatos cadastrados!')


def AlterarContato(lista_contato):
    # verifico o tamanho da lista
    if len(lista_contato) > 0:
        nome = validar_nome('Nome: ')
        if existeNome(lista_contato,nome):
            # percorro a lista e exibo as info do contato e em seguida peço o novo email e número
            for i,v in enumerate(lista_contato):
                if v['Nome'] == nome:
                    print(f'ID: {i+1}')
                    print(f'\tNome: {v["Nome"].title()}\n\tE-mail: {v["E-mail"]}\n\tCel: {v["Tel"]}')
                    print()
                    v['E-mail'] = validar_email('Novo E-mail: ')
                    v['Tel'] = validar_numero('Novo número: ')
                    print('\nO contato foi atualizado com sucesso!')
        else:
            print('Não existe contatos com esse nome!')
    else:
        print(f'Não existe contatos cadastrados!')


def LocalizarContato(lista_contato):
    # função que localiza os contatos
    if len(lista_contato) > 0: # verificando o tamanho da lista
        nome = validar_nome('Nome: ')
        if existeNome(lista_contato,nome): # se existir o nome exiba as informações do contato
            for i,v in enumerate(lista_contato):
                if v['Nome'] == nome:
                    print(f'ID: {i+1}')
                    print(f'\tNome: {v["Nome"].title()}\n\tE-mail: {v["E-mail"]}\n\tCell: {v["Tel"]}')
        else:
            # se não tiver o contato com esse nome
            print('Não existe contatos com esse nome!')
    else:
        # se o taamnho for igual a 0
        print(f'Não existe contatos cadastrados!')


def ListarContato(lista_contato):
    # verificando o tamanho da lista
    if len(lista_contato) > 0:
        # percorrendo a lista e exibindo os contatos
        for i,v in enumerate(lista_contato):
            print(f'ID: {i+1}')
            print(f'\tNome: {v["Nome"].title()}\n\tE-mail: {v["E-mail"]}\n\tCell: {v["Tel"]}')
    else:
        # caso o valor seja menor ou igual a zero
        print(f'Não existe contatos cadastrados!')


# essa função escreve os contatos no bloco de notas
def escrever_no_arq():
    # essa parte é padrão, defino o nome e método
    arquivo = open('Lista_de_Contatos.txt','w')
    # faço um for e escrevo os contatos no arquivo
    for i,v in enumerate(lista_contato):
        arquivo.write(f'ID: {i+1}')
        arquivo.write(f'\tNome: {v["Nome"].title()}\n\tE-mail: {v["E-mail"]}\n\tCell: {v["Tel"]}\n')
        # pulando uma linha para separar os contatos
        arquivo.write('\n')
    # fechando o arquivo
    arquivo.close()
