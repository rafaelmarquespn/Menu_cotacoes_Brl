#funções para requisição e print dos dados
from app import request_data_new as rq



def cotacao(opcao):
    if opcao == '1':
        price = rq.RequisicaoJson('USDBRL', 'bid')
        price = f'{float(price):.2f}'
        print(f'A cotação do dólar para o real é :')
        print(f'R${price}')
    if opcao == '2':
        price = rq.RequisicaoJson('EURBRL', 'bid')
        price = f'{float(price):.2f}'
        print(f'A cotação do euro para o real é :')
        print(f'R${price}')
    if opcao == '3':
        price = rq.RequisicaoJson('BTCBRL', 'bid')
        price = f'{float(price):.2f}'
        print(f'A cotação do bitcoin para o real é :')
        print(f'R${price}')
    return


def data(opcao):
    if opcao =='1':
        print(f'A obtenção desses dados foi feita no dia :\n',rq.RequisicaoJson('USDBRL', 'create_date'))
    if opcao =='2':
        print(f'A obtenção desses dados foi feita no dia :\n',rq.RequisicaoJson('EURBRL', 'create_date'))
    if opcao== '3':
        print(f'A obtenção desses dados foi feita no dia :\n',rq.RequisicaoJson('BTCBRL', 'create_date'))




def menor_cotacao(opcao):
    if opcao == '1':
        print((f'A menor taxa de câmbio foi de :\n R$'), rq.RequisicaoJson('USDBRL', 'low'))
    if opcao == '2':
        print(f'A menor taxa de câmbio foi de :\n R$', rq.RequisicaoJson('EURBRL', 'low'))
    if opcao == '3':
        print(f'A menor taxa de câmbio foi de :\n R$', rq.RequisicaoJson('BTCBRL', 'low'))




def maior_cotacao(opcao):
    if opcao == '1':
        print(f'A maior taxa de câmbio foi de :\n R$', rq.RequisicaoJson('USDBRL', 'high'))
    if opcao == '2':
        print(f'A maior taxa de câmbio foi de :\n R$', rq.RequisicaoJson('EURBRL', 'high'))
    if opcao == '3':
        print(f'A maior taxa de câmbio foi de :\n R$', rq.RequisicaoJson('BTCBRL', 'high'))