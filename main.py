from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QWidget,
    QMainWindow,
    QMessageBox,
    QTreeWidgetItem,
)
from PySide6 import QtCore
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from ui_login import Ui_Login
from ui_mainMenu import Ui_MainWindow
from dataBase import DataBase
from xml_files import Read_xml
from datetime import date
import sys
import sqlite3
import pandas as pd
import re
import matplotlib.pyplot as plt


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        # Btn_de_login
        self.btn_login.clicked.connect(self.check_login)

    # Função valida_usuario
    def check_login(self):
        self.users = DataBase()
        self.users.conecta()
        authenticator = self.users.check_user(
            self.txt_usuario.text().upper(), self.txt_senha.text()
        )

        if authenticator.lower() == "administrador" or authenticator == "usuário":
            self.w = MainWindow(self.txt_usuario.text(), authenticator.lower())
            self.w.show()
            self.close()

        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setWindowTitle("Verifique usuario ou senha!")
                msg.setText(
                    f"As credencias não conferem! \n \n Tentativas: {self.tentativas +1} de 3"
                )
                msg.exec()
                self.tentativas += 1

            # Block usuario
            if self.tentativas == 3:
                self.users.close_connection()
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        self.usuario = username

        # Esconde btn_cadastrar
        if user.lower() == "usuário":
            self.btn_pg_cadastro.setVisible(False)

        # --- TELAS DO SISTEMA
        # Tela principal
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))

        # Tela de cadastro usuario
        self.btn_pg_cadastro.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_cadastro_usuario)
        )

        # Tela de tabelas
        self.btn_tables.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_tables)
        )

        # Tela de O.S
        self.btn_os.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_os))

        # Tela de Clientes
        self.btn_clientes.clicked.connect(self.switch_to_cadastro_cliente)

        # Tela de contato
        self.btn_contato.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_contatos)
        )

        # Tela sobre
        self.btn_sobre.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_sobre)
        )

        # Tela importar
        self.btn_importar.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_importar)
        )

        # Btn cadastrar_usuario
        self.btn_cadastrar.clicked.connect(self.subscribe_user)

        # Btn cadastra_cliente
        self.btn_cadastrar_cliente.clicked.connect(
            lambda: self.subscribe_customer(username)
        )

        # Btn pesquisar cliente
        self.btn_pesquisar_cliente.clicked.connect(self.search_customer)

        # Btn editar cadastro cliente
        self.btn_editar_cliente.clicked.connect(self.edit_record)

        # --- ARQUIVO XML
        # Btn abrir_pasta_arquivo_XML
        self.btn_abrir_2.clicked.connect(self.open_path)

        # Btn Importar_xml
        self.btn_importarNFe.clicked.connect(self.import_xml_files)

        # Filtro
        self.txt_filtro.textChanged.connect(self.update_filter)

        # Atualzia tabelas
        self.reset_table()

        # Btn's Gerar
        # Btn saida
        self.btn_gerar.clicked.connect(self.gerar_saida)
        # Btn estorno
        self.btn_extornar.clicked.connect(self.gerar_estorno)
        # Btn Exel_estoque
        self.btn_exel.clicked.connect(self.exel_file_estoque)
        # Btn Grafico_estoque
        self.btn_grafico.clicked.connect(self.grafico_estoque)

    # Função_cadastrar_usuario
    def subscribe_user(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Senhas divergentes")
            msg.setText("As senhas não conferem!")
            msg.exec()
            return None

        nome = self.txt_nome.text()
        usuario = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()

        db.conecta()
        db.insert_user(nome, usuario, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Cadastro")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")

    # Função abre diretorio
    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(
            self,
            str("Open Directory"),
            "/home",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )
        self.txt_importar.setText(self.path)

    # Funçaõ importa XML
    def import_xml_files(self):
        xml = Read_xml(self.txt_importar.text())

        all = xml.all_files()
        self.progressBar.setMaximum(len(all))

        db = DataBase()
        db.conecta()

        cont = 1
        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            db.insert_data(fullDataSet)
            cont += 1

        # Atualizar tabelas
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Importação XML")
        msg.setText("Importação concluída")
        msg.exec()
        self.progressBar.setValue(0)

        db.close_connection()

    # Função tabela estoque
    def table_estoque(self):
        self.tw_estoque.setStyleSheet(
            " QHeaderView{ color:black}; color:#fff;font-size: 15px;"
        )
        cn = sqlite3.connect("system.db")
        result = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida = '' ", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            # Faz check para indentificar nota e nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_estoque, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        # Organiza itens
        self.tw_estoque.setSortingEnabled(True)

        # Da resize nos campos
        for i in range(1, 15):
            self.tw_estoque.resizeColumnToContents(i)

    # Função tabela saida
    def table_saida(self):
        self.tw_saida.setStyleSheet(
            " QHeaderView{ color:black}; color:#fff;font-size: 15px;"
        )
        cn = sqlite3.connect("system.db")
        result = pd.read_sql_query(
            """SELECT Nfe, serie data_importacao, data_saida, usuario FROM Notas WHERE data_saida != '' """,
            cn,
        )
        result = result.values.tolist()

        self.x = ""

        for i in result:
            # Faz check para indentificar nota e nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_saida, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        # Organiza itens
        self.tw_estoque.setSortingEnabled(True)

        # Da resize nos campos
        for i in range(1, 15):
            self.tw_estoque.resizeColumnToContents(i)

    # Função tabela geral
    def table_geral(self):
        self.tb_geral.setStyleSheet(
            " QHeaderView{ color:black}; color:#fff;font-size: 15px;"
        )

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_geral.setModel(self.model)
        self.model.setTable("Notas")
        self.model.select()

    # Função_limpa/atualiza
    def reset_table(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()

        self.table_saida()
        self.table_estoque()
        self.table_geral()

    # Função filtro
    def update_filter(self, s):
        s = re.sub("[w_]+", "", s)
        filter_str = 'Nfe LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    # Função saida_estoque
    def gerar_saida(self):
        self.checked_items_out = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items_out.append(child.text(0))

        recurse(self.tw_estoque.invisibleRootItem())

        # Confirmar ação com usuario
        self.question("saída")

    # Função estorna_estoque
    def gerar_estorno(self):
        self.checked_items = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items.append(child.text(0))

        recurse(self.tw_saida.invisibleRootItem())
        # Confirmar ação com usuario
        self.question("estorno")

    # Função confirmar_ação_estoque
    def question(self, table):
        msgBox = QMessageBox()

        if table == "estorno":
            msgBox.setText("Deseja estornar as notas selecionadas?")
            msgBox.setInformativeText(
                "As selecionadas voltarão para o estoque \n clique em 'Yes' para confirmar."
            )
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items}")

        else:
            msgBox.setText("Deseja Gerar saída das nota selecionadas?")
            msgBox.setInformativeText(
                "As notas abaixo será baixada no estoque \n clique em 'Yes' para confirmar."
            )
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items_out}")

        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:
            if table == "estorno":
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estorno(self.checked_items)
                self.db.close_connection()
                self.reset_table()

            else:
                data_saida = date.today()
                data_saida = data_saida.strftime("%d/%m/%Y")
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estoque(data_saida, self.usuario, self.checked_items_out)
                self.db.close_connection()
                self.reset_table()

    # Funcao exel_file
    def exel_file_estoque(self):
        cnx = sqlite3.connect("system.db")

        resultado = pd.read_sql_query("SELECT * FROM Notas", cnx)
        resultado.to_excel("Resumo de notas.xlsx", sheet_name="Notas", index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Relatorio de Notas")
        msg.setText("Relatorio gerado com sucesso! ")
        msg.exec()

    # Funcao grafico
    def grafico_estoque(self):
        cnx = sqlite3.connect("system.db")
        estoque = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida = ''", cnx)
        saida = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida != ''", cnx)

        estoque = len(estoque)
        saida = len(saida)

        labels = "Estoque", "Saídas"
        sizes = [estoque, saida]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
        ax1.axis("equal")

        plt.show()

    # Funcao  cadastro
    def switch_to_cadastro_cliente(self):
        self.disable_customer_fields()
        self.Pages.setCurrentWidget(self.pg_cadastro_cliente)
        self.txt_cpf_cliente.setText("00000000000")
        self.txt_nome_cliente.setText("")
        self.txt_data_nasc.setText("01012000")
        self.txt_responsavel_cliente.setText("")
        self.txt_email.setText("")
        self.txt_endereco.setText("")
        self.txt_tef1.setText("00000000000")
        self.txt_tef2.setText("00000000000")
        self.txt_num_end.setText("")
        self.txt_cep.setText("")
        self.txt_obs.setText("")

        self.txt_cpf_cliente.setEnabled(True)
        self.txt_cpf_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

    # Desabilita campos cliente até que usuario defina funcao
    def disable_customer_fields(self):
        self.btn_cadastrar_cliente.setEnabled(False)
        self.btn_editar_cliente.setEnabled(False)
        self.txt_nome_cliente.setEnabled(False)
        self.txt_data_nasc.setEnabled(False)
        self.txt_responsavel_cliente.setEnabled(False)
        self.txt_email.setEnabled(False)
        self.txt_tef1.setEnabled(False)
        self.txt_tef2.setEnabled(False)
        self.txt_endereco.setEnabled(False)
        self.txt_num_end.setEnabled(False)
        self.txt_cep.setEnabled(False)
        self.txt_obs.setEnabled(False)

        self.txt_nome_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.txt_data_nasc.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.txt_responsavel_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.txt_email.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.txt_tef1.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.txt_tef2.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.txt_endereco.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.txt_num_end.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.txt_cep.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.txt_obs.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.btn_cadastrar_cliente.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgba(0,0,0,0.5); \n"
            "	color:black;\n"
            "	border-radius: 10px;\n"
            "	font-size: 16px;\n"
            "}\n"
        )
        self.btn_editar_cliente.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgba(0,0,0,0.5); \n"
            "	color:black;\n"
            "	border-radius: 10px;\n"
            "	font-size: 16px;\n"
            "}\n"
        )

        # self.txt_rg_cliente.setStyleSheet("") << Retira estilo personalizado

    # Habilita campos cliente quando for cadastro ou edição
    def enable_customer_fields(self):
        self.btn_cadastrar_cliente.setEnabled(True)
        self.txt_nome_cliente.setEnabled(True)
        self.txt_data_nasc.setEnabled(True)
        self.txt_responsavel_cliente.setEnabled(True)
        self.txt_email.setEnabled(True)
        self.txt_tef1.setEnabled(True)
        self.txt_tef2.setEnabled(True)
        self.txt_endereco.setEnabled(True)
        self.txt_num_end.setEnabled(True)
        self.txt_cep.setEnabled(True)
        self.txt_obs.setEnabled(True)

        self.txt_nome_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_data_nasc.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_responsavel_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_email.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_tef1.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_tef2.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_endereco.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_num_end.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_cep.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_obs.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.btn_cadastrar_cliente.setStyleSheet(
            "QPushButton{\n"
            "	background-color: #fff; \n"
            "	color:black;\n"
            "	border-radius: 10px;\n"
            "	font-size: 16px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(0, 158, 231);\n"
            "}"
        )

    # Funcao cadastra cliente
    def subscribe_customer(self, usuario):
        cpf = self.txt_cpf_cliente.text()
        nome = self.txt_nome_cliente.text()
        data_nasc = self.txt_data_nasc.text()
        responsavel = self.txt_responsavel_cliente.text()
        email = self.txt_email.text()
        telefone = self.txt_tef1.text()
        telefone2 = self.txt_tef2.text()
        endereco = self.txt_endereco.text()
        num = self.txt_num_end.text()
        cep = self.txt_cep.text()
        obs = self.txt_obs.text()

        db = DataBase()
        db.conecta()
        db.insert_cliente(
            cpf,
            nome,
            data_nasc,
            responsavel,
            email,
            telefone,
            telefone2,
            endereco,
            num,
            cep,
            obs,
            usuario,
        )
        db.close_connection()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Cadastro cliente")
        msg.setText("Cadastro salvo!")
        msg.exec()

        self.btn_pesquisar_cliente.setEnabled(True)
        self.btn_pesquisar_cliente_bd.setEnabled(True)
        self.txt_cpf_cliente.setEnabled(True)

        self.btn_pesquisar_cliente_bd.setStyleSheet(
            "QPushButton{\n"
            "	background-color: #fff; \n"
            "	color:black;\n"
            "	border-radius: 10px;\n"
            "	font-size: 16px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(0, 158, 231);\n"
            "}"
        )
        self.btn_pesquisar_cliente.setStyleSheet(
            "QPushButton{\n"
            "	background-color: #fff; \n"
            "	color:black;\n"
            "	border-radius: 10px;\n"
            "	font-size: 16px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(0, 158, 231);\n"
            "}"
        )

        self.txt_cpf_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.disable_customer_fields()

        return None

    # Funcao Procura cliente
    def search_customer(self):
        cpf = self.txt_cpf_cliente.text()
        msgBox = QMessageBox()
        db = DataBase()
        db.conecta()

        if db.check_client_cpf(cpf) is False:
            msgBox = QMessageBox()
            msgBox.setText("Deseja cadastrar o Cliente?")
            msgBox.setInformativeText(
                "O CPF informado será cadastrado no sistema\nclique em 'Yes' para confirmar."
            )
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.No)
            msgBox.setDetailedText(f"O seguinte CPF será cadastrado: {cpf}")

        else:
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Cliente já cadastrado")
            msgBox.setText("Exibindo dados")
            self.btn_editar_cliente.setEnabled(True)
            self.btn_editar_cliente.setStyleSheet(
                "QPushButton{\n"
                "	background-color: #fff; \n"
                "	color:black;\n"
                "	border-radius: 10px;\n"
                "	font-size: 16px;\n"
                "}\n"
                "\n"
                "QPushButton:hover{\n"
                "background-color: rgb(0, 158, 231);\n"
                "}"
            )
            customer_info = db.get_customer_info(cpf)
            self.txt_nome_cliente.setText(customer_info["nome"])
            self.txt_data_nasc.setText(customer_info["data_nasc"])
            self.txt_responsavel_cliente.setText(customer_info["responsavel"])
            self.txt_email.setText(customer_info["email"])
            self.txt_tef1.setText(customer_info["telefone1"])
            self.txt_tef2.setText(customer_info["telefone2"])
            self.txt_endereco.setText(customer_info["endereco"])
            self.txt_num_end.setText(str(customer_info["numero"]))
            self.txt_cep.setText(str(customer_info["cep"]))
            self.txt_obs.setText(customer_info["observacoes"])

        ret = msgBox.exec()

        if ret == QMessageBox.Yes:
            self.enable_customer_fields()

        db.close_connection()

    def edit_record(self):
        self.enable_customer_fields()
        self.btn_editar_cliente.setStyleSheet(
            "QPushButton{\n"
            "	background-color: #fff; \n"
            "	color:black;\n"
            "	border-radius: 10px;\n"
            "	font-size: 16px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(0, 158, 231);\n"
            "}"
        )
        self.btn_cadastrar_cliente.setStyleSheet(
            "QPushButton{\n"
            "	background-color: #fff; \n"
            "	color:black;\n"
            "	border-radius: 10px;\n"
            "	font-size: 16px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(0, 158, 231);\n"
            "}"
        )

        self.txt_cpf_cliente.setEnabled(False)

        self.txt_cpf_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(0,0,0,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
