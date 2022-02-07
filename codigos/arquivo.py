import mysql.connector
from pip import main
from functions import *


banco = mysql.connector.connect(host='localhost', user='root', password='', database='cadastro')
cursor = banco.cursor()


if __name__ == '__main__':
    update()
    mostrar_tabela()