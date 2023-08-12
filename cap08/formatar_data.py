import datetime
hoje = datetime.date.today()
print('Hoje é dia: ', hoje)
print('Hum... que data estranha. Vamos melhorar sua apresentação!')
print('Hoje é dia: ', hoje.strftime('%d/%m/%Y'))
