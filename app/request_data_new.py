#Requisição de dados com delay

def cls():
    import os
    os.system('cls')




def delay(t = 10):
    import random
    import time
    if t < 2:
        t=10
    delays = list(range(1, t))
    random.shuffle(delays)
    num_of_secs = random.choice(delays)
    print(f'Aguarde {num_of_secs}s ', end='')
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:2d}'.format(s)
        if (s > 1 and s < num_of_secs):
            print(min_sec_format, end='s... ')
        time.sleep(1)
        num_of_secs -= 1
        if (num_of_secs != 0):
            print(f'{num_of_secs}s ', end='')
    print('FIM!')




def RequisicaoJson(Trade, filter):
    delay(5)
    import json
    import requests
    import os
    data = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    if data.status_code == 200:
        print('Perfecto!')
        dic_prices = json.loads(data.content)
        parameter =  dic_prices[Trade][filter]
        return parameter
    else:
        print('ihhh, deu ruim')


