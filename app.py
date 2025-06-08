from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def jugar():
    resultado = jugador = bot = None
    opciones = ["piedra", "papel", "tijeras"]

    if request.method == "POST":
        jugador = request.form["choice"]
        bot = random.choice(opciones)

        if jugador == bot:
            resultado = "Empate"
        elif (jugador == "piedra" and bot == "tijeras") or \
             (jugador == "papel" and bot == "piedra") or \
             (jugador == "tijeras" and bot == "papel"):
            resultado = "Ganaste!"
        else:
            resultado = "Perdiste"

    return render_template("index.html", resultado=resultado, jugador=jugador, bot=bot)

if __name__ == "__main__":
    app.run()
