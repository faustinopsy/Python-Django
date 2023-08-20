from flask import Flask, render_template, request, jsonify, redirect, url_for

import resposta as resp
import treine as tre
import historico as hist

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("escolha.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/train")
def train():
    return render_template("train.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form.get("message")
    hist.registrar_historico(message)
    response = resp.buscar_resposta(message)
    return jsonify({"message": response})

@app.route("/train_bot", methods=["POST"])
def train_bot():
    pergunta = request.form.get("pergunta")
    resposta = request.form.get("resposta")
    tre.salvar_pergunta_resposta(pergunta, resposta)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
