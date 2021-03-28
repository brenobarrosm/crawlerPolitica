import sqlite3

conn = sqlite3.connect('deputados.db')
cursor = conn.cursor()

# inserindo dados na tabela
pessoa = "Jubilou"
nome_fict = "Tantaram"
part = "NAO TEM"
stat = "MS"
url = "http://www.com.br"
entrou = "2019"
saiu = "2023"
class insertData():
	increment = 0
	# constructor
	def __init__(self, nome, nome_ficticio, partido, estado, link, ano_entrada, ano_saida):
		self.conn = sqlite3.connect('deputados.db')
		self.cursor = self.conn.cursor()
		self.nome = nome
		self.nome_ficticio = nome_ficticio
		self.partido = partido
		self.estado = estado
		self.link = link
		self.ano_entrada = ano_entrada
		self.ano_saida = ano_saida
	# salva no banco e 'printa' comentario
	def save(self):
		self.__class__.increment += 1
		self.id = self.__class__.increment
		self.cursor.execute("""
		INSERT INTO deputados (nome, nome_ficticio, partido, estado, link, ano_entrada, ano_saida)
		VALUES(?,?,?,?,?,?,?)
		""", (self.nome, self.nome_ficticio, self.partido, self.estado, self.link, self.ano_entrada, self.ano_saida))
		self.conn.commit()
		print('Inserido com sucesso')
		self.conn.close()

inserir = insertData(pessoa, nome_fict, part, stat, url, entrou, saiu)
inserir.save()

# gravar no bd
conn.commit()

print('Dados inseridos com sucesso')

conn.close()