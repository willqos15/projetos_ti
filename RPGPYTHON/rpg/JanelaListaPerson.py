from tkinter import *


def criarjlp():
    # ADCIONANDO NO BANCO DE DADOS

    jlistaperson = Toplevel()
    jlistaperson.title('Lista de Personagens')
    jlistaperson.geometry("1000x412+350+100")
    jlistaperson.resizable(0, 0)

    lbperson = Label(jlistaperson, text='Personagens', font="-weight bold -size 9")
    lbperson.grid(row=2, column=2, sticky=N)

    lbpesquisar = Label(jlistaperson, text='Pesquisar', font="-weight bold -size 9")
    lbpesquisar.grid(row=2, column=0, sticky=N)

    scrollbar = Scrollbar(jlistaperson)
    scrollbar.grid(row=3, column=3, sticky=N + S)  # (side=RIGHT, fill=Y)
    listbox = Listbox(jlistaperson, yscrollcommand=scrollbar.set, width=25, height=20)

    import pymysql

    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='ficha_bd')

    cursor = conexao.cursor()
    cursor.execute("SELECT char_nome FROM tbl_person")
    resultadonome = cursor.fetchall()
    for x in resultadonome:
        x = str(x)
        x = x.strip("(()")
        x = x.strip("(')")
        x = x.strip("(,)")
        x = x.strip("())")
        x = x.strip("(')")
        listbox.insert(END, x)
    listbox.grid(row=3, column=2, sticky=W + E, padx=10)
    scrollbar.config(command=listbox.yview)

    def selp():
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='ficha_bd')
        # nome
        cursor = conexao.cursor()
        teste_sqp = "SELECT char_nome FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        resultado = str(resultado)
        resultado = resultado.strip("(()")
        resultado = resultado.strip("(')")
        resultado = resultado.strip("(,)")
        resultado = resultado.strip("())")
        resultado = resultado.strip("(')")
        lbn.config(text=resultado)



        # sexo
        teste_sqp = "SELECT char_sexo FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbs.config(text=resultado)

        # raça
        teste_sqp = "SELECT char_raca FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbr.config(text=resultado)

        # classe
        teste_sqp = "SELECT char_classe FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbc.config(text=resultado)

        # vida
        teste_sqp = "SELECT char_vida FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbv.config(text=resultado)

        # forca
        teste_sqp = "SELECT char_for FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbf.config(text=resultado)

        # inteligência
        teste_sqp = "SELECT char_int FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbi.config(text=resultado)

        # carisma
        teste_sqp = "SELECT char_car FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbca.config(text=resultado)

        # constituição
        teste_sqp = "SELECT char_con FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbco.config(text=resultado)

        # sabedoria
        teste_sqp = "SELECT char_sab FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbsa.config(text=resultado)

        # destreza
        teste_sqp = "SELECT char_des FROM tbl_person WHERE char_nome = %s"
        xt = listbox.get(listbox.curselection())
        valorteste = (xt)
        cursor.execute(teste_sqp, valorteste)
        resultado = cursor.fetchall()
        lbd.config(text=resultado)

        # foto
        #HUMANO
        if (lbs['text']) == (('Masculino',),) and (lbr['text'])== (('Humano',),) and (lbc['text']) == (('Guerreiro',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhg.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text'])== (('Humano',),) and (lbc['text']) == (('Mago',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhm.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text'])== (('Humano',),) and (lbc['text']) == (('Ladino',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhl.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text'])== (('Humano',),) and (lbc['text']) == (('Druida',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhd.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text'])== (('Humano',),) and (lbc['text']) == (('Guerreiro',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhg.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text'])== (('Humano',),) and (lbc['text']) == (('Mago',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhm.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text'])== (('Humano',),) and (lbc['text']) == (('Ladino',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhl.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text'])== (('Humano',),) and (lbc['text']) == (('Druida',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhd.png")

        #ELFO
        if (lbs['text']) == (('Masculino',),) and (lbr['text']) == (('Elfo',),) and (lbc['text']) == (
        ('Guerreiro',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\meg.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text']) == (('Elfo',),) and (lbc['text']) == (('Mago',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mem.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text']) == (('Elfo',),) and (lbc['text']) == (('Ladino',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mel.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text']) == (('Elfo',),) and (lbc['text']) == (('Druida',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\med.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text']) == (('Elfo',),) and (lbc['text']) == (('Guerreiro',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\feg.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text']) == (('Elfo',),) and (lbc['text']) == (('Mago',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fem.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text']) == (('Elfo',),) and (lbc['text']) == (('Ladino',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fel.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text']) == (('Elfo',),) and (lbc['text']) == (('Druida',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fed.png")

        #ANÃO
        if (lbs['text']) == (('Masculino',),) and (lbr['text'])== (('Anão',),) and (lbc['text']) == (('Guerreiro',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhg.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text'])== (('Anão',),) and (lbc['text']) == (('Mago',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhm.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text'])== (('Anão',),) and (lbc['text']) == (('Ladino',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhl.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text'])== (('Anão',),) and (lbc['text']) == (('Druida',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhd.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text'])== (('Anão',),) and (lbc['text']) == (('Guerreiro',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhg.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text'])== (('Anão',),) and (lbc['text']) == (('Mago',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhm.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text'])== (('Anão',),) and (lbc['text']) == (('Ladino',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhl.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text'])== (('Anão',),) and (lbc['text']) == (('Druida',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhd.png")

        #ORC
        if (lbs['text']) == (('Masculino',),) and (lbr['text']) == (('Orc',),) and (lbc['text']) == (
        ('Guerreiro',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\meg.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text']) == (('Orc',),) and (lbc['text']) == (('Mago',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mom.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text']) == (('Orc',),) and (lbc['text']) == (('Ladino',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mol.png")

        if (lbs['text']) == (('Masculino',),) and (lbr['text']) == (('Orc',),) and (lbc['text']) == (('Druida',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mod.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text']) == (('Orc',),) and (lbc['text']) == (('Guerreiro',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fog.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text']) == (('Orc',),) and (lbc['text']) == (('Mago',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fom.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text']) == (('Orc',),) and (lbc['text']) == (('Ladino',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fol.png")

        if (lbs['text']) == (('Feminino',),) and (lbr['text']) == (('Orc',),) and (lbc['text']) == (('Druida',),):
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fod.png")


    # PESQUISADOR
    def sqlbusca():

        # TRATAMENTO DE NOME
        nomperson = ebnome.get()
        nomperson = nomperson.strip()  # tira espaço do começo e fim
        nomperson = nomperson.title()  # Maiuscula e Minuscula
        import re
        nomperson = re.sub("\s+", " ", nomperson)  # tira espaço extras no nomes
        snomperson = nomperson.replace(' ', '')  # tira todos espaços do meio

        if len(snomperson) == 0 and msexo.get() == 'Todos' and mraca.get() == 'Todas' and mclasse.get() == 'Todas':
            atualizar()
            lbn.config(text="Selecione um personagem!")
            lbs.config(text="Selecione um personagem!")
            lbr.config(text="Selecione um personagem!")
            lbc.config(text="Selecione um personagem!")
            lbv.config(text="Selecione um personagem!")
            lbf.config(text="Selecione um personagem!")
            lbi.config(text="Selecione um personagem!")
            lbca.config(text="Selecione um personagem!")
            lbco.config(text="Selecione um personagem!")
            lbsa.config(text="Selecione um personagem!")
            lbd.config(text="Selecione um personagem!")

        elif len(snomperson) >= 1 and msexo.get() == 'Todos' and mraca.get() == 'Todas' and mclasse.get() == 'Todas':
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='123456',
                database='ficha_bd')
            listbox.delete(0, END)
            cursor = conexao.cursor()
            cursor.execute("SELECT char_nome FROM tbl_person WHERE char_nome LIKE '%s%%'" % nomperson)
            resultadonome = cursor.fetchall()
            for x in resultadonome:
                x = str(x)
                x = x.strip("(()")
                x = x.strip("(')")
                x = x.strip("(,)")
                x = x.strip("())")
                x = x.strip("(')")
                listbox.insert(END, x)

        else:

            listabusca = []
            comando = "SELECT char_nome FROM tbl_person WHERE"
            if msexo.get() != 'Todos':
                comando += ' char_sexo = %s'
                listabusca.append(msexo.get())
                if mraca.get() != 'Todas':
                    comando += ' AND char_raca = %s'
                    listabusca.append(mraca.get())
                if mclasse.get() != 'Todas':
                    comando += ' AND char_classe = %s'
                    listabusca.append(mclasse.get())

            elif mraca.get() != 'Todas':
                comando += ' char_raca = %s'
                listabusca.append(mraca.get())
                if msexo.get() != 'Todos':
                    comando += ' char_sexo = %s'
                    listabusca.append(msexo.get())
                if mclasse.get() != 'Todas':
                    comando += ' AND char_classe = %s'
                    listabusca.append(mclasse.get())

            elif mclasse.get() != 'Todas':
                comando += ' char_classe = %s'
                listabusca.append(mclasse.get())
                if mraca.get() != 'Todas':
                    comando += ' AND char_raca = %s'
                    listabusca.append(mraca.get())
                if msexo.get() != 'Todos':
                    comando += ' AND char_sexo = %s'
                    listabusca.append(msexo.get())

            if len(snomperson) >= 1 and mclasse.get() != 'Todas' or mraca.get() != 'Todas' or msexo.get() != 'Todas':
                comando += (" AND char_nome LIKE %s ")
                listabusca.append((nomperson + '%',))

            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='123456',
                database='ficha_bd')
            listbox.delete(0, END)
            cursor = conexao.cursor()
            valorteste = (listabusca)
            cursor.execute(comando, (valorteste))
            resultadosexo = cursor.fetchall()
            for x in resultadosexo:
                x = str(x)
                x = x.strip("(()")
                x = x.strip("(')")
                x = x.strip("(,)")
                x = x.strip("())")
                x = x.strip("(')")
                listbox.insert(END, x)

        lbaviso.config(text="")

    framepesquisa = Frame(jlistaperson, width=30, height=200)
    framepesquisa.grid(row=3, column=0, rowspan=3, sticky=N + S, padx=20, pady=10)

    pesquisar = Button(framepesquisa, text='Pesquisar', relief=RAISED, command=sqlbusca)
    pesquisar.grid(row=10, column=2, columnspan=2, ipadx=90, pady=10)

    lbbuscanome = Label(framepesquisa, text='Buscar por nome: ')
    lbbuscanome.grid(row=1, column=2, sticky=W)
    ebnome = Entry(framepesquisa)
    ebnome.grid(row=1, column=3, sticky=W + E)

    lbbuscasexo = Label(framepesquisa, text='Buscar por Sexo: ')
    lbbuscasexo.grid(row=2, column=2, sticky=W)
    msexo = StringVar(framepesquisa)
    msexo.set('Todos')
    z = OptionMenu(framepesquisa, msexo, 'Todos', 'Masculino', 'Feminino')
    z.grid(row=2, column=3, sticky=W)

    lbbuscaraca = Label(framepesquisa, text='Buscar por Raça: ')
    lbbuscaraca.grid(row=3, column=2, sticky=W)
    mraca = StringVar(framepesquisa)
    mraca.set('Todas')
    z = OptionMenu(framepesquisa, mraca, 'Todas', 'Humano', 'Elfo', 'Anão', 'Orc')
    z.grid(row=3, column=3, sticky=W)

    lbbuscaclasse = Label(framepesquisa, text='Buscar por Classe: ')
    lbbuscaclasse.grid(row=4, column=2, sticky=W)
    mclasse = StringVar(framepesquisa)
    mclasse.set('Todas')
    z = OptionMenu(framepesquisa, mclasse, 'Todas', 'Guerreiro', 'Mago', 'Ladino', 'Druida')
    z.grid(row=4, column=3, sticky=W)

    # DADOS
    frameficha = Frame(jlistaperson, width=30, height=200, bd=4, relief=RAISED)
    frameficha.grid(row=2, column=7, rowspan=2, sticky=N + S, padx=20, pady=10)

    lbficha = Button(frameficha, text='FICHA DO PERSONAGEM', font="-weight bold -size 9", relief=SUNKEN)
    lbficha.grid(row=1, column=1, columnspan=2, sticky=W + E)

    lbnome = Button(frameficha, text='Nome:', font="-weight bold -size 9", relief=SUNKEN)
    lbnome.grid(row=2, column=1, columnspan=1, sticky=W + E)
    lbn = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbn.grid(row=2, column=2, columnspan=1, sticky=W + E)

    lbsexo = Button(frameficha, text='Sexo:', font="-weight bold -size 9", relief=SUNKEN)
    lbsexo.grid(row=3, column=1, columnspan=1, sticky=W + E)
    lbs = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbs.grid(row=3, column=2, columnspan=1, sticky=W + E)

    lbraca = Button(frameficha, text='Raça:', font="-weight bold -size 9", relief=SUNKEN)
    lbraca.grid(row=4, column=1, columnspan=1, sticky=W + E)
    lbr = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbr.grid(row=4, column=2, columnspan=1, sticky=W + E)

    lbclasse = Button(frameficha, text='Classe:', font="-weight bold -size 9", relief=SUNKEN)
    lbclasse.grid(row=5, column=1, columnspan=1, sticky=W + E)
    lbc = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbc.grid(row=5, column=2, columnspan=1, sticky=W + E)

    lbvida = Button(frameficha, text='Pontos de Vida:', font="-weight bold -size 9", relief=SUNKEN)
    lbvida.grid(row=6, column=1, columnspan=1, sticky=W + E)
    lbv = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbv.grid(row=6, column=2, columnspan=1, sticky=W + E)

    lbfor = Button(frameficha, text='Força:', font="-weight bold -size 9", relief=SUNKEN)
    lbfor.grid(row=7, column=1, columnspan=1, sticky=W + E)
    lbf = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbf.grid(row=7, column=2, columnspan=1, sticky=W + E)

    lbint = Button(frameficha, text='Inteligência:', font="-weight bold -size 9", relief=SUNKEN)
    lbint.grid(row=8, column=1, columnspan=1, sticky=W + E)
    lbi = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbi.grid(row=8, column=2, columnspan=1, sticky=W + E)

    lbcar = Button(frameficha, text='Carisma:', font="-weight bold -size 9", relief=SUNKEN)
    lbcar.grid(row=9, column=1, columnspan=1, sticky=W + E)
    lbca = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbca.grid(row=9, column=2, columnspan=1, sticky=W + E)

    lbcon = Button(frameficha, text='Constituição:', font="-weight bold -size 9", relief=SUNKEN)
    lbcon.grid(row=10, column=1, columnspan=1, sticky=W + E)
    lbco = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbco.grid(row=10, column=2, columnspan=1, sticky=W + E)

    lbsab = Button(frameficha, text='Sabedoria:', font="-weight bold -size 9", relief=SUNKEN)
    lbsab.grid(row=11, column=1, columnspan=1, sticky=W + E)
    lbsa = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbsa.grid(row=11, column=2, columnspan=1, sticky=W + E)

    lbdes = Button(frameficha, text='Destreza:', font="-weight bold -size 9", relief=SUNKEN)
    lbdes.grid(row=12, column=1, columnspan=1, sticky=W + E)
    lbd = Button(frameficha, text="Selecione um personagem!", relief=SUNKEN)
    lbd.grid(row=12, column=2, columnspan=1, sticky=W + E)

    ffchar = Frame(jlistaperson, highlightbackground='gray', highlightthickness=3)
    ffchar.grid(row=3, column=9, rowspan=6, sticky=N)
    imagechar = PhotoImage(file="")

    canvas = Canvas(ffchar, width=185, height=165)
    canvas.pack()
    canvas.create_image(20, 20, anchor=NW, image=imagechar)

    def atualizar():
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='ficha_bd')
        listbox.delete(0, END)
        cursor = conexao.cursor()
        cursor.execute("SELECT char_nome FROM tbl_person")
        resultadonome = cursor.fetchall()
        for x in resultadonome:
            x = str(x)
            x = x.strip("(()")
            x = x.strip("(')")
            x = x.strip("(,)")
            x = x.strip("())")
            x = x.strip("(')")
            listbox.insert(END, x)

    def cmdexcluir():
        if (lbn['text']) != "Selecione um personagem!":
            lbaviso.config(text='')

            def defsim():
                cursor = conexao.cursor()
                teste_sqp = "DELETE FROM tbl_person WHERE char_nome = %s"
                xt = (lbn['text'])
                valorteste = (xt)
                cursor.execute(teste_sqp, valorteste)
                nomeperson = lbn['text']
                lbaviso.config(text='O(a) personagem %s foi apagado(a) com Sucesso!' % (nomeperson))
                lbaviso['fg'] = 'green'
                conexao.commit()

                atualizar()
                lbn.config(text="Selecione um personagem!")
                lbs.config(text="Selecione um personagem!")
                lbr.config(text="Selecione um personagem!")
                lbc.config(text="Selecione um personagem!")
                lbv.config(text="Selecione um personagem!")
                lbf.config(text="Selecione um personagem!")
                lbi.config(text="Selecione um personagem!")
                lbca.config(text="Selecione um personagem!")
                lbco.config(text="Selecione um personagem!")
                lbsa.config(text="Selecione um personagem!")
                lbd.config(text="Selecione um personagem!")

                confirmarapagar.destroy()
                jlistaperson.wm_attributes('-topmost', True)
                jlistaperson.wm_attributes("-disabled", False)

            def defnao():
                confirmarapagar.destroy()
                jlistaperson.wm_attributes('-topmost', True)
                jlistaperson.wm_attributes("-disabled", False)

            confirmarapagar = Toplevel()
            confirmarapagar.title("Confirmar")
            confirmarapagar.geometry("246x100+590+300")
            confirmarapagar.resizable(0, 0)
            confirmarapagar.protocol('WM_DELETE_WINDOW', defnao)
            confirmarapagar.wm_attributes('-topmost', True)
            jlistaperson.wm_attributes("-disabled", True)

            labelapagar = Label(confirmarapagar, text="Deseja mesmo apagar esse personagem?")
            labelapagar.grid(row=0, column=1, columnspan=2, sticky=EW, ipadx=10, ipady=10)
            bsim = Button(confirmarapagar, text="Sim", command=defsim)
            bsim.grid(row=1, column=1, sticky=E, ipadx=5, pady=10)
            bnao = Button(confirmarapagar, text="Não", command=defnao)
            bnao.grid(row=1, column=2, sticky=W, ipadx=5, pady=10)

        else:
            lbaviso.config(text="Para apagar selecione um Personagem!")
            lbaviso['fg'] = 'red'

    def altnome():
        if (lbn['text']) != "Selecione um personagem!":
            lbaviso.config(text='')

            def confnome():

                # TRATAMENTO DE NOME
                novonome = entryalt.get()
                novonome = novonome.strip()  # tira espaço do começo e fim
                novonome = novonome.title()  # Maiuscula e Minuscula
                import re
                novonome = re.sub("\s+", " ", novonome)  # tira espaço extras no nomes
                snovonome = novonome.replace(' ', '')  # tira todos espaços do meio

                if snovonome.isalpha() == True and len(snovonome) <= 1:
                    lbnomeaviso.config(text='Insira um nome com mais de uma letra!')
                    lbnomeaviso['fg'] = 'red'

                elif snovonome.isalpha() == True and len(snovonome) > 20:
                    lbnomeaviso.config(text='Insira um nome menos de 20 letras!')
                    lbnomeaviso['fg'] = 'red'

                elif snovonome.isalpha() == False and len(snovonome) > 1:
                    lbnomeaviso.config(text='Insira usando somente letras!')
                    lbnomeaviso['fg'] = 'red'

                elif snovonome.isalpha() == True and len(snovonome) > 1:
                    import pymysql
                    conexao = pymysql.connect(
                        host='localhost',
                        user='root',
                        passwd='',
                        database='ficha_bd'
                    )
                    cursor = conexao.cursor()
                    teste_sqp = "SELECT * FROM tbl_person WHERE char_nome = %s"
                    cursor.execute(teste_sqp, novonome)
                    resultado = cursor.fetchall()
                    nomerepetido = 0
                    for x in resultado:

                        if len(x) >= 1:
                            nomerepetido += 1

                        else:
                            pass

                    if nomerepetido == 0:
                        conexao = pymysql.connect(
                            host='localhost',
                            user='root',
                            passwd='',
                            database='ficha_bd'
                        )
                        cursor = conexao.cursor()
                        teste_sqp = "UPDATE tbl_person SET char_nome = %s WHERE char_nome= %s"
                        nomeperson = lbn['text']
                        cursor.execute(teste_sqp, (novonome, nomeperson))
                        conexao.commit()

                        lbaviso.config(
                            text='O nome do personagem %s foi alterado para com %s!' % (nomeperson, novonome))
                        lbaviso['fg'] = 'green'
                        alterarn.destroy()
                        jlistaperson.wm_attributes('-topmost', True)
                        jlistaperson.wm_attributes("-disabled", False)
                        lbn.config(text=novonome)
                        atualizar()

                    if nomerepetido >= 1:
                        lbnomeaviso.config(text='Já existe um personagem com esse nome!')
                        lbnomeaviso['fg'] = 'red'


                else:
                    lbnomeaviso.config(text='Insira um nome com mais de um digito \nusando somente letras!')
                    lbnomeaviso['fg'] = 'red'

            def nao():
                alterarn.destroy()
                jlistaperson.wm_attributes('-topmost', True)
                jlistaperson.wm_attributes("-disabled", False)

            alterarn = Toplevel()
            alterarn.title("Alterar Nome")
            alterarn.geometry("265x106+590+300")
            alterarn.resizable(0, 0)
            alterarn.protocol('WM_DELETE_WINDOW', nao)
            alterarn.wm_attributes('-topmost', True)
            jlistaperson.wm_attributes("-disabled", True)
            labelalt = Label(alterarn, text="Insira o novo nome:")
            labelalt.grid(row=1, column=1, sticky=E, ipadx=5, pady=10)
            entryalt = Entry(alterarn)
            entryalt.grid(row=1, column=2, sticky=W, ipadx=1, pady=10, padx=1)
            btconfirmar = Button(alterarn, text="Confirmar", command=confnome)
            btconfirmar.grid(row=2, column=1, columnspan=2, ipadx=5)
            lbnomeaviso = Label(alterarn, text="")
            lbnomeaviso.grid(row=3, column=1, columnspan=2, ipadx=5)
        else:
            lbaviso.config(text="Para alterar nome selecione um Personagem!")
            lbaviso['fg'] = 'red'
        pass

    framebotoes = Frame(jlistaperson)
    framebotoes.grid(row=4, column=7, columnspan=2)

    Bsele = Button(jlistaperson, text='Selecionar', command=selp)
    Bsele.grid(row=4, column=2, pady=5)

    bmnome = Button(framebotoes, text='Alterar Nome', command=altnome)
    bmnome.grid(row=1, column=1, padx=5)

    bexcluir = Button(framebotoes, text='Excluir Ficha', command=cmdexcluir)
    bexcluir.grid(row=1, column=2)

    lbaviso = Label(jlistaperson, text='')
    lbaviso.grid(row=11, column=1, columnspan=7, sticky=W)
    
    
    # DADOS ESTATISTICA
    def estatistica():

        # Def Gráficos
        def g_sexo():
            fgsexo.pack_forget()
            fgraca.pack_forget()
            fgclasse.pack_forget()
            fgracaclasse.pack_forget()
            fgsexo.pack(side=TOP)
            bsexo['relief'] = 'sunken'
            braca['relief'] = 'raised'
            bclasse['relief'] = 'raised'
            bclasseraca['relief'] = 'raised'

        def g_raca():
            fgsexo.pack_forget()
            fgraca.pack_forget()
            fgclasse.pack_forget()
            fgracaclasse.pack_forget()
            fgraca.pack(side=TOP)
            braca['relief'] = 'sunken'
            bsexo['relief'] = 'raised'
            bclasse['relief'] = 'raised'
            bclasseraca['relief'] = 'raised'

        def g_classe():
            fgsexo.pack_forget()
            fgraca.pack_forget()
            fgclasse.pack_forget()
            fgracaclasse.pack_forget()
            fgclasse.pack(side=TOP)
            bclasse['relief'] = 'sunken'
            bsexo['relief'] = 'raised'
            braca['relief'] = 'raised'
            bclasseraca['relief'] = 'raised'

        def g_racaclasse():
            fgsexo.pack_forget()
            fgraca.pack_forget()
            fgclasse.pack_forget()
            fgracaclasse.pack_forget()
            fgracaclasse.pack(side=TOP)
            bclasseraca['relief'] = 'sunken'
            bsexo['relief'] = 'raised'
            braca['relief'] = 'raised'
            bclasse['relief'] = 'raised'

        # Janela
        jestatistica = Toplevel()
        jestatistica.title('Dados')
        jestatistica.geometry("920x500+350+100")
        ftopo = Frame(jestatistica)
        ftopo.pack(side=TOP)  # grid(row=1,column=2, padx=10, pady=20)
        lcategoria = Label(ftopo, text='Categoria:', font="-weight bold -size 15")
        lcategoria.grid(row=1, column=1, pady=20)
        bsexo = Button(ftopo, text='Sexo', command=g_sexo)
        bsexo.grid(row=1, column=2, padx=5)
        braca = Button(ftopo, text='Raça', command=g_raca)
        braca.grid(row=1, column=3, padx=5)
        bclasse = Button(ftopo, text='Classe', command=g_classe)
        bclasse.grid(row=1, column=4, padx=5)
        bclasseraca = Button(ftopo, text='Classe/Raça', command=g_racaclasse)
        bclasseraca.grid(row=1, column=5, padx=5)

        # Gráfico
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='ficha_bd')
        cursor = conexao.cursor()

        # GRAFICO SEXO --------------------------------------------------------------------------------------------------

        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_sexo = %s"
        valor = ('Masculino')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdsm = resultadox

        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_sexo = %s"
        valor = ('Feminino')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdsf = resultadox

        label_listasexo = ['Masculino', 'Feminino']

        if qtdsm == 0:
            label_listasexo[0] = ''

        if qtdsf == 0:
            label_listasexo[1] = ''

        # Formatação legenda porcentagens raça
        psm = ('%d (%s%%) %s' % (
            qtdsm, ("{0:.2f}".format(round((100 * qtdsm / (qtdsm + qtdsf)), 2))), 'Masculino'))
        psf = ('%d (%s%%) %s' % (
            qtdsf, ("{0:.2f}".format(round((100 * qtdsf / (qtdsm + qtdsf)), 2))), 'Feminino'))

        fig1 = plt.figure(figsize=(8.5, 4))
        plt.subplot(1, 2, 1)
        plt.pie((qtdsm, qtdsf), labels=(label_listasexo),
                colors=('Dodgerblue', 'DeepPink'))
        plt.title('Sexo\n')
        plt.axis('equal')
        plt.rcParams['legend.fontsize'] = 9
        plt.legend([psm, psf],
                   loc='lower left', bbox_to_anchor=(1.5, 0))
        fgsexo = Frame(jestatistica, borderwidth=1, relief='solid')
        fgsexo.pack(side=TOP)  # grid(row=2,column=2, padx=10)

        canvas = FigureCanvasTkAgg(fig1, master=fgsexo)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

        # GRAFICO RAÇA --------------------------------------------------------------------------------------------------
        # Humano
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s"
        valor = ('Humano')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdh = resultadox

        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s"
        valor = ('Elfo')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtde = resultadox

        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s"
        valor = ('Anão')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtda = resultadox

        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s"
        valor = ('Orc')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdo = resultadox

        xlista = (qtdh, qtde, qtda, qtdo)
        label_listaraca = ['Humano', 'Elfo', 'Anão ', 'Orc']
        if qtdh == 0:
            label_listaraca[0] = ''
        if qtde == 0:
            label_listaraca[1] = ''
        if qtda == 0:
            label_listaraca[2] = ''
        if qtdo == 0:
            label_listaraca[3] = ''
        cores = ('blue', 'lime', 'yellow', 'red')

        # Formatação legenda porcentagens raça
        ph = ('%d (%s%%) %s' % (
            qtdh, ("{0:.2f}".format(round((100 * qtdh / sum(xlista)), 2))), 'Humano'))
        pe = (
            '%d (%s%%) %s' % (
                qtde, ("{0:.2f}".format(round((100 * qtde / sum(xlista)), 2))), 'Elfo'))
        pa = ('%d (%s%%) %s' % (
            qtda, ("{0:.2f}".format(round((100 * qtda / sum(xlista)), 2))), 'Anão'))
        po = ('%d (%s%%) %s' % (
            qtdo, ("{0:.2f}".format(round((100 * qtdo / sum(xlista)), 2))), 'Orc'))

        fig1 = plt.figure(figsize=(8.5, 4))
        plt.subplot(1, 2, 1)
        plt.pie(xlista, labels=(label_listaraca), colors=cores)
        plt.title('Raça\n')
        plt.axis('equal')
        plt.rcParams['legend.fontsize'] = 9
        plt.legend([ph, pe, pa, po],
                   loc='lower left', bbox_to_anchor=(1.5, 0))
        fgraca = Frame(jestatistica, borderwidth=1, relief='solid')
        fgraca.pack(side=TOP)  # grid(row=2,column=2, padx=10)

        canvas = FigureCanvasTkAgg(fig1, master=fgraca)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

        # GRAFICO CLASSE --------------------------------------------------------------------------------------------------
        # Humano
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_classe = %s"
        valor = ('Guerreiro')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdg = resultadox

        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_classe = %s"
        valor = ('Mago')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdm = resultadox

        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_classe = %s"
        valor = ('Ladino')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdl = resultadox

        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_classe = %s"
        valor = ('Druida')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdd = resultadox

        xlista = (qtdg, qtdm, qtdl, qtdd)
        label_listaclasse = ['Guerreiro', 'Mago', 'Ladino', 'Druida']
        if qtdg == 0:
            label_listaclasse[0] = ''
        if qtdm == 0:
            label_listaclasse[1] = ''
        if qtdl == 0:
            label_listaclasse[2] = ''
        if qtdd == 0:
            label_listaclasse[3] = ''

        # Formatação legenda porcentagens classe
        pg = ('%d (%s%%) %s' % (
            qtdg, ("{0:.2f}".format(round((100 * qtdg / sum(xlista)), 2))), 'Guerreiro'))
        pm = ('%d (%s%%) %s' % (
            qtde, ("{0:.2f}".format(round((100 * qtdm / sum(xlista)), 2))), 'Mago'))
        pl = ('%d (%s%%) %s' % (
            qtdl, ("{0:.2f}".format(round((100 * qtdl / sum(xlista)), 2))), 'Ladino'))
        pd = ('%d (%s%%) %s' % (
            qtdd, ("{0:.2f}".format(round((100 * qtdd / sum(xlista)), 2))), 'Druida'))

        fig1 = plt.figure(figsize=(8.5, 4))
        plt.subplot(1, 2, 1)
        plt.pie(xlista, labels=label_listaclasse, colors=('red', 'blue', 'yellow', 'lime'))
        plt.title('Classe\n')
        plt.axis('equal')
        plt.rcParams['legend.fontsize'] = 9
        plt.legend([pg, pm, pl, pd],
                   loc='lower left', bbox_to_anchor=(1.5, 0))
        fgclasse = Frame(jestatistica, borderwidth=1, relief='solid')
        fgclasse.pack(side=TOP)  # grid(row=2,column=2, padx=10)

        canvas = FigureCanvasTkAgg(fig1, master=fgclasse)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

        # GRAFICO RAÇA CLASSE ------------------------------------------------------------------------------------------
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Humano', 'Guerreiro')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdhguerreiro = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Humano', 'Mago')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdhmago = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Humano', 'Ladino')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdhladino = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Humano', 'Druida')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdhdruida = resultadox

        # Elfo
        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Elfo', 'Guerreiro')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdeguerreiro = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Elfo', 'Mago')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdemago = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Elfo', 'Ladino')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdeladino = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Elfo', 'Druida')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdedruida = resultadox

        # Anão
        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Anão', 'Guerreiro')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdaguerreiro = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Anão', 'Mago')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdamago = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Anão', 'Ladino')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdaladino = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Anão', 'Druida')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdadruida = resultadox

        # Orc
        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Orc', 'Guerreiro')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdoguerreiro = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Orc', 'Mago')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdomago = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Orc', 'Ladino')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdoladino = resultadox

        cursor = conexao.cursor()
        com_sql = "SELECT COUNT(*) FROM tbl_person WHERE char_raca = %s AND char_classe = %s"
        valor = ('Orc', 'Druida')
        cursor.execute(com_sql, valor)
        resultadox = cursor.fetchall()
        resultadox = str(resultadox)
        resultadox = resultadox.strip("(()")
        resultadox = resultadox.strip("(,)")
        resultadox = resultadox.strip("())")
        resultadox = resultadox.strip("(,)")
        resultadox = int(resultadox)
        qtdodruida = resultadox

        xlista = [qtdhguerreiro, qtdhmago, qtdhladino, qtdhdruida, qtdeguerreiro, qtdemago, qtdeladino, qtdedruida,
                  qtdaguerreiro, qtdamago, qtdaladino, qtdadruida, qtdoguerreiro, qtdomago, qtdoladino, qtdodruida]
        label_listarc = ['Humano Guerreiro', 'Humano Mago', 'Humano Ladino', 'Humano Druida', 'Elfo Guerreiro',
                         'Elfo Mago', 'Elfo Ladino', 'Elfo Druida', 'Anão Guerreiro', 'Anão Mago', 'Anão Ladino',
                         'Anão Druida', 'Orc Guerreiro', 'Orc Mago', 'Orc Ladino', 'Orc Druida']

        for i in label_listarc:
            valor = label_listarc.index(i)
            if xlista[valor] == 0:
                label_listarc[valor] = ''

        cores = ('blue', 'darkblue', 'darkslateblue', 'slateblue', 'lime', 'green', 'lightgreen', 'seagreen',
                 'yellow', 'orange', 'goldenrod', 'peru', 'red', 'tomato', 'brown', 'darkred')

        # Formatação legenda porcentagens raça/classe
        phg = ('%d (%s%%) %s' % (
            qtdhguerreiro, ("{0:.2f}".format(round((100 * qtdhguerreiro / sum(xlista)), 2))), 'Humano Guerreiro'))
        phm = (
            '%d (%s%%) %s' % (qtdhmago, ("{0:.2f}".format(round((100 * qtdhmago / sum(xlista)), 2))), 'Humano Mago'))
        phl = ('%d (%s%%) %s' % (
            qtdhladino, ("{0:.2f}".format(round((100 * qtdhladino / sum(xlista)), 2))), 'Humano Ladino'))
        phd = ('%d (%s%%) %s' % (
            qtdhdruida, ("{0:.2f}".format(round((100 * qtdhdruida / sum(xlista)), 2))), 'Humano Druida'))
        peg = ('%d (%s%%) %s' % (
            qtdeguerreiro, ("{0:.2f}".format(round((100 * qtdeguerreiro / sum(xlista)), 2))), 'Elfo Guerreiro'))
        pem = (
            '%d (%s%%) %s' % (qtdemago, ("{0:.2f}".format(round((100 * qtdemago / sum(xlista)), 2))), 'Elfo Mago'))
        pel = ('%d (%s%%) %s' % (
            qtdeladino, ("{0:.2f}".format(round((100 * qtdeladino / sum(xlista)), 2))), 'Elfo Ladino'))
        ped = ('%d (%s%%) %s' % (
            qtdedruida, ("{0:.2f}".format(round((100 * qtdedruida / sum(xlista)), 2))), 'Elfo Druida'))
        pag = ('%d (%s%%) %s' % (
            qtdaguerreiro, ("{0:.2f}".format(round((100 * qtdaguerreiro / sum(xlista)), 2))), 'Anão Guerreiro'))
        pam = (
            '%d (%s%%) %s' % (qtdamago, ("{0:.2f}".format(round((100 * qtdamago / sum(xlista)), 2))), 'Anão Mago'))
        pal = ('%d (%s%%) %s' % (
            qtdaladino, ("{0:.2f}".format(round((100 * qtdaladino / sum(xlista)), 2))), 'Anão Ladino'))
        pad = ('%d (%s%%) %s' % (
            qtdadruida, ("{0:.2f}".format(round((100 * qtdadruida / sum(xlista)), 2))), 'Anão Druida'))
        pog = ('%d (%s%%) %s' % (
            qtdoguerreiro, ("{0:.2f}".format(round((100 * qtdoguerreiro / sum(xlista)), 2))), 'Orc Guerreiro'))
        pom = (
            '%d (%s%%) %s' % (
                qtdomago, ("{0:.2f}".format(round((100 * qtdomago / sum(xlista)), 2))), 'Orc Mago'))
        pol = ('%d (%s%%) %s' % (
            qtdoladino, ("{0:.2f}".format(round((100 * qtdoladino / sum(xlista)), 2))), 'Orc Ladino'))
        pod = ('%d (%s%%) %s' % (
            qtdodruida, ("{0:.2f}".format(round((100 * qtdodruida / sum(xlista)), 2))), 'Orc Druida'))

        fig1 = plt.figure(figsize=(9, 4))
        plt.subplot(1, 2, 1)
        plt.pie(xlista, labels=label_listarc, colors=cores)
        plt.title('Raça/Classe\n')
        plt.axis('equal')
        plt.rcParams['legend.fontsize'] = 9

        plt.legend([phg, phm, phl, phd, peg, pem, pel, ped, pag, pam, pal, pad, pog, pom, pol, pod],
                   loc='lower left', bbox_to_anchor=(1.5, 0))
        fgracaclasse = Frame(jestatistica, borderwidth=1, relief='solid')
        fgracaclasse.pack(side=TOP)  # grid(row=2,column=2, padx=10)
        canvas = FigureCanvasTkAgg(fig1, master=fgracaclasse)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

        g_sexo()

    bestatistica = Button(jlistaperson, text='Dados Estatisticos', command=estatistica)
    bestatistica.grid(row=4, column=0)

    mainloop()
