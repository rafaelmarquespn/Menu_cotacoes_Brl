import os
from time import sleep
import app
from app import request_data_new as rq
from app import menus_reservas as mr
from app import funcoes_requisicoes as fr
import rich
from rich.style import Style
from rich.console import Console


console = Console()


#------------------------------------------------------------------------------
# MENU DOS JOGOS
#------------------------------------------------------------------------------

def pause():
    os.system('pause')

opcoes_camb = {1:'DÓLAR -> REAL', 2:'EURO -> REAL', 3:'BITCOIN -> REAL'}
opcoes_filtros = {1:'COTAÇÃO', 2: 'DATA', 3:'MENOR OFERTA DO DIA', 4:'MAIOR OFERTA DO DIA'}

while True:
# Menu
    print(f'='*40)
    console.print(f' '* 13, 'COTAÇÕES:', style = "red")
    print(f'='*40)

# opcoes do menu principal   
    print('_'*40)
    print('[1] DÓLAR -> REAL')
    print('[2] EURO -> REAL')
    print('[3] BITCOIN -> REAL')
    print('[4] Sair')
    print('_'*40)
#input para guardar valor escolhido
    opcao = input('Escolha uma opção de Câmbio: ')
    #os.system("cls")
    match opcao:
        case '1':
            #Menu secundario
            print(f'Opção {opcoes_camb[int(opcao)]} selecioanda! Aguarde...')  
            sleep(2)
            os.system("cls")
            mr.menuSecundario(opcoes_camb[int(opcao)])
            opcao2 = input('Escolha uma opção de filtro: ')
            #os.system("cls")
            match opcao2:
                case '1':
                    print('Você escolheu a opção de cotação')
                    sleep(2)
                    rq.cls()
                    fr.cotacao(opcao)
                case '2':
                    print('Você escolheu a opção de data da consulta')
                    sleep(2)
                    rq.cls()
                    fr.data(opcao)
                case '3':
                    print('Você escolheu a opção de menor cotação')
                    sleep(2)
                    rq.cls()
                    fr.menor_cotacao(opcao)
                case '4':
                    print('Você escolheu a opção de maior cotação')
                    sleep(2)
                    rq.cls()
                    fr.maior_cotacao(opcao)
                case '5':
                    print('Voltando...')
                    sleep(2)
                    mr.menuPrincipal()
                case '6':
                    print('Saindo...')
                    sleep(2)
                    exit()
                case other:
                    print('Escolhendo opção...')
                    sleep(2)
                    print(f'Opção invalida.Tente novamente')
                    sleep(2)         
            pause()
            rq.cls()
        case '2':
            #Menu secundario
            print(f'Opção {opcoes_camb[int(opcao)]} selecioanda! Aguarde...')  
            sleep(2)
            os.system("cls")
            mr.menuSecundario(opcoes_camb[int(opcao)])
            opcao2 = input('Escolha uma opção de filtro: ')
            match opcao2:
                case '1':
                    print('Você escolheu a opção de cotação')
                    sleep(2)
                    rq.cls()
                    fr.cotacao(opcao)
                case '2':
                    print('Você escolheu a opção de data da consulta')
                    sleep(2)
                    rq.cls()
                    fr.data(opcao)
                case '3':
                    print('Você escolheu a opção de menor cotação ')
                    sleep(2)
                    rq.cls()
                    fr.menor_cotacao(opcao)
                case '4':
                    print('Você escolheu a opção de maior cotação')
                    sleep(2)
                    rq.cls()
                    fr.maior_cotacao(opcao)
                case '5':
                    print('Voltando...')
                    sleep(2)
                    mr.menuPrincipal()
                case '6':
                    print('Saindo...')
                    sleep(2)
                    exit()
                case other:
                    print('Escolhendo opção...')
                    sleep(2)
                    print(f'Opção invalida.Tente novamente')
                    sleep(2)          
            pause()
        case '3':
            #Menu secundario
            print(f'Opção {opcoes_camb[int(opcao)]} selecioanda! Aguarde...')  
            sleep(2)
            os.system("cls")
            mr.menuSecundario(opcoes_camb[int(opcao)])
            opcao2 = input('Escolha uma opção de filtro: ')
            match opcao2:
                case '1':
                    print('Você escolheu a opção de cotação')
                    sleep(2)
                    rq.cls()
                    fr.cotacao(opcao)
                case '2':
                    print('Você escolheu a opção de data da consulta')
                    sleep(2)
                    rq.cls()
                    fr.data(opcao)
                case '3':
                    print('Você escolheu a opção de menor cotação')
                    sleep(2)
                    rq.cls()
                    fr.menor_cotacao(opcao)
                case '4':
                    print('Você escolheu a opção de maior cotação')
                    sleep(2)
                    rq.cls()
                    fr.maior_cotacao(opcao)
                case '5':
                    print('Voltando...')
                    sleep(2)
                    mr.menuPrincipal()
                case '6':
                    print('Saindo...')
                    sleep(2)
                    exit()
                case other:
                    print(f'Opção invalida.Tente novamente')
                    sleep(2)         
            pause()
        case '4':
            print('Saindo...')
            sleep(2)
            exit()
        case other:
            print(f'Opção invalida.Tente novamente')
            sleep(2)
