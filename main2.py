import talib as tb
from datetime import datetime
hj = datetime.now()
from math import ceil
import MetaTrader5 as mt5
from time import sleep
import os
from openpyxl import load_workbook
# ==========================================================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
# ==========================================================================================
import pandas as pd

pd.set_option('display.max_columns', 500)  # número de colunas
pd.set_option('display.width', 1500)  # largura máxima da tabela
# ==========================================================================================
#   EXCEL
planilha = load_workbook('binomo.xlsx')
book = planilha['Planilha1']
# ==========================================================================================
# =====IF DE FUSO HORÁRIO PARA LIDAR COM O METATRADER===
hora = datetime.now().strftime('%H:%M:%S')
hour = 0
if int(hora[0:2]) >6 and int(hora[0:2]) <= 18:
    hour = int(hora[0:2]) + 5
elif int(hora[0:2]) == 19:
    hour = 0
elif int(hora[0:2]) == 20:
    hour = 1
elif int(hora[0:2]) == 21:
    hour = 2
elif int(hora[0:2]) == 22:
    hour = 3
elif int(hora[0:2]) == 23:
    hour = 4
elif int(hora[0:2]) == 00:
    hour = 5
elif int(hora[0:2]) >00 and int(hora[0:2]) <= 6:
    hour = hj.hour + 5

sleep(5)
print('Robô de Web Automação Binomo')
print('')
print(
'O navegador ira iniciar em alguns instantes\nBasta apenas fazer login e passar pela CHAPTA,\nescolher um ativo aqui novamente,\ne o robô ja estará operando para você!')
sleep(3)
print('')
print('Abrindo o navegador...')
print('=' * 45)
print('')

#   ABRIR NAVEGADOR
nav = webdriver.Chrome(service=service)
#   ENTRANDO NO SITE DA REVAL
nav.get('https://binomo.com/trading')
str(input('Após ter feito login, tecle ENTER para continuar: '))
# ===================================ROBÔ======================================================================
# =============INPUTS=================
os.system('cls')
# Escolher o ativo
print(
'Agora para a escolha do ativo, escola um ativo que deixe muitos pavios\nno grafico de 5 minutos, pois a estratégia do Robô, é a Retração.')
print('')
ativo = str(input('Digite o ativo FOREX que deseja operar (Ex. eur/usd): ')).strip().upper()
if not '/' in ativo:
    while True:
        print('ERRO!!! Verifique se o ativo foi digitado corretamente.')
        ativo = str(input('Digite o ativo FOREX que deseja operar (Ex. eur/usd): ')).strip().upper()
        if '/' in ativo and len(ativo) == 7:
            break
sleep(2)
nav.find_element(By.XPATH,'//*[@id="asset-0"]/button').click()
sleep(3)
nav.find_element(By.XPATH,'//*[@id="assets-list-popover"]/div[2]/assets-block/asset-search/vui-input/div[1]/div[2]/vui-input-text/input').send_keys(f'{ativo}')
sleep(3)
nav.find_element(By.XPATH,'//*[@id="qa_trading_assetDialog"]/lib-platform-scroll/div/div/section/div[2]').click()
sleep(3)
print('')
print('Escolha com o número correspondente o Gerenciamento para suas entradas')
gr = int(input('[1] 50/50 = 3.125%\n[2] Soros\n[3] Mão Fixa + Martingale\n[4] Mão Fixa\n : '))
if gr != 1 and gr != 2 and gr != 3 and gr != 4:
    while True:
        os.system('cls')
        print('ERRO!!! Escola um número com a oção correspondente.')
        gr = int(input('[1] 50/50 = 3.125%\n[2] Soros\n[3] Mão Fixa + Martingale\n[4] Mão Fixa\n : '))
        if gr == 1 or gr == 2 or gr == 3 or gr == 4:
            break
# valor das entradas
print('Agora digite o valor das entradas')
lote = int(input('(só números inteiros): '))

