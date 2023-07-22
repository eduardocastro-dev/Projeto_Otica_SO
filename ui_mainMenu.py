# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QTabWidget,
    QTableView,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 637)
        MainWindow.setStyleSheet("background-color: rgb(0, 68, 85);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName("btn_home")
        self.btn_home.setMinimumSize(QSize(0, 35))
        self.btn_home.setBaseSize(QSize(0, 35))
        font = QFont()
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(
            "QPushButton{\n"
            "	color:rgb(255,255,255);\n"
            "	border-radius: 1px;\n"
            "	font-size: 16px;\n"
            "	background-color: rgb(0,80,121);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: #fff; \n"
            "color:black\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_os = QPushButton(self.frame)
        self.btn_os.setObjectName("btn_os")
        self.btn_os.setMinimumSize(QSize(0, 35))
        self.btn_os.setBaseSize(QSize(0, 35))
        self.btn_os.setFont(font)
        self.btn_os.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_os.setStyleSheet(
            "QPushButton{\n"
            "	color:rgb(255,255,255);\n"
            "	border-radius: 1px;\n"
            "	font-size: 16px;\n"
            "	background-color: rgb(0,80,121);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: #fff; \n"
            "color:black\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_os)

        self.btn_clientes = QPushButton(self.frame)
        self.btn_clientes.setObjectName("btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(0, 35))
        self.btn_clientes.setBaseSize(QSize(0, 35))
        self.btn_clientes.setFont(font)
        self.btn_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clientes.setStyleSheet(
            "QPushButton{\n"
            "	color:rgb(255,255,255);\n"
            "	border-radius: 1px;\n"
            "	font-size: 16px;\n"
            "	background-color: rgb(0,80,121);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: #fff; \n"
            "color:black\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_clientes)

        self.btn_importar = QPushButton(self.frame)
        self.btn_importar.setObjectName("btn_importar")
        self.btn_importar.setMinimumSize(QSize(0, 35))
        self.btn_importar.setBaseSize(QSize(0, 35))
        self.btn_importar.setFont(font)
        self.btn_importar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importar.setStyleSheet(
            "QPushButton{\n"
            "	color:rgb(255,255,255);\n"
            "	border-radius: 1px;\n"
            "	font-size: 16px;\n"
            "	background-color: rgb(0,80,121);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: #fff; \n"
            "color:black\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_importar)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName("btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 35))
        self.btn_tables.setBaseSize(QSize(0, 35))
        self.btn_tables.setFont(font)
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(
            "QPushButton{\n"
            "	color:rgb(255,255,255);\n"
            "	border-radius: 1px;\n"
            "	font-size: 16px;\n"
            "	background-color: rgb(0,80,121);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: #fff; \n"
            "color:black\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName("btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 35))
        self.btn_contato.setBaseSize(QSize(0, 35))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(
            "QPushButton{\n"
            "	color:rgb(255,255,255);\n"
            "	border-radius: 1px;\n"
            "	font-size: 16px;\n"
            "	background-color: rgb(0,80,121);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: #fff; \n"
            "color:black\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName("btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 35))
        self.btn_sobre.setBaseSize(QSize(0, 35))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(
            "QPushButton{\n"
            "	color:rgb(255,255,255);\n"
            "	border-radius: 1px;\n"
            "	font-size: 16px;\n"
            "	background-color: rgb(0,80,121);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: #fff; \n"
            "color:black\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.verticalLayout_2.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName("Pages")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.Pages.setFont(font1)
        self.Pages.setStyleSheet("background-color: rgb(0,80,121);")
        self.pg_tables = QWidget()
        self.pg_tables.setObjectName("pg_tables")
        self.verticalLayout_9 = QVBoxLayout(self.pg_tables)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget = QTabWidget(self.pg_tables)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName("label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tab)
        self.tw_estoque.setObjectName("tw_estoque")

        self.verticalLayout_5.addWidget(self.tw_estoque)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tab)
        self.tw_saida.setObjectName("tw_saida")

        self.verticalLayout_4.addWidget(self.tw_saida)

        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName("btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(100, 25))
        self.btn_gerar.setStyleSheet(
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

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.btn_extornar = QPushButton(self.frame_2)
        self.btn_extornar.setObjectName("btn_extornar")
        self.btn_extornar.setMinimumSize(QSize(100, 25))
        self.btn_extornar.setStyleSheet(
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

        self.verticalLayout_3.addWidget(self.btn_extornar)

        self.btn_ = QPushButton(self.frame_2)
        self.btn_.setObjectName("btn_")
        self.btn_.setMinimumSize(QSize(100, 25))
        self.btn_.setStyleSheet(
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

        self.verticalLayout_3.addWidget(self.btn_)

        self.verticalSpacer = QSpacerItem(
            10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        font2 = QFont()
        font2.setFamilies(["Caladea"])
        font2.setPointSize(28)
        font2.setBold(False)
        font2.setItalic(True)
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet('font: italic 28pt "Caladea";')
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_20)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName("txt_filtro")
        self.txt_filtro.setMaximumSize(QSize(16777215, 31))
        self.txt_filtro.setBaseSize(QSize(0, 30))
        font3 = QFont()
        font3.setPointSize(12)
        self.txt_filtro.setFont(font3)
        self.txt_filtro.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.txt_filtro)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btn_grafico = QPushButton(self.tab_2)
        self.btn_grafico.setObjectName("btn_grafico")
        self.btn_grafico.setMinimumSize(QSize(0, 30))
        self.btn_grafico.setFont(font)
        self.btn_grafico.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_grafico.setStyleSheet(
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

        self.horizontalLayout_13.addWidget(self.btn_grafico)

        self.btn_exel = QPushButton(self.tab_2)
        self.btn_exel.setObjectName("btn_exel")
        self.btn_exel.setMinimumSize(QSize(0, 30))
        self.btn_exel.setFont(font)
        self.btn_exel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exel.setStyleSheet(
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

        self.horizontalLayout_13.addWidget(self.btn_exel)

        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.tb_geral = QTableView(self.tab_2)
        self.tb_geral.setObjectName("tb_geral")

        self.verticalLayout_11.addWidget(self.tb_geral)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_tables)
        self.pg_os = QWidget()
        self.pg_os.setObjectName("pg_os")
        self.label_16 = QLabel(self.pg_os)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(250, 10, 191, 31))
        font4 = QFont()
        font4.setPointSize(20)
        self.label_16.setFont(font4)
        self.Pages.addWidget(self.pg_os)
        self.pg_cadastro_cliente = QWidget()
        self.pg_cadastro_cliente.setObjectName("pg_cadastro_cliente")
        self.verticalLayout_18 = QVBoxLayout(self.pg_cadastro_cliente)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_31 = QLabel(self.pg_cadastro_cliente)
        self.label_31.setObjectName("label_31")
        self.label_31.setStyleSheet('font: italic 28pt "Caladea";')

        self.horizontalLayout_18.addWidget(self.label_31)

        self.label_18 = QLabel(self.pg_cadastro_cliente)
        self.label_18.setObjectName("label_18")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMaximumSize(QSize(300, 16777215))
        self.label_18.setLayoutDirection(Qt.LeftToRight)
        self.label_18.setPixmap(QPixmap("imagens/Cadastro_cli.png"))
        self.label_18.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_18)

        self.verticalLayout_17.addLayout(self.horizontalLayout_18)

        self.tw_dados_cliente = QTabWidget(self.pg_cadastro_cliente)
        self.tw_dados_cliente.setObjectName("tw_dados_cliente")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_31 = QVBoxLayout(self.tab_3)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.btn_pesquisar_cliente = QPushButton(self.tab_3)
        self.btn_pesquisar_cliente.setObjectName("btn_pesquisar_cliente")
        self.btn_pesquisar_cliente.setMinimumSize(QSize(100, 25))
        self.btn_pesquisar_cliente.setCursor(QCursor(Qt.PointingHandCursor))
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

        self.horizontalLayout_22.addWidget(self.btn_pesquisar_cliente)

        self.btn_cadastrar_cliente = QPushButton(self.tab_3)
        self.btn_cadastrar_cliente.setObjectName("btn_cadastrar_cliente")
        self.btn_cadastrar_cliente.setMinimumSize(QSize(100, 25))
        self.btn_cadastrar_cliente.setCursor(QCursor(Qt.PointingHandCursor))
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

        self.horizontalLayout_22.addWidget(self.btn_cadastrar_cliente)

        self.btn_salvar = QPushButton(self.tab_3)
        self.btn_salvar.setObjectName("btn_salvar")
        self.btn_salvar.setMinimumSize(QSize(100, 25))
        self.btn_salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar.setStyleSheet(
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

        self.horizontalLayout_22.addWidget(self.btn_salvar)

        self.btn_excluir = QPushButton(self.tab_3)
        self.btn_excluir.setObjectName("btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(100, 25))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(
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

        self.horizontalLayout_22.addWidget(self.btn_excluir)

        self.verticalLayout_31.addLayout(self.horizontalLayout_22)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_33 = QLabel(self.tab_3)
        self.label_33.setObjectName("label_33")

        self.verticalLayout_19.addWidget(self.label_33)

        self.txt_nome_cliente = QLineEdit(self.tab_3)
        self.txt_nome_cliente.setObjectName("txt_nome_cliente")
        self.txt_nome_cliente.setMinimumSize(QSize(0, 0))
        self.txt_nome_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.verticalLayout_19.addWidget(self.txt_nome_cliente)

        self.verticalLayout_27.addLayout(self.verticalLayout_19)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_32 = QLabel(self.tab_3)
        self.label_32.setObjectName("label_32")

        self.verticalLayout_24.addWidget(self.label_32)

        self.txt_rg_cliente = QLineEdit(self.tab_3)
        self.txt_rg_cliente.setObjectName("txt_rg_cliente")
        self.txt_rg_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.verticalLayout_24.addWidget(self.txt_rg_cliente)

        self.horizontalLayout_19.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_39 = QLabel(self.tab_3)
        self.label_39.setObjectName("label_39")

        self.verticalLayout_25.addWidget(self.label_39)

        self.txt_data_nasc = QLineEdit(self.tab_3)
        self.txt_data_nasc.setObjectName("txt_data_nasc")
        self.txt_data_nasc.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_data_nasc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.txt_data_nasc)

        self.horizontalLayout_19.addLayout(self.verticalLayout_25)

        self.verticalLayout_27.addLayout(self.horizontalLayout_19)

        self.verticalLayout_28.addLayout(self.verticalLayout_27)

        self.label_41 = QLabel(self.tab_3)
        self.label_41.setObjectName("label_41")

        self.verticalLayout_28.addWidget(self.label_41)

        self.txt_responsavel_cliente = QLineEdit(self.tab_3)
        self.txt_responsavel_cliente.setObjectName("txt_responsavel_cliente")
        self.txt_responsavel_cliente.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.verticalLayout_28.addWidget(self.txt_responsavel_cliente)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_35 = QLabel(self.tab_3)
        self.label_35.setObjectName("label_35")

        self.verticalLayout_22.addWidget(self.label_35)

        self.txt_email = QLineEdit(self.tab_3)
        self.txt_email.setObjectName("txt_email")
        self.txt_email.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.verticalLayout_22.addWidget(self.txt_email)

        self.horizontalLayout_20.addLayout(self.verticalLayout_22)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_34 = QLabel(self.tab_3)
        self.label_34.setObjectName("label_34")

        self.verticalLayout_20.addWidget(self.label_34)

        self.txt_tef1 = QLineEdit(self.tab_3)
        self.txt_tef1.setObjectName("txt_tef1")
        self.txt_tef1.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_tef1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.txt_tef1)

        self.horizontalLayout_20.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_40 = QLabel(self.tab_3)
        self.label_40.setObjectName("label_40")

        self.verticalLayout_21.addWidget(self.label_40)

        self.txt_tef2 = QLineEdit(self.tab_3)
        self.txt_tef2.setObjectName("txt_tef2")
        self.txt_tef2.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_tef2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.txt_tef2)

        self.horizontalLayout_20.addLayout(self.verticalLayout_21)

        self.verticalLayout_28.addLayout(self.horizontalLayout_20)

        self.verticalLayout_30.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_36 = QLabel(self.tab_3)
        self.label_36.setObjectName("label_36")

        self.verticalLayout_15.addWidget(self.label_36)

        self.txt_endereco = QLineEdit(self.tab_3)
        self.txt_endereco.setObjectName("txt_endereco")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_endereco.sizePolicy().hasHeightForWidth()
        )
        self.txt_endereco.setSizePolicy(sizePolicy1)
        self.txt_endereco.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.verticalLayout_15.addWidget(self.txt_endereco)

        self.horizontalLayout_21.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_37 = QLabel(self.tab_3)
        self.label_37.setObjectName("label_37")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy2)
        self.label_37.setMinimumSize(QSize(100, 0))

        self.verticalLayout_16.addWidget(self.label_37)

        self.txt_num_end = QLineEdit(self.tab_3)
        self.txt_num_end.setObjectName("txt_num_end")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txt_num_end.sizePolicy().hasHeightForWidth())
        self.txt_num_end.setSizePolicy(sizePolicy3)
        self.txt_num_end.setMaximumSize(QSize(150, 16777215))
        self.txt_num_end.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_num_end.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.txt_num_end)

        self.horizontalLayout_21.addLayout(self.verticalLayout_16)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_42 = QLabel(self.tab_3)
        self.label_42.setObjectName("label_42")
        self.label_42.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_26.addWidget(self.label_42)

        self.txt_cep = QLineEdit(self.tab_3)
        self.txt_cep.setObjectName("txt_cep")
        sizePolicy3.setHeightForWidth(self.txt_cep.sizePolicy().hasHeightForWidth())
        self.txt_cep.setSizePolicy(sizePolicy3)
        self.txt_cep.setMaximumSize(QSize(150, 16777215))
        self.txt_cep.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.txt_cep)

        self.horizontalLayout_21.addLayout(self.verticalLayout_26)

        self.verticalLayout_29.addLayout(self.horizontalLayout_21)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_38 = QLabel(self.tab_3)
        self.label_38.setObjectName("label_38")

        self.verticalLayout_23.addWidget(self.label_38)

        self.txt_obs = QLineEdit(self.tab_3)
        self.txt_obs.setObjectName("txt_obs")
        self.txt_obs.setMinimumSize(QSize(0, 40))
        self.txt_obs.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.5);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.verticalLayout_23.addWidget(self.txt_obs)

        self.verticalLayout_29.addLayout(self.verticalLayout_23)

        self.verticalLayout_30.addLayout(self.verticalLayout_29)

        self.verticalLayout_31.addLayout(self.verticalLayout_30)

        self.tw_dados_cliente.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_34 = QVBoxLayout(self.tab_4)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.lineEdit = QLineEdit(self.tab_4)
        self.lineEdit.setObjectName("lineEdit")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        self.lineEdit.setFont(font5)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.lineEdit)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.tw_os_pendente = QTableWidget(self.tab_4)
        if self.tw_os_pendente.columnCount() < 9:
            self.tw_os_pendente.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_os_pendente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_os_pendente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_os_pendente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_os_pendente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_os_pendente.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_os_pendente.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_os_pendente.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_os_pendente.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_os_pendente.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tw_os_pendente.setObjectName("tw_os_pendente")

        self.horizontalLayout_24.addWidget(self.tw_os_pendente)

        self.btn_baixa_os = QPushButton(self.tab_4)
        self.btn_baixa_os.setObjectName("btn_baixa_os")
        self.btn_baixa_os.setMinimumSize(QSize(100, 25))
        self.btn_baixa_os.setStyleSheet(
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

        self.horizontalLayout_24.addWidget(self.btn_baixa_os)

        self.verticalLayout_32.addLayout(self.horizontalLayout_24)

        self.verticalLayout_33.addLayout(self.verticalLayout_32)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.tw_os_paga = QTableWidget(self.tab_4)
        if self.tw_os_paga.columnCount() < 6:
            self.tw_os_paga.setColumnCount(6)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_os_paga.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_os_paga.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_os_paga.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_os_paga.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_os_paga.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_os_paga.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        self.tw_os_paga.setObjectName("tw_os_paga")

        self.horizontalLayout_23.addWidget(self.tw_os_paga)

        self.btn_extorna_os = QPushButton(self.tab_4)
        self.btn_extorna_os.setObjectName("btn_extorna_os")
        self.btn_extorna_os.setMinimumSize(QSize(100, 25))
        self.btn_extorna_os.setStyleSheet(
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

        self.horizontalLayout_23.addWidget(self.btn_extorna_os)

        self.verticalLayout_33.addLayout(self.horizontalLayout_23)

        self.verticalLayout_34.addLayout(self.verticalLayout_33)

        self.tw_dados_cliente.addTab(self.tab_4, "")

        self.verticalLayout_17.addWidget(self.tw_dados_cliente)

        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.Pages.addWidget(self.pg_cadastro_cliente)
        self.pg_home = QWidget()
        self.pg_home.setObjectName("pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: rgb(0,80,121);")

        self.verticalLayout.addWidget(self.label)

        self.btn_pg_cadastro = QPushButton(self.pg_home)
        self.btn_pg_cadastro.setObjectName("btn_pg_cadastro")
        self.btn_pg_cadastro.setFont(font)
        self.btn_pg_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(
            "QPushButton{\n"
            "	color:rgb(255,255,255);\n"
            "	border- radius: 1px;\n"
            "	font-size: 16px;\n"
            "	background-color: rgb(0,80,121);\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: #fff; \n"
            "color:black\n"
            "}"
        )

        self.verticalLayout.addWidget(self.btn_pg_cadastro)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro_usuario = QWidget()
        self.pg_cadastro_usuario.setObjectName("pg_cadastro_usuario")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastro_usuario)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_14 = QLabel(self.pg_cadastro_usuario)
        self.label_14.setObjectName("label_14")
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet('font: italic 28pt "Caladea";')
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro_usuario)
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet('font: italic 28pt "Caladea";')
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, -1, -1, -1)
        self.label_7 = QLabel(self.pg_cadastro_usuario)
        self.label_7.setObjectName("label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro_usuario)
        self.txt_nome.setObjectName("txt_nome")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy4)
        self.txt_nome.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.1);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.horizontalLayout_5.addWidget(self.txt_nome)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(30, -1, -1, -1)
        self.label_8 = QLabel(self.pg_cadastro_usuario)
        self.label_8.setObjectName("label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro_usuario)
        self.txt_usuario.setObjectName("txt_usuario")
        sizePolicy4.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy4)
        self.txt_usuario.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.1);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )

        self.horizontalLayout_6.addWidget(self.txt_usuario)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(30, -1, -1, -1)
        self.label_9 = QLabel(self.pg_cadastro_usuario)
        self.label_9.setObjectName("label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha.setObjectName("txt_senha")
        sizePolicy4.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy4)
        self.txt_senha.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.1);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)

        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(30, -1, -1, -1)
        self.label_10 = QLabel(self.pg_cadastro_usuario)
        self.label_10.setObjectName("label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha_2.setObjectName("txt_senha_2")
        sizePolicy4.setHeightForWidth(self.txt_senha_2.sizePolicy().hasHeightForWidth())
        self.txt_senha_2.setSizePolicy(sizePolicy4)
        self.txt_senha_2.setStyleSheet(
            "color:rgba(211,236,251,1);\n"
            "border-bottom: 1px solid white;\n"
            "border-radius:None;\n"
            "background-color:rgba(85,115,155,0.1);\n"
            "font-family:Trebucher Ms;\n"
            "font-size: 21px;"
        )
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.txt_senha_2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(30, -1, -1, -1)
        self.label_11 = QLabel(self.pg_cadastro_usuario)
        self.label_11.setObjectName("label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro_usuario)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName("cb_perfil")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy5)
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.cb_perfil.setFont(font6)
        self.cb_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_perfil.setLayoutDirection(Qt.LeftToRight)
        self.cb_perfil.setStyleSheet("color:rgba(211,236,251,1);\n" "")

        self.horizontalLayout_9.addWidget(self.cb_perfil)

        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro_usuario)
        self.label_12.setObjectName("label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro_usuario)
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(
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

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro_usuario)
        self.label_13.setObjectName("label_13")

        self.horizontalLayout_10.addWidget(self.label_13)

        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.Pages.addWidget(self.pg_cadastro_usuario)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName("pg_contatos")
        self.verticalLayout_14 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_15 = QLabel(self.pg_contatos)
        self.label_15.setObjectName("label_15")
        self.label_15.setMaximumSize(QSize(16777215, 75))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet('font: italic 28pt "Caladea";')
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_26 = QLabel(self.pg_contatos)
        self.label_26.setObjectName("label_26")
        self.label_26.setMaximumSize(QSize(50, 50))
        self.label_26.setPixmap(QPixmap("imagens/git_icone.png"))
        self.label_26.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_26)

        self.label_22 = QLabel(self.pg_contatos)
        self.label_22.setObjectName("label_22")
        font7 = QFont()
        font7.setPointSize(25)
        self.label_22.setFont(font7)
        self.label_22.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_22)

        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_27 = QLabel(self.pg_contatos)
        self.label_27.setObjectName("label_27")
        self.label_27.setMaximumSize(QSize(60, 50))
        self.label_27.setPixmap(QPixmap("imagens/whats_icone.png"))
        self.label_27.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_27)

        self.label_23 = QLabel(self.pg_contatos)
        self.label_23.setObjectName("label_23")
        self.label_23.setFont(font7)
        self.label_23.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_23)

        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_29 = QLabel(self.pg_contatos)
        self.label_29.setObjectName("label_29")
        self.label_29.setMaximumSize(QSize(50, 50))
        self.label_29.setPixmap(QPixmap("imagens/linkedin_icone.png"))
        self.label_29.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_29)

        self.label_25 = QLabel(self.pg_contatos)
        self.label_25.setObjectName("label_25")
        self.label_25.setFont(font7)
        self.label_25.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_25)

        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_28 = QLabel(self.pg_contatos)
        self.label_28.setObjectName("label_28")
        self.label_28.setMaximumSize(QSize(50, 50))
        self.label_28.setPixmap(QPixmap("imagens/gmail_icone.png"))
        self.label_28.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_28)

        self.label_24 = QLabel(self.pg_contatos)
        self.label_24.setObjectName("label_24")
        self.label_24.setFont(font7)
        self.label_24.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_24)

        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_17.addLayout(self.verticalLayout_13)

        self.label_30 = QLabel(self.pg_contatos)
        self.label_30.setObjectName("label_30")
        self.label_30.setMaximumSize(QSize(250, 300))
        self.label_30.setPixmap(QPixmap("imagens/dream_TradingCard (2).jpg"))
        self.label_30.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_30)

        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName("pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_21 = QLabel(self.pg_sobre)
        self.label_21.setObjectName("label_21")
        self.label_21.setMinimumSize(QSize(100, 25))
        self.label_21.setMaximumSize(QSize(16777215, 50))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet('font: italic 28pt "Caladea";')
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_21)

        self.label_17 = QLabel(self.pg_sobre)
        self.label_17.setObjectName("label_17")

        self.verticalLayout_12.addWidget(self.label_17)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_importar = QWidget()
        self.pg_importar.setObjectName("pg_importar")
        self.verticalLayout_10 = QVBoxLayout(self.pg_importar)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_19 = QLabel(self.pg_importar)
        self.label_19.setObjectName("label_19")
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet('font: italic 28pt "Caladea";')
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_19)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.txt_importar = QLineEdit(self.pg_importar)
        self.txt_importar.setObjectName("txt_importar")
        self.txt_importar.setMaximumSize(QSize(16777215, 31))
        self.txt_importar.setBaseSize(QSize(0, 30))
        self.txt_importar.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_importar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.txt_importar)

        self.btn_abrir_2 = QPushButton(self.pg_importar)
        self.btn_abrir_2.setObjectName("btn_abrir_2")
        self.btn_abrir_2.setMinimumSize(QSize(120, 31))
        self.btn_abrir_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_abrir_2.setStyleSheet(
            "QPushButton{\n"
            "	background-color: #fff; \n"
            "	color:black;\n"
            "	border-top-right-radius: 15px;\n"
            "	font-size: 16px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(0, 158, 231);\n"
            "}"
        )

        self.horizontalLayout_11.addWidget(self.btn_abrir_2)

        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.progressBar = QProgressBar(self.pg_importar)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_10.addWidget(self.progressBar)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_4 = QLabel(self.pg_importar)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.btn_importarNFe = QPushButton(self.pg_importar)
        self.btn_importarNFe.setObjectName("btn_importarNFe")
        self.btn_importarNFe.setMinimumSize(QSize(0, 30))
        self.btn_importarNFe.setFont(font)
        self.btn_importarNFe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importarNFe.setStyleSheet(
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

        self.horizontalLayout_12.addWidget(self.btn_importarNFe)

        self.label_5 = QLabel(self.pg_importar)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.Pages.addWidget(self.pg_importar)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)
        self.tw_dados_cliente.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.btn_home.setText(QCoreApplication.translate("MainWindow", "Home", None))
        self.btn_os.setText(QCoreApplication.translate("MainWindow", "OS", None))
        self.btn_clientes.setText(
            QCoreApplication.translate("MainWindow", "Clientes", None)
        )
        self.btn_importar.setText(
            QCoreApplication.translate("MainWindow", "Importar", None)
        )
        self.btn_tables.setText(
            QCoreApplication.translate("MainWindow", "Estoque", None)
        )
        self.btn_contato.setText(
            QCoreApplication.translate("MainWindow", "Contato", None)
        )
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", "Sobre", None))
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#ffffff;">Entrada</span></p></body></html>',
                None,
            )
        )
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(
            14, QCoreApplication.translate("MainWindow", "Usu\u00e1rio", None)
        )
        ___qtreewidgetitem.setText(
            13,
            QCoreApplication.translate("MainWindow", "Data importa\u00e7\u00e3o", None),
        )
        ___qtreewidgetitem.setText(
            12, QCoreApplication.translate("MainWindow", "Valor produto", None)
        )
        ___qtreewidgetitem.setText(
            11, QCoreApplication.translate("MainWindow", "Unidade medida", None)
        )
        ___qtreewidgetitem.setText(
            10, QCoreApplication.translate("MainWindow", "Descri\u00e7\u00e3o", None)
        )
        ___qtreewidgetitem.setText(
            9, QCoreApplication.translate("MainWindow", "Quantidade", None)
        )
        ___qtreewidgetitem.setText(
            8, QCoreApplication.translate("MainWindow", "Cod item", None)
        )
        ___qtreewidgetitem.setText(
            7, QCoreApplication.translate("MainWindow", "Item", None)
        )
        ___qtreewidgetitem.setText(
            6, QCoreApplication.translate("MainWindow", "Total NFe", None)
        )
        ___qtreewidgetitem.setText(
            5, QCoreApplication.translate("MainWindow", "Emitente", None)
        )
        ___qtreewidgetitem.setText(
            4, QCoreApplication.translate("MainWindow", "CNPJ_Emitente", None)
        )
        ___qtreewidgetitem.setText(
            3, QCoreApplication.translate("MainWindow", "Chave", None)
        )
        ___qtreewidgetitem.setText(
            2, QCoreApplication.translate("MainWindow", "Data_emiss\u00e3o", None)
        )
        ___qtreewidgetitem.setText(
            1, QCoreApplication.translate("MainWindow", "Serie", None)
        )
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("MainWindow", "NFe", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#ffffff;">Saida</span></p></body></html>',
                None,
            )
        )
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(
            3, QCoreApplication.translate("MainWindow", "USUARIO", None)
        )
        ___qtreewidgetitem1.setText(
            2, QCoreApplication.translate("MainWindow", "DATA IMPORTACAO", None)
        )
        ___qtreewidgetitem1.setText(
            1, QCoreApplication.translate("MainWindow", "DATA SAIDA", None)
        )
        ___qtreewidgetitem1.setText(
            0, QCoreApplication.translate("MainWindow", "NFCE", None)
        )
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", "Saida", None))
        self.btn_extornar.setText(
            QCoreApplication.translate("MainWindow", "Extorno", None)
        )
        self.btn_.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Base", None),
        )
        self.label_20.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:28pt; font-weight:600; text-decoration: underline; color:#ffffff;">TELA ESTOQUE</span></p></body></html>',
                None,
            )
        )
        self.txt_filtro.setText("")
        self.txt_filtro.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Filtro", None)
        )
        self.btn_grafico.setText(
            QCoreApplication.translate("MainWindow", "GERAR GRAFICO", None)
        )
        self.btn_exel.setText(
            QCoreApplication.translate("MainWindow", "GERAR EXEL", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Estoque", None),
        )
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "Gera\u00e7\u00e3o de O.S", None)
        )
        self.label_31.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="right"><span style=" font-size:36pt; font-weight:600; text-decoration: underline; color:#ffffff;">CLIENTES</span></p></body></html>',
                None,
            )
        )
        self.label_18.setText("")
        self.btn_pesquisar_cliente.setText(
            QCoreApplication.translate("MainWindow", "PESQUISAR", None)
        )
        self.btn_cadastrar_cliente.setText(
            QCoreApplication.translate("MainWindow", "CADASTRAR", None)
        )
        self.btn_salvar.setText(
            QCoreApplication.translate("MainWindow", "SALVAR", None)
        )
        self.btn_excluir.setText(
            QCoreApplication.translate("MainWindow", "EXCLUIR", None)
        )
        self.label_33.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">NOME</span></p></body></html>',
                None,
            )
        )
        self.txt_nome_cliente.setText("")
        self.label_32.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">RG</span></p></body></html>',
                None,
            )
        )
        self.txt_rg_cliente.setInputMask(
            QCoreApplication.translate("MainWindow", "00.000.000-0", None)
        )
        self.txt_rg_cliente.setText(
            QCoreApplication.translate("MainWindow", "00.000.000-0", None)
        )
        self.txt_rg_cliente.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "00.000.000-0", None)
        )
        self.label_39.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">DATA DE NASCIMENTO</span></p></body></html>',
                None,
            )
        )
        self.txt_data_nasc.setInputMask(
            QCoreApplication.translate("MainWindow", "00/00/0000", None)
        )
        self.txt_data_nasc.setText(
            QCoreApplication.translate("MainWindow", "01/01/2000", None)
        )
        self.txt_data_nasc.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Dia /Mes /Ano", None)
        )
        self.label_41.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">RESPONSAVEL</span></p></body></html>',
                None,
            )
        )
        self.label_35.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">E-MAIL</span></p></body></html>',
                None,
            )
        )
        self.label_34.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">TELEFONE</span></p></body></html>',
                None,
            )
        )
        self.txt_tef1.setInputMask(
            QCoreApplication.translate("MainWindow", "(00)00000-0000", None)
        )
        self.txt_tef1.setText(
            QCoreApplication.translate("MainWindow", "(00)00000-0000", None)
        )
        self.txt_tef1.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "(00) 00000-0000", None)
        )
        self.label_40.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">TELEFONE (2)</span></p></body></html>',
                None,
            )
        )
        self.txt_tef2.setInputMask(
            QCoreApplication.translate("MainWindow", "(00)00000-0000", None)
        )
        self.txt_tef2.setText(
            QCoreApplication.translate("MainWindow", "(00)00000-0000", None)
        )
        self.txt_tef2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "(00) 00000-0000", None)
        )
        self.label_36.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">ENDERE\u00c7O</span></p></body></html>',
                None,
            )
        )
        self.label_37.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">N\u00ba</span></p></body></html>',
                None,
            )
        )
        self.label_42.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">CEP</span></p></body></html>',
                None,
            )
        )
        self.label_38.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">OBSERVA\u00c7\u00c3O</span></p></body></html>',
                None,
            )
        )
        self.tw_dados_cliente.setTabText(
            self.tw_dados_cliente.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "Dados cliente", None),
        )
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "FILTRO", None)
        )
        ___qtablewidgetitem = self.tw_os_pendente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "OS", None)
        )
        ___qtablewidgetitem1 = self.tw_os_pendente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "Servi\u00e7o", None)
        )
        ___qtablewidgetitem2 = self.tw_os_pendente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "Valor", None)
        )
        ___qtablewidgetitem3 = self.tw_os_pendente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", "Cod arma\u00e7\u00e3o", None)
        )
        ___qtablewidgetitem4 = self.tw_os_pendente.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", "Tipo de lente", None)
        )
        ___qtablewidgetitem5 = self.tw_os_pendente.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", "Data_emiss\u00e3o", None)
        )
        ___qtablewidgetitem6 = self.tw_os_pendente.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MainWindow", "Venciemento", None)
        )
        ___qtablewidgetitem7 = self.tw_os_pendente.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", "Responsavel", None)
        )
        self.btn_baixa_os.setText(
            QCoreApplication.translate("MainWindow", "BAIXA", None)
        )
        ___qtablewidgetitem8 = self.tw_os_paga.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("MainWindow", "OS", None)
        )
        ___qtablewidgetitem9 = self.tw_os_paga.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", "Valor", None)
        )
        ___qtablewidgetitem10 = self.tw_os_paga.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", "Servi\u00e7o", None)
        )
        ___qtablewidgetitem11 = self.tw_os_paga.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(
            QCoreApplication.translate("MainWindow", "New Column", None)
        )
        ___qtablewidgetitem12 = self.tw_os_paga.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", "Data_emiss\u00e3o", None)
        )
        ___qtablewidgetitem13 = self.tw_os_paga.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(
            QCoreApplication.translate("MainWindow", "Responsavel", None)
        )
        self.btn_extorna_os.setText(
            QCoreApplication.translate("MainWindow", "EXTORNO", None)
        )
        self.tw_dados_cliente.setTabText(
            self.tw_dados_cliente.indexOf(self.tab_4),
            QCoreApplication.translate("MainWindow", "Historico cliente", None),
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;">Sistema de gerenciamento</span><br/></p><p align="center"><img src="D:/Projeto_Optica/imagens/logo_2optica.png"/></p></body></html>',
                None,
            )
        )
        self.btn_pg_cadastro.setText(
            QCoreApplication.translate("MainWindow", "Cadastrar usuario", None)
        )
        self.label_14.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt; font-weight:600; text-decoration: underline; color:#ffffff;">Tela de cadastro</span></p></body></html>',
                None,
            )
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><img src="D:/Projeto_Optica/imagens/cadastro.png"/></p><p align="center"><span style=" font-size:18pt; font-weight:600; color:#ffffff;">Cadastrar usu\u00e1rio</span></p></body></html>',
                None,
            )
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">Nome: </span></p></body></html>',
                None,
            )
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">Usu\u00e1rio:</span></p></body></html>',
                None,
            )
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">Senha:  </span></p></body></html>',
                None,
            )
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">Senha: </span></p></body></html>',
                None,
            )
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#ffffff;">Perfil: </span></p></body></html>',
                None,
            )
        )
        self.cb_perfil.setItemText(
            0, QCoreApplication.translate("MainWindow", "Usu\u00e1rio", None)
        )
        self.cb_perfil.setItemText(
            1, QCoreApplication.translate("MainWindow", "Administrador", None)
        )

        self.label_12.setText("")
        self.btn_cadastrar.setText(
            QCoreApplication.translate("MainWindow", "Cadastrar", None)
        )
        self.label_13.setText("")
        self.label_15.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt; font-weight:600; font-style:normal; color:#ffffff;">CONTATOS</span></p></body></html>',
                None,
            )
        )
        self.label_26.setText("")
        self.label_22.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><a href="https://github.com/eduardocastro-dev"><span style=" font-size:16pt; font-weight:600; color:#ffffff;">Desenvolvedor: Eduardo Castro</span></a></p></body></html>',
                None,
            )
        )
        self.label_27.setText("")
        self.label_23.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt; font-weight:600; color:#ffffff;">(19)99554-5996</span></p></body></html>',
                None,
            )
        )
        self.label_29.setText("")
        self.label_25.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><a href="https://www.linkedin.com/in/eduardo-castro-138301187/"><span style=" font-size:16pt; text-decoration: underline; color:#ffffff;">Eduardo-castro</span></a></p></body></html>',
                None,
            )
        )
        self.label_28.setText("")
        self.label_24.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt; color:#ffffff;">eduardocastro.technology@gmail.com</span></p></body></html>',
                None,
            )
        )
        self.label_30.setText("")
        self.label_21.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt; font-weight:600; text-decoration: underline; color:#ffffff;">Sobre</span></p></body></html>',
                None,
            )
        )
        self.label_17.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; font-weight:600; text-decoration: underline; color:#ffffff;">Este sistema tem como objetvos:</span></p><p align="center"><span style=" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;">- Cadastro de usuarios e clientes</span></p><p align="center"><span style=" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;">- Gera\u00e7\u00e3o de O.S</span></p><p align="center"><span style=" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;">- Controle e baixa de vendas</span></p><p align="center"><span style=" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;">- Importa\u00e7\u00e3o de XML\u00b4s</span></p><p align="center"><span style=" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;">- Controle de estoque</span></p></body></html>',
                None,
            )
        )
        self.label_19.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:36pt; font-weight:600; text-decoration: underline; color:#ffffff;">Importa\u00e7\u00e3o</span></p></body></html>',
                None,
            )
        )
        self.txt_importar.setText("")
        self.txt_importar.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "Selecione a pasta com os arquivos XML -------->", None
            )
        )
        self.btn_abrir_2.setText(
            QCoreApplication.translate("MainWindow", "ABRIR", None)
        )
        self.label_4.setText("")
        self.btn_importarNFe.setText(
            QCoreApplication.translate("MainWindow", "Importar", None)
        )
        self.label_5.setText("")

    # retranslateUi
