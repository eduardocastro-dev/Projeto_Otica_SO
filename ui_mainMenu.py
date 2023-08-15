# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(696, 662)
        MainWindow.setMaximumSize(QSize(696, 662))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 68, 85);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 35))
        self.btn_home.setBaseSize(QSize(0, 35))
        font = QFont()
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0,80,121);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fff; \n"
"color:black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_clientes = QPushButton(self.frame)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(0, 35))
        self.btn_clientes.setBaseSize(QSize(0, 35))
        self.btn_clientes.setFont(font)
        self.btn_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clientes.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0,80,121);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fff; \n"
"color:black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_clientes)

        self.btn_os = QPushButton(self.frame)
        self.btn_os.setObjectName(u"btn_os")
        self.btn_os.setMinimumSize(QSize(0, 35))
        self.btn_os.setBaseSize(QSize(0, 35))
        self.btn_os.setFont(font)
        self.btn_os.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_os.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0,80,121);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fff; \n"
"color:black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_os)

        self.btn_importar = QPushButton(self.frame)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setMinimumSize(QSize(0, 35))
        self.btn_importar.setBaseSize(QSize(0, 35))
        self.btn_importar.setFont(font)
        self.btn_importar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importar.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0,80,121);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fff; \n"
"color:black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_importar)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 35))
        self.btn_tables.setBaseSize(QSize(0, 35))
        self.btn_tables.setFont(font)
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0,80,121);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fff; \n"
"color:black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 35))
        self.btn_contato.setBaseSize(QSize(0, 35))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0,80,121);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fff; \n"
"color:black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 35))
        self.btn_sobre.setBaseSize(QSize(0, 35))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0,80,121);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fff; \n"
