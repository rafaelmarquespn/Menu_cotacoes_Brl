import app

def menuPrincipal():
    opcao=''
    print(f'='*40)
    print(f' ' * 13, 'COTAÇÕES:')
    print(f'='*40)
    print('_'*40)
    print('[1] DÓLAR -> REAL')
    print('[2] EURO -> REAL')
    print('[3] BITCOIN -> REAL')
    print('[4] Voltar')
    print('[5] Sair')
    print('_'*40)

def menuSecundario(opcao):
    print(f'='*40)
    print(f'cambio escolhido: {opcao}')
    print(f'='*40)
       #opcoes do segundo menu
    print('_'*40)
    print('1- Cotação')
    print('2- Data')
    print('3- Menor oferta do dia')
    print('4- Maior oferta do dia')
    print('5- Voltar')
    print('6- Sair')
    print('_'*40)
