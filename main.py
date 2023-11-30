import PySimpleGUI as psg

import conver
from conver import fah
from conver import cel

layout = [
    [psg.Text('Qual a temperatura em Graus?'), psg.InputText(key='Num1')],
    [psg.Radio('Celsius', 'Radio1', default=True),
    psg.Radio('Fahrenheit', 'Radio2')],
    [psg.Text('->'), psg.Text('', key = 'resultado'), psg.Text('Resultado')],
    [psg.Button('Calcular')],
    [psg.Button('Limpar')],
]

janela = psg.Window('Conversor de temperatura', layout)

while True:
    evento, botao, temp = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['Num1'].update('')
        janela['resultado'].update('')
    elif botao[1]:
        num1 = int(temp['Num1'])
        janela['resultado'].update(conver.cel(num1))
    elif botao[2]:
        num1 = int(temp['Num1'])
        janela['resultado'].update(conver.fah(num1))
janela.close()



