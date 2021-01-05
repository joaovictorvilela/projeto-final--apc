# importando todos os módulos 
from validacao_de_dados import *
from formatacao import *
from funcionalidades import * 

# função principal
def main():
    while True: 
        menu() # invocando a função menu
        opcao = validar_entrada('Informe a opção desejada: ') # pedindo a opção
        print() # print para pular de linha
        # condição para parar o laço
        if opcao == 0:
            sair()
            break
        else:
            # demais opções do programa
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

