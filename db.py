from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def conectar():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database="os.getenv('DB_NAME')"
        )
        return conexao

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar: {erro}")
        return None