"color:black\n"
"}")

        self.horizontalLayout.addWidget(self.btn_sobre)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.Pages.setFont(font1)
        self.Pages.setStyleSheet(u"background-color: rgb(0,80,121);")
        self.pg_tables = QWidget()
        self.pg_tables.setObjectName(u"pg_tables")
        self.verticalLayout_9 = QVBoxLayout(self.pg_tables)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(self.pg_tables)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tab)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_5.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tab)
        self.tw_saida.setObjectName(u"tw_saida")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_gerar = QPushButton(self.frame_2)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(100, 25))
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_gerar)

        self.btn_extornar = QPushButton(self.frame_2)
        self.btn_extornar.setObjectName(u"btn_extornar")
        self.btn_extornar.setMinimumSize(QSize(100, 25))
        self.btn_extornar.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_extornar)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        font2 = QFont()
        font2.setFamilies([u"Caladea"])
        font2.setPointSize(28)
        font2.setBold(False)
        font2.setItalic(True)
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"font: italic 28pt \"Caladea\";")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_20)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setMaximumSize(QSize(16777215, 31))
        self.txt_filtro.setBaseSize(QSize(0, 30))
        font3 = QFont()
        font3.setPointSize(12)
        self.txt_filtro.setFont(font3)
        self.txt_filtro.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.txt_filtro)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_grafico = QPushButton(self.tab_2)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setMinimumSize(QSize(0, 30))
        self.btn_grafico.setFont(font)
        self.btn_grafico.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_grafico.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_grafico)

        self.btn_exel = QPushButton(self.tab_2)
        self.btn_exel.setObjectName(u"btn_exel")
        self.btn_exel.setMinimumSize(QSize(0, 30))
        self.btn_exel.setFont(font)
        self.btn_exel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exel.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_exel)


        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.tb_geral = QTableView(self.tab_2)
        self.tb_geral.setObjectName(u"tb_geral")

        self.verticalLayout_11.addWidget(self.tb_geral)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_tables)
        self.pg_os = QWidget()
        self.pg_os.setObjectName(u"pg_os")
        self.horizontalLayout_57 = QHBoxLayout(self.pg_os)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.tabWidget_2 = QTabWidget(self.pg_os)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_53 = QVBoxLayout(self.tab_5)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_77 = QLabel(self.tab_5)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMaximumSize(QSize(739, 19))
        self.label_77.setStyleSheet(u"border-bottom: 1px solid white;")
        self.label_77.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_77)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_74 = QLabel(self.tab_5)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_55.addWidget(self.label_74)

        self.txt_cpf_cliente_os = QLineEdit(self.tab_5)
        self.txt_cpf_cliente_os.setObjectName(u"txt_cpf_cliente_os")
        self.txt_cpf_cliente_os.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_55.addWidget(self.txt_cpf_cliente_os)


        self.horizontalLayout_63.addLayout(self.horizontalLayout_55)

        self.btn_pesquisar_cliente_os = QPushButton(self.tab_5)
        self.btn_pesquisar_cliente_os.setObjectName(u"btn_pesquisar_cliente_os")
        self.btn_pesquisar_cliente_os.setMinimumSize(QSize(100, 25))
        self.btn_pesquisar_cliente_os.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_63.addWidget(self.btn_pesquisar_cliente_os)


        self.verticalLayout_43.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_76 = QLabel(self.tab_5)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_56.addWidget(self.label_76)

        self.txt_nome_cliente_os = QLineEdit(self.tab_5)
        self.txt_nome_cliente_os.setObjectName(u"txt_nome_cliente_os")
        self.txt_nome_cliente_os.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_56.addWidget(self.txt_nome_cliente_os)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_75 = QLabel(self.tab_5)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_61.addWidget(self.label_75)

        self.txt_responsavel_cliente_os = QLineEdit(self.tab_5)
        self.txt_responsavel_cliente_os.setObjectName(u"txt_responsavel_cliente_os")
        self.txt_responsavel_cliente_os.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_61.addWidget(self.txt_responsavel_cliente_os)


        self.horizontalLayout_56.addLayout(self.horizontalLayout_61)


        self.verticalLayout_43.addLayout(self.horizontalLayout_56)


        self.verticalLayout_44.addLayout(self.verticalLayout_43)


        self.verticalLayout_51.addLayout(self.verticalLayout_44)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_60 = QLabel(self.tab_5)
        self.label_60.setObjectName(u"label_60")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy)
        self.label_60.setMaximumSize(QSize(600, 19))
        self.label_60.setStyleSheet(u"border-bottom: 1px solid white;")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.label_60)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_43 = QLabel(self.tab_5)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_32.addWidget(self.label_43)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_50 = QLabel(self.tab_5)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_25.addWidget(self.label_50)

        self.txt_armacao_rs = QLineEdit(self.tab_5)
        self.txt_armacao_rs.setObjectName(u"txt_armacao_rs")
        self.txt_armacao_rs.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_25.addWidget(self.txt_armacao_rs)


        self.horizontalLayout_32.addLayout(self.horizontalLayout_25)


        self.verticalLayout_35.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_44 = QLabel(self.tab_5)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_33.addWidget(self.label_44)

        self.label_51 = QLabel(self.tab_5)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_33.addWidget(self.label_51)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.txt_lentes_rs = QLineEdit(self.tab_5)
        self.txt_lentes_rs.setObjectName(u"txt_lentes_rs")
        self.txt_lentes_rs.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_26.addWidget(self.txt_lentes_rs)


        self.horizontalLayout_33.addLayout(self.horizontalLayout_26)


        self.verticalLayout_35.addLayout(self.horizontalLayout_33)


        self.verticalLayout_36.addLayout(self.verticalLayout_35)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_45 = QLabel(self.tab_5)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_27.addWidget(self.label_45)

        self.label_53 = QLabel(self.tab_5)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_27.addWidget(self.label_53)

        self.txt_outros_rs = QLineEdit(self.tab_5)
        self.txt_outros_rs.setObjectName(u"txt_outros_rs")
        self.txt_outros_rs.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_27.addWidget(self.txt_outros_rs)


        self.verticalLayout_36.addLayout(self.horizontalLayout_27)


        self.verticalLayout_46.addLayout(self.verticalLayout_36)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_47 = QLabel(self.tab_5)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_29.addWidget(self.label_47)

        self.label_54 = QLabel(self.tab_5)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_29.addWidget(self.label_54)

        self.txt_descontos_rs = QLineEdit(self.tab_5)
        self.txt_descontos_rs.setObjectName(u"txt_descontos_rs")
        self.txt_descontos_rs.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_29.addWidget(self.txt_descontos_rs)


        self.verticalLayout_46.addLayout(self.horizontalLayout_29)


        self.verticalLayout_47.addLayout(self.verticalLayout_46)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_46 = QLabel(self.tab_5)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_35.addWidget(self.label_46)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_56 = QLabel(self.tab_5)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_28.addWidget(self.label_56)

        self.txt_total_rs = QLineEdit(self.tab_5)
        self.txt_total_rs.setObjectName(u"txt_total_rs")
        self.txt_total_rs.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_28.addWidget(self.txt_total_rs)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_28)


        self.verticalLayout_47.addLayout(self.horizontalLayout_35)


        self.horizontalLayout_39.addLayout(self.verticalLayout_47)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_55 = QLabel(self.tab_5)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_36.addWidget(self.label_55)

        self.txt_entrada_rs = QLineEdit(self.tab_5)
        self.txt_entrada_rs.setObjectName(u"txt_entrada_rs")
        self.txt_entrada_rs.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_36.addWidget(self.txt_entrada_rs)


        self.verticalLayout_41.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_59 = QLabel(self.tab_5)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_38.addWidget(self.label_59)

        self.cb_tipo = QComboBox(self.tab_5)
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.setObjectName(u"cb_tipo")
        self.cb_tipo.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_38.addWidget(self.cb_tipo)


        self.verticalLayout_41.addLayout(self.horizontalLayout_38)


        self.verticalLayout_49.addLayout(self.verticalLayout_41)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_49 = QLabel(self.tab_5)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_34.addWidget(self.label_49)

        self.cb_pagamento = QComboBox(self.tab_5)
        self.cb_pagamento.addItem("")
        self.cb_pagamento.addItem("")
        self.cb_pagamento.setObjectName(u"cb_pagamento")
        self.cb_pagamento.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_34.addWidget(self.cb_pagamento)


        self.verticalLayout_42.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_48 = QLabel(self.tab_5)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_37.addWidget(self.label_48)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_52 = QLabel(self.tab_5)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_52)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_31.addLayout(self.horizontalLayout_37)

        self.cb_a_pagar_os = QComboBox(self.tab_5)
        self.cb_a_pagar_os.setObjectName(u"cb_a_pagar_os")
        self.cb_a_pagar_os.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_31.addWidget(self.cb_a_pagar_os)


        self.verticalLayout_42.addLayout(self.horizontalLayout_31)


        self.verticalLayout_48.addLayout(self.verticalLayout_42)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_57 = QLabel(self.tab_5)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_40.addWidget(self.label_57)

        self.comboBox = QComboBox(self.tab_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_40.addWidget(self.comboBox)


        self.verticalLayout_48.addLayout(self.horizontalLayout_40)


        self.verticalLayout_49.addLayout(self.verticalLayout_48)


        self.horizontalLayout_39.addLayout(self.verticalLayout_49)


        self.verticalLayout_50.addLayout(self.horizontalLayout_39)


        self.horizontalLayout_41.addLayout(self.verticalLayout_50)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_16 = QLabel(self.tab_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(200, 0))
        font4 = QFont()
        font4.setPointSize(20)
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"border-bottom: 1px solid white;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_16)

        self.btn_gerar_os = QPushButton(self.tab_5)
        self.btn_gerar_os.setObjectName(u"btn_gerar_os")
        self.btn_gerar_os.setMinimumSize(QSize(100, 25))
        self.btn_gerar_os.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.verticalLayout_45.addWidget(self.btn_gerar_os)

        self.label_68 = QLabel(self.tab_5)
        self.label_68.setObjectName(u"label_68")

        self.verticalLayout_45.addWidget(self.label_68)

        self.btn_gerar_pdf_os = QPushButton(self.tab_5)
        self.btn_gerar_pdf_os.setObjectName(u"btn_gerar_pdf_os")
        self.btn_gerar_pdf_os.setMinimumSize(QSize(100, 25))
        self.btn_gerar_pdf_os.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.verticalLayout_45.addWidget(self.btn_gerar_pdf_os)

        self.label_69 = QLabel(self.tab_5)
        self.label_69.setObjectName(u"label_69")

        self.verticalLayout_45.addWidget(self.label_69)

        self.btn_teste = QPushButton(self.tab_5)
        self.btn_teste.setObjectName(u"btn_teste")
        self.btn_teste.setMinimumSize(QSize(100, 25))
        self.btn_teste.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.verticalLayout_45.addWidget(self.btn_teste)


        self.horizontalLayout_41.addLayout(self.verticalLayout_45)


        self.verticalLayout_51.addLayout(self.horizontalLayout_41)


        self.verticalLayout_52.addLayout(self.verticalLayout_51)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_73 = QLabel(self.tab_5)
        self.label_73.setObjectName(u"label_73")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy1)
        self.label_73.setMaximumSize(QSize(740, 19))
        self.label_73.setStyleSheet(u"border-bottom: 1px solid white;")
        self.label_73.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_73)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.btn_anexar_receita = QPushButton(self.tab_5)
        self.btn_anexar_receita.setObjectName(u"btn_anexar_receita")
        self.btn_anexar_receita.setMinimumSize(QSize(120, 30))
        self.btn_anexar_receita.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_46.addWidget(self.btn_anexar_receita)

        self.ln_anexo_receita = QLineEdit(self.tab_5)
        self.ln_anexo_receita.setObjectName(u"ln_anexo_receita")
        self.ln_anexo_receita.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ln_anexo_receita.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.ln_anexo_receita)


        self.verticalLayout_37.addLayout(self.horizontalLayout_46)


        self.verticalLayout_39.addLayout(self.verticalLayout_37)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_61 = QLabel(self.tab_5)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_43.addWidget(self.label_61)

        self.txt_cod_armacao = QLineEdit(self.tab_5)
        self.txt_cod_armacao.setObjectName(u"txt_cod_armacao")
        self.txt_cod_armacao.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_43.addWidget(self.txt_cod_armacao)


        self.verticalLayout_38.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_62 = QLabel(self.tab_5)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_44.addWidget(self.label_62)

        self.txt_tipo_lente = QLineEdit(self.tab_5)
        self.txt_tipo_lente.setObjectName(u"txt_tipo_lente")
        self.txt_tipo_lente.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_44.addWidget(self.txt_tipo_lente)


        self.verticalLayout_38.addLayout(self.horizontalLayout_44)


        self.verticalLayout_40.addLayout(self.verticalLayout_38)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_65 = QLabel(self.tab_5)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_60.addWidget(self.label_65)

        self.txt_examinador = QLineEdit(self.tab_5)
        self.txt_examinador.setObjectName(u"txt_examinador")
        self.txt_examinador.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_60.addWidget(self.txt_examinador)


        self.verticalLayout_40.addLayout(self.horizontalLayout_60)


        self.verticalLayout_39.addLayout(self.verticalLayout_40)


        self.verticalLayout_52.addLayout(self.verticalLayout_39)


        self.verticalLayout_53.addLayout(self.verticalLayout_52)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")

        self.horizontalLayout_57.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.pg_os)
        self.pg_cadastro_cliente = QWidget()
        self.pg_cadastro_cliente.setObjectName(u"pg_cadastro_cliente")
        self.verticalLayout_18 = QVBoxLayout(self.pg_cadastro_cliente)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_31 = QLabel(self.pg_cadastro_cliente)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: italic 28pt \"Caladea\";")

        self.horizontalLayout_18.addWidget(self.label_31)

        self.label_18 = QLabel(self.pg_cadastro_cliente)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMaximumSize(QSize(300, 16777215))
        self.label_18.setLayoutDirection(Qt.LeftToRight)
        self.label_18.setPixmap(QPixmap(u"imagens/Cadastro_cli.png"))
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_18)


        self.verticalLayout_17.addLayout(self.horizontalLayout_18)

        self.tw_dados_cliente = QTabWidget(self.pg_cadastro_cliente)
        self.tw_dados_cliente.setObjectName(u"tw_dados_cliente")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_31 = QVBoxLayout(self.tab_3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_pesquisar_cliente = QPushButton(self.tab_3)
        self.btn_pesquisar_cliente.setObjectName(u"btn_pesquisar_cliente")
        self.btn_pesquisar_cliente.setMinimumSize(QSize(100, 25))
        self.btn_pesquisar_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar_cliente.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_22.addWidget(self.btn_pesquisar_cliente)

        self.btn_pesquisar_cliente_bd = QPushButton(self.tab_3)
        self.btn_pesquisar_cliente_bd.setObjectName(u"btn_pesquisar_cliente_bd")
        self.btn_pesquisar_cliente_bd.setMinimumSize(QSize(100, 25))
        self.btn_pesquisar_cliente_bd.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar_cliente_bd.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_22.addWidget(self.btn_pesquisar_cliente_bd)

        self.btn_cadastrar_cliente = QPushButton(self.tab_3)
        self.btn_cadastrar_cliente.setObjectName(u"btn_cadastrar_cliente")
        self.btn_cadastrar_cliente.setMinimumSize(QSize(100, 25))
        self.btn_cadastrar_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_cliente.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_22.addWidget(self.btn_cadastrar_cliente)

        self.btn_editar_cliente = QPushButton(self.tab_3)
        self.btn_editar_cliente.setObjectName(u"btn_editar_cliente")
        self.btn_editar_cliente.setMinimumSize(QSize(100, 25))
        self.btn_editar_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar_cliente.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_22.addWidget(self.btn_editar_cliente)


        self.verticalLayout_31.addLayout(self.horizontalLayout_22)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_32 = QLabel(self.tab_3)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_24.addWidget(self.label_32)

        self.txt_cpf_cliente = QLineEdit(self.tab_3)
        self.txt_cpf_cliente.setObjectName(u"txt_cpf_cliente")
        self.txt_cpf_cliente.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.verticalLayout_24.addWidget(self.txt_cpf_cliente)


        self.horizontalLayout_19.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_39 = QLabel(self.tab_3)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_25.addWidget(self.label_39)

        self.txt_data_nasc = QLineEdit(self.tab_3)
        self.txt_data_nasc.setObjectName(u"txt_data_nasc")
        self.txt_data_nasc.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")
        self.txt_data_nasc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.txt_data_nasc)


        self.horizontalLayout_19.addLayout(self.verticalLayout_25)


        self.verticalLayout_19.addLayout(self.horizontalLayout_19)

        self.label_33 = QLabel(self.tab_3)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_19.addWidget(self.label_33)

        self.txt_nome_cliente = QLineEdit(self.tab_3)
        self.txt_nome_cliente.setObjectName(u"txt_nome_cliente")
        self.txt_nome_cliente.setMinimumSize(QSize(0, 0))
        self.txt_nome_cliente.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.verticalLayout_19.addWidget(self.txt_nome_cliente)


        self.verticalLayout_27.addLayout(self.verticalLayout_19)


        self.verticalLayout_28.addLayout(self.verticalLayout_27)

        self.label_41 = QLabel(self.tab_3)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_28.addWidget(self.label_41)

        self.txt_responsavel_cliente = QLineEdit(self.tab_3)
        self.txt_responsavel_cliente.setObjectName(u"txt_responsavel_cliente")
        self.txt_responsavel_cliente.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.verticalLayout_28.addWidget(self.txt_responsavel_cliente)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_35 = QLabel(self.tab_3)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_22.addWidget(self.label_35)

        self.txt_email = QLineEdit(self.tab_3)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.verticalLayout_22.addWidget(self.txt_email)


        self.horizontalLayout_20.addLayout(self.verticalLayout_22)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_34 = QLabel(self.tab_3)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_20.addWidget(self.label_34)

        self.txt_tef1 = QLineEdit(self.tab_3)
        self.txt_tef1.setObjectName(u"txt_tef1")
        self.txt_tef1.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")
        self.txt_tef1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.txt_tef1)


        self.horizontalLayout_20.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_40 = QLabel(self.tab_3)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_21.addWidget(self.label_40)

        self.txt_tef2 = QLineEdit(self.tab_3)
        self.txt_tef2.setObjectName(u"txt_tef2")
        self.txt_tef2.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")
        self.txt_tef2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.txt_tef2)


        self.horizontalLayout_20.addLayout(self.verticalLayout_21)


        self.verticalLayout_28.addLayout(self.horizontalLayout_20)


        self.verticalLayout_30.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_36 = QLabel(self.tab_3)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_15.addWidget(self.label_36)

        self.txt_endereco = QLineEdit(self.tab_3)
        self.txt_endereco.setObjectName(u"txt_endereco")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_endereco.sizePolicy().hasHeightForWidth())
        self.txt_endereco.setSizePolicy(sizePolicy2)
        self.txt_endereco.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.verticalLayout_15.addWidget(self.txt_endereco)


        self.horizontalLayout_21.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_37 = QLabel(self.tab_3)
        self.label_37.setObjectName(u"label_37")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy3)
        self.label_37.setMinimumSize(QSize(100, 0))

        self.verticalLayout_16.addWidget(self.label_37)

        self.txt_num_end = QLineEdit(self.tab_3)
        self.txt_num_end.setObjectName(u"txt_num_end")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txt_num_end.sizePolicy().hasHeightForWidth())
        self.txt_num_end.setSizePolicy(sizePolicy4)
        self.txt_num_end.setMaximumSize(QSize(150, 16777215))
        self.txt_num_end.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")
        self.txt_num_end.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.txt_num_end)


        self.horizontalLayout_21.addLayout(self.verticalLayout_16)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_42 = QLabel(self.tab_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_26.addWidget(self.label_42)

        self.txt_cep = QLineEdit(self.tab_3)
        self.txt_cep.setObjectName(u"txt_cep")
        sizePolicy4.setHeightForWidth(self.txt_cep.sizePolicy().hasHeightForWidth())
        self.txt_cep.setSizePolicy(sizePolicy4)
        self.txt_cep.setMaximumSize(QSize(150, 16777215))
        self.txt_cep.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.txt_cep)


        self.horizontalLayout_21.addLayout(self.verticalLayout_26)


        self.verticalLayout_29.addLayout(self.horizontalLayout_21)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_38 = QLabel(self.tab_3)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_23.addWidget(self.label_38)

        self.txt_obs = QLineEdit(self.tab_3)
        self.txt_obs.setObjectName(u"txt_obs")
        self.txt_obs.setMinimumSize(QSize(0, 40))
        self.txt_obs.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.verticalLayout_23.addWidget(self.txt_obs)


        self.verticalLayout_29.addLayout(self.verticalLayout_23)


        self.verticalLayout_30.addLayout(self.verticalLayout_29)


        self.verticalLayout_31.addLayout(self.verticalLayout_30)

        self.tw_dados_cliente.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_34 = QVBoxLayout(self.tab_4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.lineEdit = QLineEdit(self.tab_4)
        self.lineEdit.setObjectName(u"lineEdit")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        self.lineEdit.setFont(font5)
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.lineEdit)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.tw_os_pendente = QTableWidget(self.tab_4)
        if (self.tw_os_pendente.columnCount() < 9):
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
        self.tw_os_pendente.setObjectName(u"tw_os_pendente")

        self.horizontalLayout_24.addWidget(self.tw_os_pendente)

        self.btn_baixa_os = QPushButton(self.tab_4)
        self.btn_baixa_os.setObjectName(u"btn_baixa_os")
        self.btn_baixa_os.setMinimumSize(QSize(100, 25))
        self.btn_baixa_os.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_24.addWidget(self.btn_baixa_os)


        self.verticalLayout_32.addLayout(self.horizontalLayout_24)


        self.verticalLayout_33.addLayout(self.verticalLayout_32)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.tw_os_paga = QTableWidget(self.tab_4)
        if (self.tw_os_paga.columnCount() < 6):
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
        self.tw_os_paga.setObjectName(u"tw_os_paga")

        self.horizontalLayout_23.addWidget(self.tw_os_paga)

        self.btn_extorna_os = QPushButton(self.tab_4)
        self.btn_extorna_os.setObjectName(u"btn_extorna_os")
        self.btn_extorna_os.setMinimumSize(QSize(100, 25))
        self.btn_extorna_os.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_23.addWidget(self.btn_extorna_os)


        self.verticalLayout_33.addLayout(self.horizontalLayout_23)


        self.verticalLayout_34.addLayout(self.verticalLayout_33)

        self.tw_dados_cliente.addTab(self.tab_4, "")

        self.verticalLayout_17.addWidget(self.tw_dados_cliente)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.Pages.addWidget(self.pg_cadastro_cliente)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(0,80,121);")

        self.verticalLayout.addWidget(self.label)

        self.btn_pg_cadastro = QPushButton(self.pg_home)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setFont(font)
        self.btn_pg_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border- radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0,80,121);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fff; \n"
