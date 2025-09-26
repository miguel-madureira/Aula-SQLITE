#Criar um banco de dados SQLITE e uma tabela
import sqlite3

#Criar a conexão com o banco de dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objetivo chamado de "cursor" que será usado para executar os comandos sql 
cursor = conexao.cursor()