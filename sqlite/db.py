import sqlite3

class DataBase:
    """ Class that represent the application database """

    def __init__(self, dbname='database.dat'):
        self._dbname = dbname
        self._conn = None

    def conn(self):
        self._conn = sqlite3.connect(self._dbname)

    def close(self):
        try:
            self._conn.close()
        except AttributeError:
             raise Exception("No connection exists.")

    def _get_cursor(self):
        _cursor = None

        try:
            _cursor = self._conn.cursor()
        except AttributeError:
            raise Exception("Need a database connection...")

        return _cursor

    def drop_table(self, name):
        str_drop = """ DROP TABLE {} """

        cursor = self._get_cursor()

        cursor.execute(str_drop.format(name))

        self._conn.commit()

    def create_table(self, name):
        str_create_tb = """
                     CREATE TABLE IF NOT EXISTS {}(
                           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                           nome TEXT NOT NULL,
                           senha VARCHAR(20) NOT NULL,
                           cpf VARCHAR(11) UNIQUE NOT NULL,
                           email TEXT NOT NULL
                    );
              """.format(name)

        cursor = self._get_cursor()

        try:
            cursor.execute(str_create_tb)
        except AttributeError:
            raise Exception("Need a database connection first.")

    def insert_client(self, table_name, **kwargs):
        str_insert = """
                        INSERT INTO {} (nome, senha, cpf, email) VALUES (?, ?, ?, ?)
                     """.format(table_name)

        cursor = self._get_cursor()

        try:
            cursor.execute(str_insert, (kwargs['nome'], kwargs['senha'], kwargs['cpf'], kwargs['email']))
            self._conn.commit()
        except sqlite3.IntegrityError:
           print("CPF {} already exists in database".format(kwargs['cpf']))


    def search_client_by_cpf(self, cpf):
        str_search = """
                     SELECT * FROM clientes where cpf={};
                     """
        client = None

        cursor = self._get_cursor()

        cursor.execute(str_search.format(cpf))
        client = cursor.fetchone()

        return client

    def remove_client(self, cpf):
        str_delete = """
                     DELETE FROM clientes where id={};
                     """
        c = self.search_client_by_cpf(cpf)

        if c:
            client_id = c[0]
            cursor = self._get_cursor()

            try:
                cursor.execute(str_delete.format(client_id))
                self._conn.commit()
            except Exception as ex:
                print(ex)
        else:
            print("Client Not found!!!")

    def search_client_by_email(self, email):
        str_search = """
                     SELECT * FROM clientes where email='{}';
                     """
        cursor = self._get_cursor()
        found = False

        cursor.execute(str_search.format(email))
        client = cursor.fetchone()

        if client:
            found = True

        return found

    def login(self, username, password):
        logged = False
        cursor = self._get_cursor()
        sql = 'SELECT * FROM clientes WHERE cpf=? AND senha=?'

        client = cursor.execute(sql, [username, password]).fetchone()
        if client:
            logged = True

        return logged
