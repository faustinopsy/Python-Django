""" Exemplo de uso do polimorfismo em Python com um erro proposital """
from datetime import datetime
from documento import Documento
from oficio_circular2 import OficioCircular
from comunicacao_interna import CI

doc1 = OficioCircular(numero='0001/2019',
                      data_criacao=datetime(2019,6,1),
                      resumo='Teste de criaçao de oficio circular',
                      texto='Lorem ipsum dolor sit...',
                      data_limite=datetime(2019,6,30),
                      destinatarios= ['cicrana@teste.com', 'fulano@teste.com'])

doc2 = CI(numero='0058/2019',
          texto='Lorem ipsum dolor sit...',
          resumo = 'Teste teste',
          destinatarios=['cicrana@teste.com', 'fulano@teste.com'])

lista_documentos = []
lista_documentos.append(doc1)
lista_documentos.append(doc2)
print('\nImprimindo a lista de documentos atual:\n')
for documento in lista_documentos:
    print(documento)
    print(f'Data limite para envio: {documento.data_limite}')
