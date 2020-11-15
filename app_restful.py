

import json
from models import Evento,Usuarios
from flask import Flask, request
from flask_restful import Resource, Api
from models import Usuarios,Dinheiro,Rodada
from flask_httpauth import HTTPBasicAuth
from datetime import datetime, timedelta, date
from datetime import datetime, timezone, timedelta
from random import randint
auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)
import os




@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Eventos(Resource):
    @auth.login_required
    def get(self, id):
        evento = Evento.query.filter_by(id=id).first()
        try:
            response = {
                'nome': evento.nome,
                'rodada': evento.rodada,
                'milhar': evento.milhar,
                'conferir': evento.conferir,
                'valor': evento.valor
            }

        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada'
            }
        return response







class VerDinheiro(Resource):
    @auth.login_required
    def get(self):
        a = auth.get_auth()

        print(a)
        b = a['username']
        print(b)
        dinheiro = Dinheiro.query.all()
        vetor = []
        contador = 0
        print("olá presta atenção")

        for i in dinheiro:

            print(i.nome)
            print(b)

            if str(i.nome) == str(b):
                contador = 1


                response = {'dinheiro': i.dinheiro}
                vetor.append(response)
        if contador == 1:
            response = vetor
        else:
            response = [{"Erro"}]
        return response

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        print("aqui")
        print(Dinheiro.query.all())

        print(auth.get_auth())
        a = auth.get_auth()
        b = a['username']
        print(Dinheiro.query.all())

        print(b)
        eventos = Evento.query.all()
        vetor = []
        contador = 0

        for i in eventos:

            print(i.nome)
            print(b)

            if str(i.nome) == str(b):
                contador = 1


                response = { 'Milhar': i.milhar,'Dinheiro gasto':i.valor,'Rodada':i.rodada}
                vetor.append(response)
        if contador == 1:
            response = vetor
        else:
            response = [{"Erro"}]
        return response

    def post(self):
        print("eu cai aqui")

        dados = request.json
        a = auth.get_auth()

        print(a)
        b = a['username']
        print(b)
        print(a)
        b = a['username']
        print(b)
        dinheiro = Dinheiro.query.all()
        print("eu cai aqui")

        for variavel2 in dinheiro:
            print("eu cai aqui")

            if str(variavel2.nome) == str(b):
                print("eu cai aqui")
                variavel2.dinheiro = int(variavel2.dinheiro) - int(dados['valor'])
                variavel2.save()
                print(variavel2.dinheiro)

        rodadas = Rodada.query.all()
        rodada = 0
        for variavel1 in rodadas:
            if rodada < variavel1.rodada:
                rodada = int(variavel1.rodada)

        print(rodada)


        evento = Evento(nome=b, milhar=dados['milhar'], rodada=rodada,
                        valor=dados['valor'],
                        conferir=0)
        evento.save()
        response = {
                    'id': evento.id,
                    'nome': evento.nome,
                    'milhar': evento.milhar,
                    'rodada': evento.rodada,
                    'valor':evento.valor,
                    'conferir': evento.conferir

                }

        return response

class Registro(Resource):
    @auth.login_required
    def get(self):

        a = auth.get_auth()
        b = a['username']
        c = a['password']
        usuarios = consulta_todos_usuarios()
        d = "d"
        for variavel in usuarios:

            if str(b) == variavel.login:
                if str(c) == variavel.senha:
                    return d





    def post(self):
        dados = request.json
        usuarios = consulta_todos_usuarios()

        for variavel in usuarios:

            if str(dados['nome']) == variavel.login:
                if str(dados['senha']) == variavel.senha:
                    return "Ok"
        try:
            insere_usuario(dados['nome'], dados['senha'])
            insere_dinheiro(dados['nome'])
            return "Registrado"
        except:
            return "Senha errada"