sleep(2)
nav.find_element(By.XPATH, '//*[@id="amount-counter"]/div[1]/div[1]/vui-input-number/input').send_keys(Keys.BACKSPACE, lote)
sleep(2)
print('ROBÔ INICIADO...')
sleep(3)
os.system('cls')
# =============================================================================================================
call = nav.find_element(By.XPATH, '//*[@id="qa_trading_dealUpButton"]/button')
put = nav.find_element(By.XPATH, '//*[@id="qa_trading_dealDownButton"]/button')
historico = nav.find_element(By.XPATH, '//*[@id="qa_historyButton"]')
click_fora = nav.find_element(By.XPATH,'//*[@id="qa_trading_abilityDashboard"]/div/vui-sidebar/div/div/div[1]/vui-icon')
cont = 0
y = 0
c = 147
r = ''
v = 0
i = 20
ce = 0
entrada = win = loss = empate = espera = 0
while True:
    # ==COLOCAR A EXPIRAÇÃO PARA 5 MINUTOS
    """
    if time[4] == '4' and time[6:] == '35':
        sleep(1)
        navegador.find_element_by_xpath('//*[@id="qa_trading_dealTimeInput"]/div[1]/div[1]/vui-input-number/input').click()
        sleep(3)
        navegador.find_element_by_xpath('//*[@id="qa_trading_dealTimeInput"]/div[1]/vui-popover/div[2]/lib-platform-scroll/div/div/div/div[1]/vui-option[5]').click()
        sleep(1)
    if time[4] == '9' and time[6:] == '35':
        sleep(1)
        navegador.find_element_by_xpath('//*[@id="qa_trading_dealTimeInput"]/div[1]/div[1]/vui-input-number/input').click()
        sleep(3)
        navegador.find_element_by_xpath('//*[@id="qa_trading_dealTimeInput"]/div[1]/vui-popover/div[2]/lib-platform-scroll/div/div/div/div[1]/vui-option[5]').click()
        sleep(1)
    """


    #==========METATRADER===========================
    mt5.initialize()
    # =====IF DE FUSO HORÁRIO PARA LIDAR COM O METATRADER===
    hora = datetime.now().strftime('%H:%M:%S')
    hour = 0
    minute = 0
    if int(hora[0:2]) >6 and int(hora[0:2]) <= 18:
        hour = int(hora[0:2]) + 5
    elif int(hora[0:2]) == 19:
        hour = 0
        h4 = 18
    elif int(hora[0:2]) == 20:
        hour = 1
        h4 = 19
    elif int(hora[0:2]) == 21:
        hour = 2
        h4 = 20
    elif int(hora[0:2]) == 22:
        hour = 3
        h4 = 21
    elif int(hora[0:2]) == 23:
        hour = 4
        h4 = 22
    elif int(hora[0:2]) == 00:
        hour = 5
        h4 = 23
    elif int(hora[0:2]) == 1:
        hour = 6
        h4 = 0
    elif int(hora[0:2]) >00 and int(hora[0:2]) <= 6:
        hour = int(hj.hour) + 5

    if int(hora[4]) >5:
        minute = int(hora[3:5]) - (int(hora[4]) - 5)
    elif int(hora[4]) <5:
        minute = int(hora[3:5]) - (int(hora[4]) - 0)
    else:
        minute = int(hora[3:5])


    # ==============================ESTRATÉGIA=============================================================
    rates = mt5.copy_rates_from(f"{ativo.replace('/','')}", mt5.TIMEFRAME_M1, datetime(hj.year, hj.month, hj.day, hour, minute, hj.second), 10)
    rates_frame = pd.DataFrame(rates)
    # rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
    v = len(rates_frame) - 1
    # print(rates_frame)
    #  DADOS DAS VELAS
    close = rates_frame['close']
    open = rates_frame['open']
    high = rates_frame['high']
    low = rates_frame['low']
    #   INDICADORES
    upper, mid, lower = tb.BBANDS(close, timeperiod=9, nbdevup=1, nbdevdn=1, matype=0)
    # ============================================================================
    if close.loc[v] > upper.loc[v]:# and close.loc[v-1] < upper.loc[v-1]:
        put.click()
        cont += 1
        book[f'A{cont+1}'] = 'Entrada de VENDA'
        book[f'B{cont + 1}'] = hora
        book[f'C{cont + 1}'] = 'Preço:'
        book[f'D{cont + 1}'] = close.loc[v]
        book[f'E{cont + 1}'] = 'Banda Superior:'
        book[f'F{cont + 1}'] = upper.loc[v]
        print(f'Entrada de VENDA // {hora} // Preço: {close.loc[v]} // Banda Superior: {upper.loc[v]}')
    # APOS CALL/PUT =========================================================================================================================================================================================
        sleep(3)
        historico.click()
        sleep(3)
        minuto = int(nav.find_element(By.XPATH,'//*[@id="qa_trading_openDeal"]/vui-timer/vui-label/div/div[2]/div/span[3]').text)
        segundo = int(nav.find_element(By.XPATH,'//*[@id="qa_trading_openDeal"]/vui-timer/vui-label/div/div[2]/div/span[5]').text)
        espera = (minuto * 60) + (segundo) + 5
        sleep(2)
        print(f'{minuto}:{segundo}  // Tempo de espera em Segundos: {(minuto * 60) + segundo}')
        sleep(espera)
        preco_entrada = nav.find_element(By.XPATH,'//*[@id="qa_trading_tradeHistoryStandardTab"]/option-item[1]/div/div[2]/div[2]/p[2]').text.strip().replace('R$', '').replace(' ', '').replace(',', '.')
        if '₮' in preco_entrada:
            preco_entrada = preco_entrada.replace('₮','')
        preco_entrada = float(preco_entrada)
        preco_resultado = nav.find_element(By.XPATH,'//*[@id="qa_trading_tradeHistoryStandardTab"]/option-item[1]/div/div[2]/div[2]/p[1]').text.strip().replace('R$', '').replace(' ', '').replace(',', '.')
        if '₮' in preco_resultado:
            preco_resultado = preco_resultado.replace('₮','')
        preco_resultado = float(preco_resultado)
        if preco_resultado == 0:
            r = 'PERCA'
        elif preco_resultado > preco_entrada:
            r = 'VITÓRIA'
        elif preco_resultado == preco_entrada:
            r = 'EMPATE'
        book[f'F{cont + 1}'] = f'{r}'
        sleep(1)
        click_fora.click()
        sleep(1)
        #   === GERENCIAMENTO === NA COMPRA
        # 1 - 50/50

        # 2 - Soros
        if gr == 2:
            if r == 'VITÓRIA':
                lote = float(preco_resultado)
                nav.find_element(By.XPATH, '//*[@id="amount-counter"]/div[1]/div[1]/vui-input-number/input').send_keys(
                    Keys.BACKSPACE, lote)
            if r == 'PERCA':
                lote = int(ceil(lote * 1.10))
                nav.find_element(By.XPATH, '//*[@id="amount-counter"]/div[1]/div[1]/vui-input-number/input').send_keys(
                    Keys.BACKSPACE, lote)
        # 3 - Mão Fixa com Martingale

        # 4 - Mão Fixa

        # ===================================================================================================================
    # =======================================================================================================================================================================================================
        print(f'---> Resultado: {r}')
        planilha.save('binomo.xlsx')

    elif close.loc[v] < lower.loc[v]:# and close.loc[v-1] > lower.loc[v-1]:
        call.click()
        cont += 1
        book[f'A{cont + 1}'] = 'Entrada de COMPRA'
        book[f'B{cont + 1}'] = hora
        book[f'C{cont + 1}'] = 'Preço:'
        book[f'D{cont + 1}'] = close.loc[v]
        book[f'E{cont + 1}'] = 'Banda Inferior:'
        book[f'F{cont + 1}'] = lower.loc[v]
        print(f'Entrada de COMPRA // {hora} // Preço: {close.loc[v]} // Banda Inferior: {lower.loc[v]}')
        sleep(3)
        historico.click()
        sleep(3)
        minuto = int(nav.find_element(By.XPATH,'//*[@id="qa_trading_openDeal"]/vui-timer/vui-label/div/div[2]/div/span[3]').text)
        segundo = int(nav.find_element(By.XPATH,'//*[@id="qa_trading_openDeal"]/vui-timer/vui-label/div/div[2]/div/span[5]').text)
        espera = (minuto * 60) + (segundo) + 5
        sleep(2)
        print(f'{minuto}:{segundo}  // Tempo de espera em Segundos: {(minuto * 60) + segundo}')
        sleep(espera)
        preco_entrada = nav.find_element(By.XPATH,'//*[@id="qa_trading_tradeHistoryStandardTab"]/option-item[1]/div/div[2]/div[2]/p[2]').text.strip().replace('R$', '').replace(' ', '').replace(',', '.')
        if '₮' in preco_entrada:
            preco_entrada = preco_entrada.replace('₮','')
        preco_entrada = float(preco_entrada.strip())
        preco_resultado = nav.find_element(By.XPATH,'//*[@id="qa_trading_tradeHistoryStandardTab"]/option-item[1]/div/div[2]/div[2]/p[1]').text.strip().replace('R$', '').replace(' ', '').replace(',', '.')
        if '₮' in preco_resultado:
            preco_resultado = preco_resultado.replace('₮','')
        preco_resultado = float(preco_resultado.strip())
        if preco_resultado == 0:
            r = 'PERCA'
        elif preco_resultado > preco_entrada:
            r = 'VITÓRIA'
        elif preco_resultado == preco_entrada:
            r = 'EMPATE'
        book[f'F{cont + 1}'] = f'{r}'
        sleep(1)
        click_fora.click()
        sleep(1)
        # ===================================================================================================================
        #   === GERENCIAMENTO === NA VENDA
        # 1 - 50/50

        # 2 - Soros
        """if gr == 2:
            if r == 'VITÓRIA':
                lote = float(preco_resultado)
                nav.find_element(By.XPATH, '//*[@id="amount-counter"]/div[1]/div[1]/vui-input-number/input').send_keys(
                    Keys.BACKSPACE, lote)
            if r == 'PERCA':
                lote = ceil(lote * 1.10)
                nav.find_element(By.XPATH, '//*[@id="amount-counter"]/div[1]/div[1]/vui-input-number/input').send_keys(Keys.BACKSPACE, lote)"""
        # 3 - Mão Fixa com Martingale

        # 4 - Mão Fixa

        # ===================================================================================================================
    # =======================================================================================================================================================================================================
        print(f'---> Resultado: {r}')
        planilha.save('binomo.xlsx')

    else:
        sleep(1)
        print('PROCURANDO ENTRADA...',hora)
        os.system('cls')

    # ===================================================================================================================
