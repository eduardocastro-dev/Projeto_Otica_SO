import sqlite3


class DataBase:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except AttributeError:
            pass

    def create_table_user(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users ( 
                           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           user TEXT UNIQUE NOT NULL,
                           password TEXT NOT NULL,
                           access TEXT NOT NULL
                           ); 
                """
            )
        except AttributeError:
            print("Faça a conexão")

    def insert_user(self, name, user, passaword, access):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                INSERT INTO users (name, user, password, access)
                  VALUES(?,?,?,?)
        """,
                (name, user, passaword, access),
            )
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão")

    def check_user(self, user, passaword):
        try:
            cursor = self.connection.cursor()

            cursor.execute(
                """                       
                SELECT * FROM users;
            """
            )

            for linha in cursor.fetchall():
                if (
                    linha[2].upper() == user.upper()
                    and linha[3] == passaword
                    and linha[4] == "Administrador"
                ):
                    return "administrador"

                elif (
                    linha[2].upper() == user.upper()
                    and linha[3] == passaword
                    and linha[4] == "Usuário"
                ):
                    return "usuário"

                else:
                    continue

            return "Sem acessso"

        except AttributeError:
            print("Faça a conexão")

    def insert_data(self, full_dataset):
        cursor = self.connection.cursor()
        campos_tabela = (
            "NFe",
            "serie",
            "data_emissao",
            "chave",
            "cnpj_emitente",
            "nome_emitente",
            "valorNfe",
            "itemNota",
            "cod",
            "qntd",
            "descricao",
            "unidade_medida",
            "valorProd",
            "data_importacao",
            "usuario",
            "data_saida",
        )

        qntd = ",".join(map(str, "?" * 16))

        query = f""" INSERT INTO Notas {campos_tabela} VALUES ({qntd})"""

        try:
            for nota in full_dataset:
                cursor.execute(query, tuple(nota))
                self.connection.commit()
        except sqlite3.IntegrityError:
            print("Nota já existe no banco")

    def create_table_nfe(self):
        cursor = self.connection.cursor()

        cursor.execute(
            """

            CREATE TABLE IF NOT EXISTS Notas(

            NFe TEXT,
            serie TEXT,
            data_emissao TEXT,
            chave TEXT,
            cnpj_emitente TEXT,
            nome_emitente TEXT,                
            valorNfe TEXT,
            itemNota TEXT,
            cod TEXT,
            qntd TEXT,
            descricao TEXT,
            unidade_medida TEXT,
            valorProd TEXT,
            data_importacao TEXT,
            usuario TEXT,
            data_saida TEXT,


        
        PRIMARY KEY(Chave, Nfe, itemNota)                

            );

        """
        )

    def update_estoque(self, data_saida, usuario, notas):
        try:
            cursor = self.connection.cursor()
            for nota in notas:
                cursor.execute(
                    f""" UPDATE Notas SET Data_saida = '{data_saida}', usuario = '{usuario}' WHERE Nfe = '{nota}' """
                )
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão para alterar os campos")

    def update_estorno(self, notas):
        try:
            cursor = self.connection.cursor()
            for nota in notas:
                cursor.execute(f"UPDATE Notas SET Data_saida = '' WHERE Nfe ={nota} ")
                self.connection.commit()
        except AttributeError:
            print("Faça a conexão para alterar os campos")

    def crate_table_cliente(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        rg TEXT UNIQUE NOT NULL,
                        nome TEXT NOT NULL,
                        data_nasc TEXT NOT NULL,
                        responsavel TEXT,
                        email TEXT,
                        telefone TEXT NOT NULL,
                        telefone2 TEXT,
                        endereco TEXT NOT NULL,
                        num INTEGER NOT NULL,
                        cep INTEGER NOT NULL,
                        observacao TEXT
                    );
                    """
            )
        except AttributeError:
            print("Faça a conexão")

    def insert_cliente(
        self,
        rg,
        nome,
        data_nasc,
        responsavel,
        email,
        telefone,
        telefone2,
        endereco,
        numero,
        cep,
        observacao,
    ):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                    INSERT INTO clientes (rg, nome, data_nasc, responsavel, email, telefone, telefone2, endereco, num, cep, observacao)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?)
            """,
                (
                    rg,
                    nome,
                    data_nasc,
                    responsavel,
                    email,
                    telefone,
                    telefone2,
                    endereco,
                    numero,
                    cep,
                    observacao,
                ),
            )
            self.connection.commit()

        except AttributeError:
            print("Faça a conexão")

    def check_client_rg(self, rg):
        try:
            cursor = self.connection.cursor()

            # Executar consulta SQL para verificar se o RG já existe
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE rg = ?", (rg,))
            resultado = cursor.fetchone()[0]

            # Verificar se o RG existe ou não
            if resultado > 0:
                return True  # RG já existe no banco de dados
            else:
                return False  # RG não existe no banco de dados

        except AttributeError:
            print("Faça a conexão")


if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_table_user()
    db.create_table_nfe()
    db.crate_table_cliente()
    db.close_connection()
