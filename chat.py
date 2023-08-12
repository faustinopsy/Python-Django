import resposta as resp
import treine as tre
import historico as hist

while True:
    sair='s'
    questao=str(input("Treinar ou conversar? "))
    if questao.lower()=='treinar':
        while sair.lower()!='sair':
            pergunta=str(input("Digite a Pergunta: "))
            resposta=str(input("Digite a Resposta: "))
            tre.salvar_pergunta_resposta(pergunta, resposta)
            sair=str(input("Enter, ou digite, sair "))
    elif questao.lower()=='conversar':
        while sair.lower()!='sair':
            pergunta=str(input("Pergunte, ou digite sair: "))
            if pergunta.lower()=='sair':
                sair=pergunta
            else:
                hist.registrar_historico(pergunta)
                print(resp.buscar_resposta(pergunta))
