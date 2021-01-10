# funçõs que irão garantir que o usuário irá digirtar um valor válido para o
#  programa, todas elas irão ter um parâmetro mensagem que será a mensgem 
# exibida  em cada caso, a diferença delas é basicamente a lógica de
#  verificação que será diferente em cada caso

def validar_entrada(msg):
    tudo_certo = False
    opcao = 0
    while True:
        entrada = str(input(msg))
        # verifica se é um número e se está dentro do intervalo 0-5
        if entrada.isnumeric() and int(entrada) >= 0 and int(entrada) <= 5:
            opcao = int(entrada) 
            tudo_certo = True
        else:
            print('ERRO! informe uma opção válida.')
        
        if tudo_certo:
            break
    return opcao


def validar_nome(msg):
    tudo_certo = False
    nome = ''
    while True:
        entrada = str(input(msg))
        # verifica se não é um número e se não está vazio
        if not entrada.isnumeric() and entrada.strip() != '':
            nome = entrada
            tudo_certo = True
        else:
            print('ERRO! informe um nome válido.')
        
        if tudo_certo:
            break
    return nome


def validar_numero(msg):
    tudo_certo = False
    numero = 0
    while True:
        entrada = str(input(msg)).strip()
        # verifica se é um número e se não está vazio
        if entrada.isnumeric() and entrada.strip() != '':
            numero = int(entrada)
            tudo_certo = True
        else:
            print('ERRO! informe um número válido.')
        
        if tudo_certo:
            break
    return numero


def validar_email(msg):
    tudo_certo = False
    email = ''
    while True:
        entrada = str(input(msg))
        # verifica se não está vazio
        if entrada.strip() != '':
            email = entrada
            tudo_certo = True
        else:
            print('ERRO! informe um e-mail válido.')
        
        if tudo_certo:
            break
    return email