"color:black\n"
"}")

        self.verticalLayout.addWidget(self.btn_pg_cadastro)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro_usuario = QWidget()
        self.pg_cadastro_usuario.setObjectName(u"pg_cadastro_usuario")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastro_usuario)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.pg_cadastro_usuario)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"font: italic 28pt \"Caladea\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro_usuario)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"font: italic 28pt \"Caladea\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, -1, -1, -1)
        self.label_7 = QLabel(self.pg_cadastro_usuario)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro_usuario)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy5)
        self.txt_nome.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_5.addWidget(self.txt_nome)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(30, -1, -1, -1)
        self.label_8 = QLabel(self.pg_cadastro_usuario)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro_usuario)
        self.txt_usuario.setObjectName(u"txt_usuario")
        sizePolicy5.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy5)
        self.txt_usuario.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_6.addWidget(self.txt_usuario)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(30, -1, -1, -1)
        self.label_9 = QLabel(self.pg_cadastro_usuario)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha.setObjectName(u"txt_senha")
        sizePolicy5.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy5)
        self.txt_senha.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(30, -1, -1, -1)
        self.label_10 = QLabel(self.pg_cadastro_usuario)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro_usuario)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        sizePolicy5.setHeightForWidth(self.txt_senha_2.sizePolicy().hasHeightForWidth())
        self.txt_senha_2.setSizePolicy(sizePolicy5)
        self.txt_senha_2.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.txt_senha_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(30, -1, -1, -1)
        self.label_11 = QLabel(self.pg_cadastro_usuario)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro_usuario)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy6)
        font6 = QFont()
        font6.setFamilies([u"Trebucher Ms"])
        self.cb_perfil.setFont(font6)
        self.cb_perfil.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_perfil.setLayoutDirection(Qt.LeftToRight)
        self.cb_perfil.setStyleSheet(u"color:rgba(211,236,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius:None;\n"
"background-color:rgba(85,115,155,0.5);\n"
"font-family:Trebucher Ms;\n"
"font-size: 21px;")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro_usuario)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro_usuario)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro_usuario)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.Pages.addWidget(self.pg_cadastro_usuario)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_14 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.pg_contatos)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 75))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"font: italic 28pt \"Caladea\";")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_26 = QLabel(self.pg_contatos)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(50, 50))
        self.label_26.setPixmap(QPixmap(u"imagens/git_icone.png"))
        self.label_26.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_26)

        self.label_22 = QLabel(self.pg_contatos)
        self.label_22.setObjectName(u"label_22")
        font7 = QFont()
        font7.setPointSize(25)
        self.label_22.setFont(font7)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_22)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_27 = QLabel(self.pg_contatos)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(60, 50))
        self.label_27.setPixmap(QPixmap(u"imagens/whats_icone.png"))
        self.label_27.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_27)

        self.label_23 = QLabel(self.pg_contatos)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font7)
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_23)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_29 = QLabel(self.pg_contatos)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(50, 50))
        self.label_29.setPixmap(QPixmap(u"imagens/linkedin_icone.png"))
        self.label_29.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_29)

        self.label_25 = QLabel(self.pg_contatos)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font7)
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_25)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_28 = QLabel(self.pg_contatos)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(50, 50))
        self.label_28.setPixmap(QPixmap(u"imagens/gmail_icone.png"))
        self.label_28.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_28)

        self.label_24 = QLabel(self.pg_contatos)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font7)
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_24)


        self.verticalLayout_13.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_17.addLayout(self.verticalLayout_13)

        self.label_30 = QLabel(self.pg_contatos)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(250, 300))
        self.label_30.setPixmap(QPixmap(u"imagens/dream_TradingCard (2).jpg"))
        self.label_30.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_30)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_21 = QLabel(self.pg_sobre)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(100, 25))
        self.label_21.setMaximumSize(QSize(16777215, 50))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"font: italic 28pt \"Caladea\";")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_21)

        self.label_17 = QLabel(self.pg_sobre)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_12.addWidget(self.label_17)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_importar = QWidget()
        self.pg_importar.setObjectName(u"pg_importar")
        self.verticalLayout_10 = QVBoxLayout(self.pg_importar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_19 = QLabel(self.pg_importar)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"font: italic 28pt \"Caladea\";")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_19)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.txt_importar = QLineEdit(self.pg_importar)
        self.txt_importar.setObjectName(u"txt_importar")
        self.txt_importar.setMaximumSize(QSize(16777215, 31))
        self.txt_importar.setBaseSize(QSize(0, 30))
        self.txt_importar.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_importar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.txt_importar)

        self.btn_abrir_2 = QPushButton(self.pg_importar)
        self.btn_abrir_2.setObjectName(u"btn_abrir_2")
        self.btn_abrir_2.setMinimumSize(QSize(120, 31))
        self.btn_abrir_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_abrir_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-top-right-radius: 15px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_abrir_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.progressBar = QProgressBar(self.pg_importar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_10.addWidget(self.progressBar)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.pg_importar)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.btn_importarNFe = QPushButton(self.pg_importar)
        self.btn_importarNFe.setObjectName(u"btn_importarNFe")
        self.btn_importarNFe.setMinimumSize(QSize(0, 30))
        self.btn_importarNFe.setFont(font)
        self.btn_importarNFe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importarNFe.setStyleSheet(u"QPushButton{\n"
"	background-color: #fff; \n"
"	color:black;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 158, 231);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_importarNFe)

        self.label_5 = QLabel(self.pg_importar)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.Pages.addWidget(self.pg_importar)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tw_dados_cliente.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_os.setText(QCoreApplication.translate("MainWindow", u"OS", None))
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Entrada</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(14, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(13, QCoreApplication.translate("MainWindow", u"Data importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Valor produto", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Unidade medida", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Cod item", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Total NFe", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Emitente", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"CNPJ_Emitente", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Chave", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Data_emiss\u00e3o", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Saida</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"USUARIO", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"DATA IMPORTACAO", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"DATA SAIDA", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"NFCE", None));
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Saida", None))
        self.btn_extornar.setText(QCoreApplication.translate("MainWindow", u"Extorno", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline; color:#ffffff;\">TELA ESTOQUE</span></p></body></html>", None))
        self.txt_filtro.setText("")
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"GERAR GRAFICO", None))
        self.btn_exel.setText(QCoreApplication.translate("MainWindow", u"GERAR EXCEL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">DADOS DO CLIENTE</span></p></body></html>", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CPF</span></p></body></html>", None))
        self.txt_cpf_cliente_os.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.txt_cpf_cliente_os.setText(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.txt_cpf_cliente_os.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.000.000-0", None))
        self.btn_pesquisar_cliente_os.setText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CLIENTE</span></p></body></html>", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">RESPONSAVEL</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">DADOS DO PAGAMENTO</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">ARMA\u00c7\u00c3O</span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">R$</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">LENTES</span></p></body></html>", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">R$</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">OUTROS</span></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">R$</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">DESCONTO</span></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">R$</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">TOTAL</span></p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">R$</span></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">ENTRADA R$:</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">TIPO</span></p></body></html>", None))
        self.cb_tipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Debito", None))
        self.cb_tipo.setItemText(1, QCoreApplication.translate("MainWindow", u"PIX", None))
        self.cb_tipo.setItemText(2, QCoreApplication.translate("MainWindow", u"Dinheiro", None))

        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PAGAMENTO</span></p></body></html>", None))
        self.cb_pagamento.setItemText(0, QCoreApplication.translate("MainWindow", u"Cart\u00e3o", None))
        self.cb_pagamento.setItemText(1, QCoreApplication.translate("MainWindow", u"Carne", None))

        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">A PAGAR</span></p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">R$</span></p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">VENCIMENTO DIA: </span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.comboBox.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.comboBox.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.comboBox.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">O.S COMPLETA</span></p></body></html>", None))
        self.btn_gerar_os.setText(QCoreApplication.translate("MainWindow", u"GERAR O.S", None))
        self.label_68.setText("")
        self.btn_gerar_pdf_os.setText(QCoreApplication.translate("MainWindow", u"O.S EM PDF", None))
        self.label_69.setText("")
        self.btn_teste.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">DADOS ARMA\u00c7\u00c3O / LENTE</span></p></body></html>", None))
        self.btn_anexar_receita.setText(QCoreApplication.translate("MainWindow", u"Anexar Receita", None))
        self.ln_anexo_receita.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com o arquivo  -------->", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">COD.ARMA\u00c7\u00c3O</span></p></body></html>", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">TIPO DE LENTE</span></p></body></html>", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">EXAMINADOR</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"OS COMPLETA", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline; color:#ffffff;\">CLIENTES </span></p></body></html>", None))
        self.label_18.setText("")
        self.btn_pesquisar_cliente.setText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        self.btn_pesquisar_cliente_bd.setText(QCoreApplication.translate("MainWindow", u"PESQUISAR REGISTRO", None))
        self.btn_cadastrar_cliente.setText(QCoreApplication.translate("MainWindow", u"SALVAR CADASTRO", None))
        self.btn_editar_cliente.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CPF</span></p></body></html>", None))
        self.txt_cpf_cliente.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.txt_cpf_cliente.setText(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.txt_cpf_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.000.000-0", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">DATA DE NASCIMENTO</span></p></body></html>", None))
        self.txt_data_nasc.setInputMask(QCoreApplication.translate("MainWindow", u"00/00/0000", None))
        self.txt_data_nasc.setText(QCoreApplication.translate("MainWindow", u"01/01/0001", None))
        self.txt_data_nasc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dia /Mes /Ano", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">NOME</span></p></body></html>", None))
        self.txt_nome_cliente.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">RESPONSAVEL</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">E-MAIL</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">TELEFONE</span></p></body></html>", None))
        self.txt_tef1.setInputMask(QCoreApplication.translate("MainWindow", u"(00)00000-0000", None))
        self.txt_tef1.setText(QCoreApplication.translate("MainWindow", u"(00)00000-0000", None))
        self.txt_tef1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(00) 00000-0000", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">TELEFONE (2)</span></p></body></html>", None))
        self.txt_tef2.setInputMask(QCoreApplication.translate("MainWindow", u"(00)00000-0000", None))
        self.txt_tef2.setText(QCoreApplication.translate("MainWindow", u"(00)00000-0000", None))
        self.txt_tef2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(00) 00000-0000", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">ENDERE\u00c7O</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">N\u00ba</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CEP</span></p></body></html>", None))
        self.txt_cep.setInputMask(QCoreApplication.translate("MainWindow", u"00000-000", None))
        self.txt_cep.setText(QCoreApplication.translate("MainWindow", u"00000-000", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">OBSERVA\u00c7\u00c3O</span></p></body></html>", None))
        self.tw_dados_cliente.setTabText(self.tw_dados_cliente.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dados cliente", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FILTRO", None))
        ___qtablewidgetitem = self.tw_os_pendente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"OS", None));
        ___qtablewidgetitem1 = self.tw_os_pendente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7o", None));
        ___qtablewidgetitem2 = self.tw_os_pendente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem3 = self.tw_os_pendente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cod arma\u00e7\u00e3o", None));
        ___qtablewidgetitem4 = self.tw_os_pendente.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tipo de lente", None));
        ___qtablewidgetitem5 = self.tw_os_pendente.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data_emiss\u00e3o", None));
        ___qtablewidgetitem6 = self.tw_os_pendente.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None));
        ___qtablewidgetitem7 = self.tw_os_pendente.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        self.btn_baixa_os.setText(QCoreApplication.translate("MainWindow", u"BAIXA", None))
        ___qtablewidgetitem8 = self.tw_os_paga.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"OS", None));
        ___qtablewidgetitem9 = self.tw_os_paga.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem10 = self.tw_os_paga.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7o", None));
        ___qtablewidgetitem11 = self.tw_os_paga.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Data_emiss\u00e3o", None));
        ___qtablewidgetitem12 = self.tw_os_paga.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Data_baixa", None));
        ___qtablewidgetitem13 = self.tw_os_paga.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        self.btn_extorna_os.setText(QCoreApplication.translate("MainWindow", u"EXTORNO", None))
        self.tw_dados_cliente.setTabText(self.tw_dados_cliente.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Historico cliente", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;\">Sistema de gerenciamento</span><br/></p><p align=\"center\"><img src=\"D:/Projeto_Optica/imagens/logo_2optica.png\"/></p></body></html>", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar usuario", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Tela de cadastro</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"D:/Projeto_Optica/imagens/cadastro.png\"/></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Cadastrar usu\u00e1rio</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Nome: </span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha:  </span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha: </span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Perfil: </span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:normal; color:#ffffff;\">CONTATOS</span></p></body></html>", None))
        self.label_26.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/eduardocastro-dev\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Desenvolvedor: Eduardo Castro</span></a></p></body></html>", None))
        self.label_27.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">(19)99554-5996</span></p></body></html>", None))
        self.label_29.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://www.linkedin.com/in/eduardo-castro-138301187/\"><span style=\" font-size:16pt; text-decoration: underline; color:#ffffff;\">Eduardo-castro</span></a></p></body></html>", None))
        self.label_28.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">eduardocastro.technology@gmail.com</span></p></body></html>", None))
        self.label_30.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Sobre</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Este sistema tem como objetvos:</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">- Cadastro de usuarios e clientes</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">- Gera\u00e7\u00e3o de O.S</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">- Controle e baixa de vendas</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">- Importa\u00e7\u00e3o de XML\u00b4s</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;\">- Controle de estoque</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Importa\u00e7\u00e3o</span></p></body></html>", None))
        self.txt_importar.setText("")
        self.txt_importar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com os arquivos XML -------->", None))
        self.btn_abrir_2.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.label_4.setText("")
        self.btn_importarNFe.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.label_5.setText("")
    # retranslateUi

