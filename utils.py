from models import Usuarios,Rodada
from datetime import datetime, timedelta
from datetime import datetime, timezone, timedelta
from random import randint

# Insere dados na tabela pessoa
'''
def insere_pessoas():
    pessoa = Jogador(nome='Renan',valor=1)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Jogador.query.all()
    print(pessoas)
    pessoa = Jogador.query.filter_by(nome='Renan').first()
    print(pessoa.valor)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Jogador.query.filter_by(nome='Renan').first()
    pessoa.nome = 'Lucas'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Jogador.query.filter_by(nome='Lucas').first()
    pessoa.delete()

'''


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

def insere_rodada(rodada,primeiraMilhar, segundaMilhar,terceiraMilhar,quartaMilhar,quintaMilhar,data):
    rodada = Rodada(rodada=rodada,primeiraMilhar=primeiraMilhar, segundaMilhar=segundaMilhar,terceiraMilhar=terceiraMilhar,
                    quartaMilhar=quartaMilhar,quintaMilhar=quintaMilhar,data=data)
    rodada.save()


if __name__ == '__main__':
    data_e_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fuso_horario = timezone(diferenca)
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")
    print(data_e_hora_sao_paulo_em_texto)

    primeiro_lugar = randint(1, 9999)
    segundo_lugar = randint(1, 9999)
    terceiro_lugar = randint(1, 9999)
    quarto_lugar = randint(1, 9999)
    quinto_lugar = randint(1, 9999)

    insere_rodada(1,primeiro_lugar,segundo_lugar,terceiro_lugar,quarto_lugar,quinto_lugar,"10/11/2020 19:18")

    consulta_todos_usuarios()

    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()





