from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Criando o app(site)
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar msg
@socketio.on("message")
def gerenciar_mensgem(mensagem):
    send(mensagem, broadcast=True)

# cria a nossa 1ª pagina = 1ª rota
@app.route("/")
def homepage():
    return render_template("index.html")

# rota o nosso aplicativo

socketio.run(app, host="192.168.10.13")

# websocket