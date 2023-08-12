import difflib
def buscar_resposta(pergunta):
    arquivo='chatbot.txt'
    perguntas_respostas = {}

    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                p, r = linha.strip().split("=", 1)
                perguntas_respostas[p] = r

        if pergunta not in perguntas_respostas:
            matches = difflib.get_close_matches(pergunta, perguntas_respostas.keys(), n=1)
            if matches:
                return f"Você quis dizer '{matches[0]}'? {perguntas_respostas[matches[0]]}"
            else:
                return 'Não entendi sua questão'
        else:
            return perguntas_respostas[pergunta]

    except FileNotFoundError:
        return 'Não entendi sua questão'



# import difflib
# def buscar_resposta(pergunta):
#     arquivo='chatbot.txt'
#     with open(arquivo, 'r', encoding='utf-8') as f:
#         perguntas_respostas = {}
#         try:
#             with open(arquivo, 'r', encoding='utf-8') as f:
#                 for linha in f:
#                     p, r = linha.strip().split("=", 1) 
#                     perguntas_respostas[p] = r
#         except FileNotFoundError:
#             pass
#         return perguntas_respostas.get(pergunta, 'Não entendi sua questão')

