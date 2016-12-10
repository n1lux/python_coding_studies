from db import DataBase


if __name__ == "__main__":
    db = DataBase()
    db.conn()
    #db.drop_table(name='clientes')
    #db.create_table(name='clientes')
    #clients = ({'nome': 'Nilo', 'senha':'123mudar', 'cpf': '11111111111', 'email': 'nilo@teste.com'},
    #           {'nome': 'Marcos', 'senha':'123mudar', 'cpf': '22222222222', 'email': 'marcos@teste.com'},
    #)
    #for c in clients:
    #    db.insert_client(table_name='clientes', **c)
    #c = db.search_client_by_cpf('11111111111')
    #print(c)
    #c = db.search_client_by_email('nilo@teste.com')
    #print(c)
    print(db.login(username='22222222222', password='123mudar'))
    #db.remove_client(cpf='22222222222')
    db.close()
