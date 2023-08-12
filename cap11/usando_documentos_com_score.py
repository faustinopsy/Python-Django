""" Exemplo de uso das classses CI e OficioCircular com o conceito de score """
from datetime import datetime
from documento_com_score import OficioCircular, CI

print('Criando uma CI...')
doc1 = CI(numero='0058/2019',
          texto='Lorem ipsum dolor sit...',
	  resumo = 'Teste teste',
          destinatarios=['cicrana@teste.com', 'fulano@teste.com'])
print(doc1)
print('Criando um ofício circular...')
doc2 = OficioCircular(numero='0001/2019',
                      data_criacao=datetime(2019,6,1),
                      resumo='Teste de criaçao de oficio circular',
                      texto='Lorem ipsum dolor sit...',
                      data_limite=datetime(2019,6,30),
                      destinatarios= ['cicrana@teste.com', 'fulano@teste.com'])
print(f'O score da CI é {doc1.score}')
print(f'O score do ofício circular é {doc2.score}')
