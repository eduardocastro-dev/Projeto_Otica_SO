    def grafico_estoque(self):
        cnx = sqlite3.connect("system.db")
        estoque = pd.read_sql_query("SELECT * FROM Notas", cnx)
        saida = pd.read_sql_query(
            "SELECT * FROM Notas WHERE NOT data_saida IS NULL", cnx
        )

        estoque = len(estoque)
        saida = len(saida)

        total = estoque + saida

        porcentagem_estoque = estoque / total * 100
        porcentagem_saida = saida / total * 100

        sizes = [porcentagem_estoque, porcentagem_saida]

        labels = ["Estoque", "Saídas"]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
        ax1.axis("equal")

        plt.show()