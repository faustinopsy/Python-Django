from datetime import datetime

str_nascimento = input("Digite sua data de nascimento no formato dd/mm/yyyy: ")
data_nasc = datetime.strptime(str_nascimento, "%d/%m/%Y")
idade = datetime.now() - data_nasc
print(f'Você viveu {idade.days} dias ate hoje.')
