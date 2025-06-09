from flask import Flask, redirect, request, render_template
import random

app = Flask(__name__)

def determinar_resultado(jugador, bot):
    if jugador == bot:
        return "Empate"
    elif (jugador == "piedra" and bot == "tijeras") or \
         (jugador == "papel" and bot == "piedra") or \
         (jugador == "tijeras" and bot == "papel"):
        return "Ganaste!"
    else:
        return "Perdiste"
@app.route("/")
def redirigir_al_juego():
    return redirect("/jugar")
    
@app.route("/jugar", methods=["GET", "POST"])
def jugar():
    resultado = jugador = bot = None
    opciones = ["piedra", "papel", "tijeras"]

    if request.method == "POST":
        jugador = request.form["choice"]
        bot = random.choice(opciones)
        resultado = determinar_resultado(jugador, bot)

    return render_template("index.html", resultado=resultado, jugador=jugador, bot=bot)

if __name__ == "__main__":
    app.run()
