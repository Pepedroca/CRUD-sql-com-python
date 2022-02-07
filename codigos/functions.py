import mysql.connector

banco = mysql.connector.connect(host='localhost', user='root', password='', database='cadastro')
cursor = banco.cursor()


def criar_conta(nome=None, email=None, senha=None):
    cursor.execute('use cadastro;')

    nome = input('Nome(primeiro): ')
    senha = input('Senha: ')
    email = input('Email: ')
    dados = (nome,  email, senha)
    cursor.execute("INSERT INTO contas (nome, email, senha) VALUES (%s, %s, %s);", dados)
    banco.commit()


def mostrar_tabela():
    cursor.execute('use cadastro;')
    
    cursor.execute('SELECT * FROM contas;')
    pegar_valores = cursor.fetchall()
    for x in pegar_valores:
        print(30 * '=')
        print(f"""ID: {x[0]} \nNome: {x[1]}""")
        print(30 * '=')



def deletar():
    cursor.execute('USE cadastro;')
    mostrar_tabela()
    id = int(input('Digite o id da pessoa desejada: '))
    comando_sql = f"DELETE FROM contas WHERE id = {id};"
    cursor.execute(comando_sql)
    banco.commit()


def update():
    escolha = input('Alterar (nome, email ou senha): ')
    if escolha == 'email':
        mostrar_tabela()
        id = int(input('ID Da pessoa: '))
        email = (input('Alterar email: '))
        comando_sql = f"UPDATE contas set email = {email} where id = {id};"
        cursor.execute(comando_sql)
        banco.commit()

    if escolha == 'nome':
        mostrar_tabela()
        id = int(input('ID Da pessoa: '))
        nome = (input('Alterar nome: '))
        comando_sql = f"UPDATE contas set nome = '{nome}' where id = {id};"
        cursor.execute(comando_sql)
        banco.commit()

    if escolha == 'senha':
        mostrar_tabela()
        id = int(input('ID Da pessoa: '))
        senha = (input('Alterar senha: '))
        comando_sql = f"UPDATE contas set senha = {senha} where id = {id};"
        cursor.execute(comando_sql)
        banco.commit()