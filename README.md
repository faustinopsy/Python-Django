# Chatbot com Treinamento

Este é um projeto de chatbot desenvolvido com Flask que permite aos usuários conversar com um chatbot e treiná-lo com novas perguntas e respostas.

## Como funciona

O chatbot lê um arquivo de texto que contém pares de perguntas e respostas e usa essas informações para responder às perguntas dos usuários. Os usuários também podem treinar o chatbot adicionando novas perguntas e respostas ao arquivo de texto.

## Configuração

1. Clone o repositório:
  - git clone [Python-Flask](https://github.com/faustinopsy/Python-Flask)
2. Instale as dependências necessárias:
  -  pip install Flask
3. Inicie o aplicativo Flask: (ainda que o nome do diretorio é django foi utilizado o flask por ser minimalista para o proposito do projeto)
  -  python app.py
4. Abra um navegador e vá para [http://localhost:5000](http://localhost:5000) para acessar a interface do chatbot.

## Uso

- Na tela inicial, você pode escolher entre treinar o chatbot ou conversar com ele.
- Se você escolher treinar o chatbot, será solicitada uma senha secreta. A senha correta é `#1Dia_Aluno#1Dia_Professor`. Uma vez que a senha correta seja inserida, você será levado para a tela de treinamento, onde pode adicionar novas perguntas e respostas ao chatbot.
- Se você escolher conversar com o chatbot, será levado para a tela de chat, onde pode enviar mensagens ao chatbot e receber respostas.

## Arquivos

- `app.py`: É o arquivo principal que contém o aplicativo Flask e define todas as rotas e lógica do aplicativo.
- `resposta.py`: Este arquivo contém a função que o chatbot usa para buscar respostas para as perguntas dos usuários.
- `treine.py`: Este arquivo contém a função que permite aos usuários treinar o chatbot com novas perguntas e respostas.
Demostração de uso em: https://chatbot-ultron-bba8f1e43a07.herokuapp.com/
## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT.
