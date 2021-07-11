from validacao_de_dados import *

lista_contato = []
contatos = {}

def existeNome(lista_contato,nome):
    if len(lista_contato) > 0:
        for contato in lista_contato:
            if contato['Nome'] == nome:
                return True
    return False
    
def AdicionarContato(lista_contato):
    while True:
        nome = validar_nome('Nome: ')
        if not existeNome(lista_contato,nome): 
            contatos['Nome'] = nome
            break
        else:
            print('Nome já utilizado, tente um nome diferente!')
     
    contatos['E-mail'] = validar_email('E-mail: ')
    contatos['Tel'] = validar_numero('Número: ')

    print(f'\nNovo contato cadastrado: {contatos["Nome"]}')

    lista_contato.append(contatos.copy())
    contatos.clear()


def RemoverContato():
    if len(lista_contato) > 0:
        nome = validar_nome('Nome: ')
        if existeNome(lista_contato,nome):
            for i,v in enumerate(lista_contato):
                if v['Nome'] == nome:
                    print(f'ID: {i+1}')
                    print(f'\tNome: {v["Nome"].title()}\n\tE-mail: {v["E-mail"]}\n\tCell: {v["Tel"]}')
                    del lista_contato[i]
                    print('O contato foi excluído com sucesso!')
        else:
            print('Não existe contatos com esse nome!')
    else:
        print(f'Não existe contatos cadastrados!')


def AlterarContato(lista_contato):
    if len(lista_contato) > 0:
        nome = validar_nome('Nome: ')
        if existeNome(lista_contato,nome):
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
    if len(lista_contato) > 0: 
        nome = validar_nome('Nome: ')
        if existeNome(lista_contato,nome): 
            for i,v in enumerate(lista_contato):
                if v['Nome'] == nome:
                    print(f'ID: {i+1}')
                    print(f'\tNome: {v["Nome"].title()}\n\tE-mail: {v["E-mail"]}\n\tCell: {v["Tel"]}')
        else:
            print('Não existe contatos com esse nome!')
    else:
        print(f'Não existe contatos cadastrados!')


def ListarContato(lista_contato):
    if len(lista_contato) > 0:
        for i,v in enumerate(lista_contato):
            print(f'ID: {i+1}')
            print(f'\tNome: {v["Nome"].title()}\n\tE-mail: {v["E-mail"]}\n\tCell: {v["Tel"]}')
    else:
        print(f'Não existe contatos cadastrados!')

def escrever_no_arq():
    arquivo = open('Lista_de_Contatos.txt','w')
    for i,v in enumerate(lista_contato):
        arquivo.write(f'ID: {i+1}')
        arquivo.write(f'\tNome: {v["Nome"].title()}\n\tE-mail: {v["E-mail"]}\n\tCell: {v["Tel"]}\n')
        arquivo.write('\n')
    arquivo.close()
