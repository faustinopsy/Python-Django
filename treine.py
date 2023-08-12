def salvar_pergunta_resposta(pergunta, resposta):
    arquivo='chatbot.txt'
    with open(arquivo, 'a', encoding='utf-8') as f:
        f.write(f"{pergunta}={resposta}\n")