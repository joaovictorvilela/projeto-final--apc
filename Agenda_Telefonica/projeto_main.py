from validacao_de_dados import *
from formatacao import *
from funcionalidades import * 

def main():
    while True: 
        menu()
        opcao = validar_entrada('Informe a opção desejada: ') 
        print()
        if opcao == 0:
            sair()
            break
        else:
            if opcao == 1:
                AdicionarContato(lista_contato)
                escrever_no_arq()
            elif opcao == 2:
                RemoverContato()
                escrever_no_arq()
            elif opcao == 3:
                AlterarContato(lista_contato)
                escrever_no_arq()
            elif opcao == 4:
                ListarContato(lista_contato)
            elif opcao == 5:
                LocalizarContato(lista_contato)
main()

