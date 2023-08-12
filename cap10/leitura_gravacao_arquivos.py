""" Leitura de dados em arquivo de texto """

print('Abrindo um arquivo para leitura:')
arquivo = open('contatos.txt', 'r')
conteudo = arquivo.read()
print(f'O conteudo de contatos.txt e: \n{conteudo}')
print('Fechando o arquivo.')
arquivo.close()

print('Criando um novo arquivo:')
arquivo = open('contatos1.txt', 'w')
linha = 'Harriet, 3555-0001\n'
arquivo.write(linha)
print('Abrindo novamente contatos1.txt para conferir as informaçoes. Agora, so para leitura:')
arquivo = open('contatos1.txt', 'r')
conteudo = arquivo.read()
print(f'O conteudo de contatos1.txt e: \n{conteudo}')
print('Fechando o arquivo.')
arquivo.close()

print('Substituindo o conteudo de contatos1.txt:')
arquivo = open('contatos1.txt', 'w')
linha = 'Harriet, 3555-1000\n'
arquivo.write(linha)
print('Abrindo novamente contatos1.txt para conferir as informaçoes. Agora, so para leitura:')
arquivo = open('contatos1.txt', 'r')
conteudo = arquivo.read()
print(f'O conteudo de contatos1.txt e: \n{conteudo}')
print(f'O telefone de Harriet mudou de 3555-0001 para 3555-1000')
print('Fechando o arquivo.')
arquivo.close()

print('Adicionando um novo contato ao arquivo contatos1.txt:')
arquivo = open('contatos1.txt', 'a')
linha = 'Ivan, 3555-1221\n'
arquivo.write(linha)
print('Abrindo novamente contatos1.txt para conferir as informaçoes. Agora, so para leitura:')
arquivo = open('contatos1.txt', 'r')
conteudo = arquivo.read()
print(f'O conteudo de contatos1.txt e: \n{conteudo}')
arquivo.close()

print('Atualizando o conteudo de contatos1.txt:')
arquivo = open('contatos1.txt', 'r+')
linha = 'Harriet, 3555-1001\n'
arquivo.write(linha)
linha = 'Ivan, 3555-1223\n'
arquivo.write(linha)
arquivo.seek(0)
conteudo = arquivo.read()
print(f'O conteudo de contatos1.txt e: \n{conteudo}')
arquivo.close()

print('Adicionando informaçoes a contatos1.txt, no final do arquivo:')
arquivo = open('contatos1.txt', 'a+')
linha = 'Janet, 3555-1002\n'
arquivo.write(linha)
linha = 'Karla, 3555-1003\n'
arquivo.write(linha)
arquivo.seek(0)
conteudo = arquivo.read()
print(f'O conteudo de contatos1.txt e: \n{conteudo}')
arquivo.close()

print('Mudando todo o conteudo de contatos1.txt:')
arquivo = open('contatos1.txt', 'w+')
linha = 'Lucy, 3555-1004\n'
arquivo.write(linha)
linha = 'Mary, 3555-1005\n'
arquivo.write(linha)
arquivo.seek(0)
conteudo = arquivo.read()
print(f'O conteudo de contatos1.txt e: \n{conteudo}')
arquivo.close()

