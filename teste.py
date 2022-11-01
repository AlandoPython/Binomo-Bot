import talib as tb
from datetime import datetime
hj = datetime.now()
import MetaTrader5 as mt5
# ==========================================================================================
import pandas as pd

pd.set_option('display.max_columns', 500)  # número de colunas
pd.set_option('display.width', 1500)  # largura máxima da tabela
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
# ==========================================================================================
#   DATAFRAME
ativos = ['EURUSD','USDJPY']
entrada = win = loss = empate = c = 0
#   METATRADER
mt5.initialize()
for a in range(0,len(ativos)):
    rates = mt5.copy_rates_from(f'{ativos[a]}',mt5.TIMEFRAME_M1, datetime(hj.year, hj.month, hj.day, hour, hj.minute, hj.second), 10000)
    rates_frame = pd.DataFrame(rates)
    #   DADOS VELA
    close = rates_frame['close']
    open = rates_frame['open']
    high = rates_frame['high']
    low = rates_frame['low']
    #   INDICADORES
    upper, mid, lower = tb.BBANDS(close, timeperiod=9, nbdevup=2.5, nbdevdn=2.5, matype=0)
    # ==========================================================================================
    # MHI QUEBRA CICLO
    # ==========================================================================================
    """# BANDS
    for c in range(1,len(rates_frame)):
        if high[c-1] >= upper[c-1] and close[c-1] < upper[c-1]:
            entrada += 1
            if close[c] < close[c-1]:
                win += 1
            elif close[c] == close[c-1]:
                empate += 1
            else:
                loss += 1
        elif low[c-1] <= lower[c-1] and close[c-1] > lower[c-1]:
            entrada += 1
            if close[c] > close[c-1]:
                win += 1
            elif close[c] == close[c-1]:
                empate += 1
            else:
                loss += 1

    #   PRINT DOS RESULTADOS
    text = f'{ativos[a]}'
    print('='*30)
    print(f'{text} .:^30')
    print('=' * 30)
    print()
    print(f'Total de Entradas: {entrada}')
    print(f'Vitórias: {win}')
    print(f'Empates: {empate}')
    print(f'Derrotas: {loss}')
    print('-'*30)
    print()"""

    #================================================================================================================



