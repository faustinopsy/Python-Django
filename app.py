from flask import Flask, render_template, request, jsonify, redirect, url_for, session

import os

import resposta as resp
import treine as tre
import historico as hist

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dontcrynomore'  

@app.route("/")
def index():
    return render_template("escolha.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/train")
def train():
    if 'password' in session and session['password'] == "#1Dia_Aluno#1Dia_Professor":
        return render_template("train.html")
    else:
        return render_template("login.html")

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

@app.route("/check_password", methods=["POST"])
def check_password():
    password = request.form.get("password")
    secret_password = "#1Dia_Aluno#1Dia_Professor" 
   
    if password == secret_password:
        session['password']=password
        return redirect(url_for("train"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