class Resultado(Resource):
    @auth.login_required
    def get(self):
        rodada_lista = Rodada.query.all()
        rodada = 0
        data_dia1 = ""
        data_mes1 = ""
        data_ano1 = ""
        data_dia2 = ""
        data_mes2 = ""
        data_ano2 = ""

        contador = 0
        data_agora = data_atual()
        for variavel in rodada_lista:
            print(variavel.rodada)
            if int(rodada) < int(variavel.rodada):
                rodada = int(variavel.rodada)
            data_sistema = variavel.data
        for variavel1 in data_sistema:
            contador = contador + 1
            # data
            if contador == 1:
                data_dia1 = data_dia1 + variavel1
            if contador == 2:
                data_dia1 = data_dia1 + variavel1
            # mes
            if contador == 4:
                data_mes1 = data_mes1 + variavel1
            if contador == 5:
                data_mes1 = data_mes1 + variavel1

            if contador == 7:
                data_ano1 = data_ano1 + variavel1
            if contador == 8:
                data_ano1 = data_ano1 + variavel1
            if contador == 9:
                data_ano1 = data_ano1 + variavel1
            if contador == 10:
                data_ano1 = data_ano1 + variavel1
        contador = 0
        for variavel_in_data_e_hora_atual in data_agora:
            contador = contador + 1
            # data
            if contador == 1:
                data_dia2 = data_dia2 + variavel_in_data_e_hora_atual
            if contador == 2:
                data_dia2 = data_dia2 + variavel_in_data_e_hora_atual
            # mes
            if contador == 4:
                data_mes2 = data_mes2 + variavel_in_data_e_hora_atual
            if contador == 5:
                data_mes2 = data_mes2 + variavel_in_data_e_hora_atual

            if contador == 7:
                data_ano2 = data_ano2 + variavel_in_data_e_hora_atual
            if contador == 8:
                data_ano2 = data_ano2 + variavel_in_data_e_hora_atual
            if contador == 9:
                data_ano2 = data_ano2 + variavel_in_data_e_hora_atual
            if contador == 10:
                data_ano2 = data_ano2 + variavel_in_data_e_hora_atual
        data1 = str(data_ano1) + "-" + str(data_mes1) + "-" + str(data_dia1)
        data2 = str(data_ano2) + "-" + str(data_mes2) + "-" + str(data_dia2)
        print(data1)
        print(data2)
        d1 = datetime.strptime(data1, '%Y-%m-%d')
        d2 = datetime.strptime(data2, '%Y-%m-%d')
        quantidade_dias = abs((d2 - d1).days)
        print("quantida de dias" + str(quantidade_dias))
        d = date(int(data_ano1), int(data_mes1), int(data_dia1))
        if quantidade_dias > 0:
            sopranaoidentar = 0
            contar = 0
            for quantidade_dias_variavel in range(quantidade_dias):
                contar = contar + 1
                if sopranaoidentar == 0:

                    a = 3600 * 12

                    primeiro_lugar = randint(1, 9999)
                    segundo_lugar = randint(1, 9999)
                    terceiro_lugar = randint(1, 9999)
                    quarto_lugar = randint(1, 9999)
                    quinto_lugar = randint(1, 9999)


                    data_que_vai = d + timedelta(days=int(contar))
                    print(data_que_vai)

                    data_que_vai = data_que_vai.strftime("%d/%m/%Y")
                    rodada = rodada + 1
                    insere_rodada(rodada, primeiro_lugar, segundo_lugar, terceiro_lugar, quarto_lugar, quinto_lugar,
                                  data_que_vai)


            print("data e ano")
            print(data_ano1)
            print(data_dia1)
            print(data_mes1)
            print(data_ano2)
            print(data_dia2)
            print(data_mes2)

            contador = contador + 1









        rodada_lista = Rodada.query.all()

        response = [{'rodada': i.rodada, 'Primeira Milhar': i.primeiraMilhar,
                     'Segunda Milhar': i.segundaMilhar,'Terceira Milhar':i.terceiraMilhar,
                     'Quarta Milhar':i.quartaMilhar,'Quinta Milhar':i.quintaMilhar,
                     'data':i.data}for i in rodada_lista]


        return response




