# app.py
from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)

# Rota para renderizar a página index.html
@app.route('/')
def index():
    return render_template('index.html')

# Rota para executar a query e retornar os resultados em formato JSON
@app.route('/search')
def search():
    # Conectar ao banco de dados
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Xpto1313!",
        database="winter19"
    )

    # Executar a query
    query = """
        SELECT Cr.name_pair AS Crypto, Co.Price_usd AS Price, Co.Date_cotation AS USD
        FROM Crypto Cr, Cotation Co
        WHERE Cr.cd_crypto = Co.Cd_Crypto
        ORDER BY Co.Date_cotation DESC
    """
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    # Fechar a conexão com o banco de dados
    cursor.close()
    connection.close()

    # Formatar os resultados em formato JSON e retorná-los
    formatted_results = [{'Crypto': row[0], 'Price': row[1], 'USD': row[2]} for row in results]
    return jsonify(formatted_results)

if __name__ == '__main__':
    app.run(debug=True)
