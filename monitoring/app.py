from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Configuration de la base de données
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("POSTGRES_DB", "northwind")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")

def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print("Erreur de connexion à la base de données :", e)
        return None

@app.route("/")
def home():
    return jsonify({"message": "Application Flask en cours d'exécution"})

@app.route("/products")
def products():
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM products;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    else:
        return jsonify({"error": "Impossible de se connecter à la base de données"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