class Conferir(Resource):
    @auth.login_required
    def get(self):

        a = auth.get_auth()
        b = a['username']
        dinheiro_todos = Dinheiro.query.all()
        for variavel2 in dinheiro_todos:
            print("eu cai aqui")

            if str(variavel2.nome) == str(b):
                print("eu cai aqui")
                dinheiro_alterar = variavel2





        eventos = Evento.query.all()

        vetor = []
        contador = 0

        for i in eventos:

            print(i.nome)
            print(b)

            if str(i.nome) == str(b):
                if str(i.conferir) == str(0):
                    contador = 1

                    response = {'id': i.id, 'nome': i.nome, 'rodada': i.rodada, 'milhar': i.milhar, 'conferir': i.conferir,'valor':i.valor}
                    milhar = i.milhar
                    rodada = i.rodada
                    valor = i.valor
                    vetor.append(rodada)
                    vetor.append(valor)

                    vetor.append(milhar)
                    i.conferir = 1
                    i.save()

        if contador == 1:
            response = vetor
        else:
            response = [{"Erro"}]
        print(vetor)
        print(vetor[0])
        rodadas = Rodada.query.all()
        contador = 3
        for variavel in vetor:
            contador = contador + 1
            resto = contador % 3

            if resto == 1:
                rodada_para_comparar  = int(variavel)
            if resto == 2:
                valor  = int(variavel)
            if resto == 0:
                for variavel2 in rodadas:
                    if str(variavel2.rodada) == str(rodada_para_comparar):
                        if str(variavel2.primeiraMilhar) == str(variavel):
                            dinheiro_alterar.dinheiro = int(dinheiro_alterar.dinheiro) + valor*9000
                            dinheiro_alterar.save()

                        if str(variavel2.segundaMilhar) == str(variavel):
                            dinheiro_alterar.dinheiro = int(dinheiro_alterar.dinheiro) + valor*9000
                            dinheiro_alterar.save()
                        if str(variavel2.terceiraMilhar) == str(variavel):
                            dinheiro_alterar.dinheiro = int(dinheiro_alterar.dinheiro) + valor*9000
                            dinheiro_alterar.save()

                        if str(variavel2.quartaMilhar) == str(variavel):
                            dinheiro_alterar.dinheiro = int(dinheiro_alterar.dinheiro) + valor*9000
                            dinheiro_alterar.save()
                        if str(variavel2.quintaMilhar) == str(variavel):
                            dinheiro_alterar.dinheiro = int(dinheiro_alterar.dinheiro) + valor*9000
                            dinheiro_alterar.save()





        return response

api.add_resource(ListaPessoas, '/evento/')
api.add_resource(Registro, '/registro/')
api.add_resource(Resultado, '/resultado/')
api.add_resource(VerDinheiro, '/dinheiro/')
api.add_resource(Conferir, '/conferir/')






def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def insere_dinheiro(login):
    dinheiro = Dinheiro(nome=login, dinheiro=600)
    dinheiro.save()


def consulta_dinheiro():
    a = Dinheiro.query.all()
    print(a)
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)
    return usuarios
def data_atual():
    data_e_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fuso_horario = timezone(diferenca)
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")
    return data_e_hora_sao_paulo_em_texto


def insere_rodada(rodada,primeiraMilhar, segundaMilhar,terceiraMilhar,quartaMilhar,quintaMilhar,data):
    rodada = Rodada(rodada=rodada,primeiraMilhar=primeiraMilhar, segundaMilhar=segundaMilhar,terceiraMilhar=terceiraMilhar,
                    quartaMilhar=quartaMilhar,quintaMilhar=quintaMilhar,data=data)
    rodada.save()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
