import sqlite3


class DataBase:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    # Fecha conexão com o banco
    def close_connection(self):
        try:
            self.connection.close()
        except AttributeError:
            pass

    # Cria tabalea usuarios
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

    # Inseri dados Usario
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

    # Verifica o usuario
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

    # Inseri dados NFCE
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

    # Cria tabela NFCE
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

    # Atualzia estoque
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

    # Atualzia estorno
    def update_estorno(self, notas):
        try:
            cursor = self.connection.cursor()
            for nota in notas:
                cursor.execute(f"UPDATE Notas SET Data_saida = '' WHERE Nfe ={nota} ")
                self.connection.commit()
        except AttributeError:
            print("Faça a conexão para alterar os campos")

    # Cria a tabela cliente
    def crate_table_cliente(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        cpf TEXT UNIQUE NOT NULL,
                        nome TEXT NOT NULL,
                        data_nasc TEXT NOT NULL,
                        responsavel TEXT,
                        email TEXT,
                        telefone TEXT NOT NULL,
                        telefone2 TEXT,
                        endereco TEXT NOT NULL,
                        num INTEGER NOT NULL,
                        cep INTEGER NOT NULL,
                        observacao TEXT,
                        usuario TEXT NOT NULL
                    );
                    """
            )
        except AttributeError:
            print("Faça a conexão")

    # Verifica CPF cliente
    def check_client_cpf(self, cpf):
        try:
            cursor = self.connection.cursor()

            # Executar consulta SQL para verificar se o RG já existe
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE cpf = ?", (cpf,))
            resultado = cursor.fetchone()[0]

            # Verificar se o RG existe ou não
            if resultado > 0:
                return True  # RG já existe no banco de dados
            else:
                return False  # RG não existe no banco de dados

        except AttributeError:
            print("Faça a conexão")

    # Insere/altera dados do cliente
    def insert_cliente(
        self,
        cpf,
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
        usuario,
    ):
        try:
            cursor = self.connection.cursor()
            if self.check_client_cpf(cpf) is True:
                cursor.execute(
                    """
                    UPDATE clientes
                    SET nome = ?,
                        data_nasc = ?,
                        responsavel = ?,
                        email = ?,
                        telefone = ?,
                        telefone2 = ?,
                        endereco = ?,
                        num = ?,
                        cep = ?,
                        observacao = ?
                        usuario = ?
                    WHERE cpf = ?
                    """,
                    (
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
                        cpf,
                        usuario,
                    ),
                )
            else:
                cursor.execute(
                    """
                    INSERT INTO clientes (cpf, nome, data_nasc, responsavel, email, telefone, telefone2, endereco, num, cep, observacao, usuario)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                    """,
                    (
                        cpf,
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
                        usuario,
                    ),
                )
            self.connection.commit()

        except AttributeError:
            print("Faça a conexão")

    # Set informações de usuario caso exista
    def get_customer_info(self, cpf):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
            result = cursor.fetchone()

            if result:
                customer_info = {
                    "nome": result[2],
                    "data_nasc": result[3],  # Supondo que seja uma data
                    "responsavel": result[4],
                    "email": result[5],
                    "telefone1": result[6],
                    "telefone2": result[7],
                    "endereco": result[8],
                    "numero": result[9],
                    "cep": result[10],
                    "observacoes": result[11],
                }
                return customer_info
            else:
                return None

        except AttributeError:
            print("Faça a conexão")

    # Cria tabela OS
    def create_table_os(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS os (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    parcelas_os TEXT NOT NULL,
                    os INTEGER NOT NULL,
                    cpf TEXT NOT NULL,
                    nome_cliente TEXT NOT NULL,
                    armacao_valor INTEGER,
                    lentes_valor INTEGER,
                    outros INTEGER,
                    desconto INTEGER,
                    total INTEGER NOT NULL,
                    entrada INTEGER NOT NULL,
                    tipo_entrada TEXT NOT NULL,
                    valor_receber INTEGER NOT NULL,
                    tipo_pagamento TEXT NOT NULL,
                    vencimento INTEGER NOT NULL,
                    cod_armacao TEXT,
                    tipo_lente TEXT,
                    examinador TEXT,
                    anexo_receita BLOB,
                    usuario TEXT NOT NULL,
                    FOREIGN KEY (cpf) REFERENCES clientes (cpf)
                );
                """
            )
            print("Tabela OS criada com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela OS: {e}")

    def insert_os(self, **kwargs):
        """Insere um novo OS no banco de dados."""

        try:
            cursor = self.connection.cursor()

            query = """
                INSERT INTO os (
                    parcelas_os,
                    os,
                    cpf,
                    nome_cliente,
                    armacao_valor,
                    lentes_valor,
                    outros,
                    desconto,
                    total,
                    entrada,
                    tipo_entrada,
                    valor_receber,
                    tipo_pagamento,
                    vencimento,
                    cod_armacao,
                    tipo_lente,
                    examinador,
                    anexo_receita,
                    usuario
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            cursor.execute(query, tuple(kwargs.values()))
            self.connection.commit()
            cursor.close()
            print("Dados inseridos com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados na tabela OS: {e}")


if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_table_user()
    db.create_table_nfe()
    db.crate_table_cliente()
    db.create_table_os()
    db.close_connection()
