# importa o sqlite3
import sqlite3
# conecta ao banco de dados
conn = sqlite3.connect('deputados.db')
# define o cursor
cursor = conn.cursor()

# cria a tabela (schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS deputados (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nome_ficticio TEXT NOT NULL,
    partido TEXT NOT NULL,
    estado VARCHAR(2) NOT NULL,
    link TEXT NOT NULL,
    ano_entrada VARCHAR(4) NOT NULL,
    ano_saida VARCHAR(4) NOT NULL
);
""")

print('Tabela criada com sucesso.')

# desconecta do banco de dados
conn.close()

# comandos para rodar no terminal
# python3 connect_db.py
# sqlite3 deputados.db '.tables' -> ve qual tabela foi criada
# sqlite3 deputados.db 'PRAGMA table_info(deputados)' -> visualiza os campos da tabela 'deputados'