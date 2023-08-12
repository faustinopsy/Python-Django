print('Cálculo de Volume')
comprimento = float(input('Entre com o comprimento em metros da caixa d\'água: '))
largura = float(input('Entre com a largura em metros da caixa d\'água: '))
profundidade = float(input('Entre com a largura em metros da caixa d\'água: '))
volume_em_m3 = comprimento * largura * profundidade
volume_em_litros = volume_em_m3 * 1000
print('A caixa d\'agua comporta %.2f litros.' % volume_em_litros)
