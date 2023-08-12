import datetime

print('Usando informaçoes temporais...')
dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
agora=datetime.datetime.now()
print(f'Agora são {agora}')
print('Extraindo os componentes do momento atual:')
print(f'Dia: {agora.day}')
print(f'Mes: {agora.month}')
print(f'Ano: {agora.year}')
print(f'Horas: {agora.hour} h')
print(f'Minutos: {agora.minute} min')
print(f'Segundos: {agora.second} s')
dia_semana = datetime.date.weekday(agora)
print(f'Hoje e dia {dias[dia_semana]}, o dia de numero {dia_semana + 2} da semana.')
t1 = datetime.datetime(2019, 5, 6)       # t1 = 06/05/2019
t2 = datetime.datetime(2019, 5, 13)      # t2 = 13/05/2019
print(f'A diferença entre {t2} e {t1} é {t2 - t1}')
print('Se você tentar somar duas variáveis datetime, obterá um erro:')
print(t2 + t1)
