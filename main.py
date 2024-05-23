from flask import Flask, render_template

app = Flask(__name__)

# Criar primeira pagina do site
#route -> shovel.com.br/
#funcao -> o que quer exibir na pagina
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)
# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)


