from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>Videogamer page</h1>
    <a href="/random_fact">¡Ver un hecho al azar!</a>
    """

@app.route("/random_fact")
def random_fact():
    facts_list = [
        "Los delfines tienen nombres específicos entre ellos.",
        "El corazón de un camarón está en su cabeza.",
        "La miel nunca se echa a perder.",
        "Los plátanos son bayas, pero las fresas no.",
        "Una nube promedio pesa alrededor de 1.1 millones de libras."
    ]
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)