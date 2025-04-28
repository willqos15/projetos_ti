from tkinter import *  # Biblioteca Interface
from random import randint  # Biblioteca Random

valorh = int(0)
contador = 0


def criarjc():

    def bconfirmar():
        pvida = 0

        # IMAGEM CHAR MASCULINO
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\m.png")

        # IMAGEM CHAR FEMININO
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\f.png")

        # IMAGEM CHAR MASCULINO CLASSES
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Guerreiro' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mg.png")
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Mago' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mm.png")
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Ladino' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\ml.png")
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Druida' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\md.png")

        # IMAGEM CHAR FEMININO CLASSES
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Guerreiro' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fg.png")
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Mago' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fm.png")
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Ladino' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fl.png")
        if mraca.get() == 'Escolha uma raça' and mclasse.get() == 'Druida' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fd.png")

        # IMAGEM CHAR MASCULINO HUMANO
        if mraca.get() == 'Humano' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mh.png")

        if mraca.get() == 'Humano' and mclasse.get() == 'Guerreiro' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhg.png")

        if mraca.get() == 'Humano' and mclasse.get() == 'Mago' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhm.png")

        if mraca.get() == 'Humano' and mclasse.get() == 'Ladino' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhl.png")

        if mraca.get() == 'Humano' and mclasse.get() == 'Druida' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhd.png")

        # IMAGEM CHAR FEMININO HUMANO
        if mraca.get() == 'Humano' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fh.png")

        if mraca.get() == 'Humano' and mclasse.get() == 'Guerreiro' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhg.png")

        if mraca.get() == 'Humano' and mclasse.get() == 'Mago' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhm.png")

        if mraca.get() == 'Humano' and mclasse.get() == 'Ladino' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhl.png")

        if mraca.get() == 'Humano' and mclasse.get() == 'Druida' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhd.png")

        # IMAGEM CHAR MASCULINO ELFO
        if mraca.get() == 'Elfo' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\me.png")

        if mraca.get() == 'Elfo' and mclasse.get() == 'Guerreiro' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\meg.png")

        if mraca.get() == 'Elfo' and mclasse.get() == 'Mago' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mem.png")

        if mraca.get() == 'Elfo' and mclasse.get() == 'Ladino' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mel.png")

        if mraca.get() == 'Elfo' and mclasse.get() == 'Druida' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\med.png")

        # IMAGEM CHAR FEMININO ELFO
        if mraca.get() == 'Elfo' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fe.png")

        if mraca.get() == 'Elfo' and mclasse.get() == 'Guerreiro' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\feg.png")

        if mraca.get() == 'Elfo' and mclasse.get() == 'Mago' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fem.png")

        if mraca.get() == 'Elfo' and mclasse.get() == 'Ladino' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fel.png")

        if mraca.get() == 'Elfo' and mclasse.get() == 'Druida' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fed.png")

        # IMAGEM CHAR MASCULINO ANÃO
        if mraca.get() == 'Anão' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mh.png")

        if mraca.get() == 'Anão' and mclasse.get() == 'Guerreiro' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhg.png")

        if mraca.get() == 'Anão' and mclasse.get() == 'Mago' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhm.png")

        if mraca.get() == 'Anão' and mclasse.get() == 'Ladino' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhl.png")

        if mraca.get() == 'Anão' and mclasse.get() == 'Druida' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mhd.png")

        # IMAGEM CHAR FEMININO HUMANO
        if mraca.get() == 'Anão' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fh.png")

        if mraca.get() == 'Anão' and mclasse.get() == 'Guerreiro' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhg.png")

        if mraca.get() == 'Anão' and mclasse.get() == 'Mago' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhm.png")

        if mraca.get() == 'Anão' and mclasse.get() == 'Ladino' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhl.png")

        if mraca.get() == 'Anão' and mclasse.get() == 'Druida' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fhd.png")

        # IMAGEM CHAR MASCULINO ORC
        if mraca.get() == 'Orc' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mo.png")

        if mraca.get() == 'Orc' and mclasse.get() == 'Guerreiro' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mog.png")

        if mraca.get() == 'Orc' and mclasse.get() == 'Mago' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mom.png")

        if mraca.get() == 'Orc' and mclasse.get() == 'Ladino' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mol.png")

        if mraca.get() == 'Orc' and mclasse.get() == 'Druida' and sexo.get() == '1':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\mod.png")

        # IMAGEM CHAR FEMININO ORC
        if mraca.get() == 'Orc' and mclasse.get() == 'Escolha uma classe' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fo.png")

        if mraca.get() == 'Orc' and mclasse.get() == 'Guerreiro' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fog.png")

        if mraca.get() == 'Orc' and mclasse.get() == 'Mago' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fom.png")

        if mraca.get() == 'Orc' and mclasse.get() == 'Ladino' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fol.png")

        if mraca.get() == 'Orc' and mclasse.get() == 'Druida' and sexo.get() == '2':
            imagechar.configure(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fod.png")

        # CLASSES
        if mclasse.get != 'Escolha uma classe':

            classe = mclasse.get()
            if classe == 'Guerreiro':
                lbevida.config(text='20 pontos de vida', fg='green')
                pvida = 20

            elif classe == 'Mago':
                lbevida.config(text='08 pontos de vida', fg='green')
                pvida = 8

            elif classe == 'Ladino':
                lbevida.config(text='12 pontos de vida', fg='green')
                pvida = 12

            elif classe == 'Druida':
                lbevida.config(text='16 pontos de vida', fg='green')
                pvida = 16

        # RAÇAS
        if mraca.get() != 'Escolha uma raça':
            raca = mraca.get()

            global contador
            global valorh
            global efor
            global eint
            global ecar
            global econ
            global esab
            global edes

            if contador == 0:
                efor = 0
                eint = 0
                ecar = 0
                econ = 0
                esab = 0
                edes = 0

            if mraca.get() == 'Humano' and contador == 0:

                def confirmahuman():

                    if vatrihum1.get() != vatrihum2.get() and vatrihum2.get() != "Escolha" and vatrihum1.get() != "Escolha":

                        lbefor.config(text='+0 Racial ', fg='gray')
                        lbeint.config(text='+0 Racial ', fg='gray')
                        lbecar.config(text='+0 Racial ', fg='gray')
                        lbecon.config(text='+0 Racial ', fg='gray')
                        lbesab.config(text='+0 Racial ', fg='gray')
                        lbedes.config(text='+0 Racial ', fg='gray')
                        ahum1 = vatrihum1.get()
                        ahum2 = vatrihum2.get()

                        global valorh
                        global efor
                        global eint
                        global ecar
                        global econ
                        global esab
                        global edes
                        efor = 0
                        eint = 0
                        ecar = 0
                        econ = 0
                        esab = 0
                        edes = 0

                        if ahum1 == 'Força':
                            lbefor.config(text='+2 Racial ', fg='green')

                            efor = 2
                            valorh = 1

                        elif ahum1 == 'Inteligência':
                            lbeint.config(text='+2 Racial ', fg='green')
                            # global eint
                            eint = 2
                            valorh = 1

                        elif ahum1 == 'Carisma':
                            lbecar.config(text='+2 Racial ', fg='green')
                            # global ecar
                            ecar = 2
                            valorh = 1

                        elif ahum1 == 'Constituição':
                            # global econ
                            lbecon.config(text='+2 Racial ', fg='green')
                            econ = 2
                            valorh = 1

                        elif ahum1 == 'Sabedoria':
                            # global esab
                            lbesab.config(text='+2 Racial ', fg='green')
                            esab = 2
                            valorh = 1

                        elif ahum1 == 'Destreza':
                            # global edes
                            lbedes.config(text='+2 Racial ', fg='green')
                            edes = 2
                            valorh = 1

                        if ahum2 == 'Força':
                            lbefor.config(text='+2 Racial ', fg='green')
                            efor = 2
                            valorh += 1
                        elif ahum2 == 'Inteligência':
                            lbeint.config(text='+2 Racial ', fg='green')
                            # global eint
                            eint = 2
                            valorh += 1
                        elif ahum2 == 'Carisma':
                            lbecar.config(text='+2 Racial ', fg='green')
                            ecar = 2
                            valorh += 1
                        elif ahum2 == 'Constituição':
                            lbecon.config(text='+2 Racial ', fg='green')
                            econ = 2
                            valorh += 1
                        elif ahum2 == 'Sabedoria':
                            lbesab.config(text='+2 Racial ', fg='green')
                            esab = 2
                            valorh += 1
                        elif ahum2 == 'Destreza':
                            lbedes.config(text='+2 Racial ', fg='green')
                            edes = 2
                            valorh += 1

                        # atrihum.wm_attributes('-topmost', False)


                        atrihum.destroy()
                        jcadastro.wm_attributes("-disabled", False)  # destrava janela
                        jcadastro.wm_attributes('-topmost', True)
                        global contador
                        contador += 1
                        bconfirmar()
                        contador = 0

                    elif vatrihum1.get() == "Escolha" or vatrihum2.get() == "Escolha":
                        lbmsg.config(text='Escolha os atributos')
                        lbmsg['fg']= 'red'

                    elif vatrihum1.get() == vatrihum2.get():
                        lbmsg.config(text='Os atributos estão repetidos')
                        lbmsg['fg'] = 'red'

                def randomh():
                    import random
                    pts = ['Força', 'Inteligência', 'Carisma', 'Constituição', 'Sabedoria', 'Destreza']
                    random.shuffle(pts)
                    vatrihum1.set(pts[1])
                    vatrihum2.set(pts[2])


                jcadastro.wm_attributes("-disabled", True)  # trava janela
                atrihum = Toplevel()
                atrihum.title('Pontos Raciais')
                atrihum.wm_attributes('-topmost', True)
                atrihum.resizable(0, 0)
                atrihum.protocol('WM_DELETE_WINDOW', confirmahuman)
                atrihum.maxsize(width=280, height=250)
                atrihum.minsize(width=280, height=250)
                lbhum = Label(atrihum,
                              text='\n\nOBS: Você tem +2 pontos raciais para\ndistribuir em dois atributos diferentes.')
                lbhum.pack(side=TOP)

                fatri = Frame(atrihum)
                fatri.pack(pady= 15)

                vatrihum1 = StringVar(fatri)
                vatrihum1.set('Escolha')
                w = OptionMenu(fatri, vatrihum1, 'Força', 'Inteligência', 'Carisma', 'Constituição', 'Sabedoria',
                               'Destreza')
                w.pack(side=LEFT)
                lbdois1 = Label(fatri, text='  +2', fg='green')
                lbdois1.pack(side=LEFT)

                lbdois2 = Label(fatri, text='  +2', fg='green')
                lbdois2.pack(side=RIGHT)
                vatrihum2 = StringVar(fatri)
                vatrihum2.set("Escolha")
                w = OptionMenu(fatri, vatrihum2, 'Força', 'Inteligência', 'Carisma', 'Constituição', 'Sabedoria',
                               'Destreza')
                w.pack(side=RIGHT)

                lbmsg= Label(atrihum, text='')
                lbmsg.pack()

                fbt = Frame(atrihum)
                fbt.pack(pady= 20)

                okhum = Button(fbt, text='Confirmar', command=confirmahuman)
                okhum.pack(pady=5)

                randomhum = Button(fbt, text='Random', command= randomh)
                randomhum.pack(fill=X)


            if raca == 'Anão':
                lbefor.config(text='+0 Racial ', fg='gray')
                lbeint.config(text='+0 Racial ', fg='gray')
                lbecar.config(text='+0 Racial ', fg='gray')
                lbecon.config(text='+4 Racial ', fg='green')
                lbesab.config(text='+2 Racial ', fg='green')
                lbedes.config(text='-2 Racial. ', fg='red')
                efor = 0
                eint = 0
                ecar = 0
                econ = 4
                esab = 2
                edes = -2

            elif raca == 'Elfo':
                lbefor.config(text='+0 Racial ', fg='gray')
                lbeint.config(text='+2 Racial ', fg='green')
                lbecar.config(text='+0 Racial ', fg='gray')
                lbecon.config(text='-2 Racial ', fg='red')
                lbesab.config(text='+0 Racial ', fg='gray')
                lbedes.config(text='+4 Racial. ', fg='green')
                efor = 0
                eint = 2
                ecar = 0
                econ = -2
                esab = 0
                edes = 4

            elif raca == 'Orc':
                lbefor.config(text='+4 Racial ', fg='green')
                lbeint.config(text='+0 Racial ', fg='gray')
                lbecar.config(text='-2 Racial ', fg='red')
                lbecon.config(text='+2 Racial ', fg='green')
                lbesab.config(text='+0 Racial ', fg='gray')
                lbedes.config(text='+0 Racial. ', fg='gray')
                efor = 4
                eint = 0
                ecar = -2
                econ = 2
                esab = 0
                edes = 0

        listaAtri = [0]  # RESETA A LISTA PARA NÃO CONCATENAR CASO CONFIRME 2 VEZES
        # RECEBE VALOR DOS ATRIBUTOS
        if vatri1.get() and vatri2.get() and vatri3.get() and vatri4.get() and vatri5.get() and vatri6.get() != 'Escolha':
            afor = int(vatri1.get())  # Pega os valores dos atributos
            aint = int(vatri2.get())
            acar = int(vatri3.get())
            acon = int(vatri4.get())
            asab = int(vatri5.get())
            ades = int(vatri6.get())
            listaAtri.append(afor)
            listaAtri.append(aint)
            listaAtri.append(acar)
            listaAtri.append(acon)
            listaAtri.append(asab)
            listaAtri.append(ades)

        validacao = 0  # VARIAVEL PARA IDENTIFICAR SE TODOS CAMPOS FORAM PREENCHIDOS

        # TRATAMENTO DE NOME
        nomperson = enome.get()
        nomperson = nomperson.strip()  # tira espaço do começo e fim
        nomperson = nomperson.title()  # Maiuscula e Minuscula
        import re
        nomperson = re.sub("\s+", " ", nomperson)  # tira espaço extras no nomes
        snomperson = nomperson.replace(' ', '')  # tira todos espaços do meio

        if snomperson.isalpha() == True and len(snomperson) <= 1:
            lbficha.config(text='Insira um nome com mais de uma letra!')
            lbficha['fg'] = 'red'
            btficha['bg'] = 'red'
            btficha['fg'] = 'white'
            lbnome['fg'] = 'red'

        elif snomperson.isalpha() == True and len(snomperson) > 20:
            lbficha.config(text='Insira um nome menos de 20 letras!')
            lbficha['fg'] = 'red'
            btficha['bg'] = 'red'
            btficha['fg'] = 'white'
            lbnome['fg'] = 'red'

        elif snomperson.isalpha() == False and len(snomperson) > 1:
            lbficha.config(text='Insira usando somente letras!')
            lbficha['fg'] = 'red'
            btficha['bg'] = 'red'
            btficha['fg'] = 'white'
            lbnome['fg'] = 'red'

        elif snomperson.isalpha() == True and len(snomperson) > 1:
            import pymysql
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='123456',
                database='ficha_bd')

            cursor = conexao.cursor()
            teste_sqp = "SELECT * FROM tbl_person WHERE char_nome = %s"
            valorteste = (nomperson)
            cursor.execute(teste_sqp, valorteste)
            resultado = cursor.fetchall()
            nomerepetido = 0
            for x in resultado:

                if len(x) >= 1:
                    nomerepetido += 1

                else:
                    pass

            if nomerepetido == 0:
                lbnome['fg'] = 'black'
                validacao += 1

            if nomerepetido >= 1:
                lbficha.config(text='Já existe um personagem com esse nome!')
                lbficha['fg'] = 'red'
                btficha['bg'] = 'red'
                btficha['fg'] = 'white'
                lbnome['fg'] = 'red'

        else:
            lbficha.config(text='Insira um nome com mais de um digito \nusando somente letras!')
            lbficha['fg'] = 'red'
            btficha['bg'] = 'red'
            btficha['fg'] = 'white'
            lbnome['fg'] = 'red'

        if mclasse.get() != 'Escolha uma classe':
            classe = mclasse.get()
            lbclasse['fg'] = 'black'
            validacao += 1
        else:

            lbficha.config(text='Escolha uma classe para o personagem')
            lbficha['fg'] = 'red'
            btficha['bg'] = 'red'
            btficha['fg'] = 'white'
            lbclasse['fg'] = 'red'

        if sexo.get() == '1' or sexo.get() == '2':
            if sexo.get() == '1':
                sexoperson = 'Masculino'
            if sexo.get() == '2':
                sexoperson = 'Feminino'
            validacao += 1
        else:
            lbficha.config(text='Escolha uma sexo para o personagem')
            lbficha['fg'] = 'red'
            btficha['bg'] = 'red'
            btficha['fg'] = 'white'

            # if confirmar['bg'] == 'green':
            # validacao += 1
            # else:
            # lbficha.config(text='Verifique os Atributos')
            # lbficha['fg'] = 'red'
            # btficha['bg'] = 'red'
            # btficha['fg'] = 'white'

        if sorted(lista) == sorted(listaAtri):
            lbatributos['fg'] = 'black'
            validacao += 1

        if vatri1.get() and vatri2.get() and vatri3.get() and vatri4.get() and vatri5.get() and vatri6.get() == 'Escolha':
            lbficha.config(text='Escolha os Atributos!')
            lbficha['fg'] = 'red'
            lbatributos['fg'] = 'red'

        if vatri1.get() and vatri2.get() and vatri3.get() and vatri4.get() and vatri5.get() and vatri6.get() != 'Escolha' and sorted(
                lista) != sorted(listaAtri):
            lbficha.config(text='Atributos repetidos!')
            lbficha['fg'] = 'red'
            lbatributos['fg'] = 'red'

        if mraca.get() != 'Escolha uma raça':

            if mraca.get() != "Humano" and mraca.get() != 'Escolha uma raça':
                raca = mraca.get()
                lbraca['fg'] = 'black'
                validacao += 1

            elif mraca.get() == "Humano" and valorh > 1:
                lbraca['fg'] = 'black'
                validacao += 1




        else:
            lbficha.config(text='Escolha uma raça para o personagem')
            lbficha['fg'] = 'red'
            btficha['bg'] = 'red'
            btficha['fg'] = 'white'
            lbraca['fg'] = 'red'

        if validacao == 5:
            lbficha.config(text='')

            def defsim():

                # SOMA DE PONTO DE ATRIBUTOS + RACIAIS
                # import efor
                # import eint
                # global ecar
                # global econ
                # global esab
                # global edes
                global efor
                global eint
                global ecar
                global econ
                global esab
                global edes

                ptfor = (int(vatri1.get()) + efor)
                ptint = (int(vatri2.get()) + eint)
                ptcar = (int(vatri3.get()) + ecar)
                ptcon = (int(vatri4.get()) + econ)
                ptsab = (int(vatri5.get()) + esab)
                ptdes = (int(vatri6.get()) + edes)

                # ADCIONANDO NO BANCO DE DADOS
                import pymysql
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='123456',
                    database='ficha_bd')
                cursor = conexao.cursor()
                com_sql = "INSERT INTO tbl_person(char_nome, char_sexo, char_raca, char_classe, char_vida, char_for, char_int, char_car, char_con, char_sab, char_des) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                valor = (nomperson, sexoperson, raca, classe, pvida, ptfor, ptint, ptcar, ptcon, ptsab, ptdes)
                cursor.execute(com_sql, valor)
                conexao.commit()
                confirmarficha.destroy()
                jcadastro.wm_attributes('-topmost', True)
                jcadastro.wm_attributes("-disabled", False)
                lbficha.config(text='Cadastro feito com sucesso.')
                lbficha['fg'] = 'green'
                btficha['bg'] = 'green'
                btficha['fg'] = 'white'

                lista.clear()
                lista.append(0)
                print(lista)
                for atributo in range(6):
                    atributo = randint(0, 20)
                    lista.append(atributo)
                    print('1d20: ', atributo)
                vatri1.set(lista[1])
                vatri2.set(lista[2])
                vatri3.set(lista[3])
                vatri4.set(lista[4])
                vatri5.set(lista[5])
                vatri6.set(lista[6])
                print(lista)
                # jcadastro.destroy()

            def defnao():
                confirmarficha.destroy()
                jcadastro.wm_attributes('-topmost', True)
                jcadastro.wm_attributes("-disabled", False)
                lbficha.config(text='')
                btficha['bg'] = 'gray'
                btficha['fg'] = 'black'
                global contador
                contador = 0

            if contador == 1 or mraca.get() != 'Humano' and mraca.get() != 'Escolha uma raça':
                confirmarficha = Toplevel()
                confirmarficha.title("Confirmar")
                confirmarficha.maxsize(width=250, height=100)
                confirmarficha.minsize(width=250, height=100)
                confirmarficha.protocol('WM_DELETE_WINDOW', defnao)
                confirmarficha.wm_attributes('-topmost', True)
                jcadastro.wm_attributes("-disabled", True)

                labelapagar = Label(confirmarficha, text="Deseja mesmo salvar esse personagem?")
                labelapagar.grid(row=0, column=1, columnspan=2, sticky=EW, ipadx=10, ipady=10)
                bsim = Button(confirmarficha, text="Sim", command=defsim)
                bsim.grid(row=1, column=1, sticky=E, ipadx=5, pady=10)
                bnao = Button(confirmarficha, text="Não", command=defnao)
                bnao.grid(row=1, column=2, sticky=W, ipadx=5, pady=10)

    # -----------------------------------------JANELA CADASTRO-------------------------------------------------------
    jcadastro = Toplevel()
    # jinicial.wm_attributes("-disabled", False) #trava janela
    jcadastro.title('Cadastro de Personagens')
    jcadastro.geometry("850x260+350+200")
    jcadastro.resizable(0, 0)

    # GERADOR DE PONTOS
    lista = [0]
    for atributo in range(6):
        atributo = randint(0, 20)
        lista.append(atributo)
        print('1d20: ', atributo)

    # LABEL TIPOS DE ATRIBUTOS
    lbatributos = Label(jcadastro, text='Atributos', font="-weight bold -size 10")
    lbatributos.grid(row=0, column=1, sticky=N, ipadx=10)

    lbfor = Label(jcadastro, text='Força')
    lbfor.grid(row=1, column=1)

    lbint = Label(jcadastro, text='Inteligência')
    lbint.grid(row=2, column=1, ipadx=10)

    lbcar = Label(jcadastro, text='Carisma')
    lbcar.grid(row=3, column=1)

    lbcon = Label(jcadastro, text='Constituição')
    lbcon.grid(row=4, column=1)

    lbsab = Label(jcadastro, text='Sabedoria')
    lbsab.grid(row=5, column=1)

    lbdes = Label(jcadastro, text='Destreza')
    lbdes.grid(row=6, column=1)

    # MENU DE OPÇÕES DE PONTOS DE ATRIBUTOS
    vatri1 = StringVar(jcadastro)
    vatri1.set("Escolha")
    w = OptionMenu(jcadastro, vatri1, lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
    w.grid(row=1, column=2, sticky=W)

    vatri2 = StringVar(jcadastro)
    vatri2.set("Escolha")
    w = OptionMenu(jcadastro, vatri2, lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
    w.grid(row=2, column=2, sticky=W)

    vatri3 = StringVar(jcadastro)
    vatri3.set("Escolha")
    w = OptionMenu(jcadastro, vatri3, lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
    w.grid(row=3, column=2, sticky=W)

    vatri4 = StringVar(jcadastro)
    vatri4.set("Escolha")
    w = OptionMenu(jcadastro, vatri4, lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
    w.grid(row=4, column=2, sticky=W)

    vatri5 = StringVar(jcadastro)
    vatri5.set("Escolha")
    w = OptionMenu(jcadastro, vatri5, lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
    w.grid(row=5, column=2, sticky=W)

    vatri6 = StringVar(jcadastro)
    vatri6.set("Escolha")
    w = OptionMenu(jcadastro, vatri6, lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
    w.grid(row=6, column=2, sticky=W)

    # Random
    def randomizar():
        import random
        vatri1.set(lista[1])
        vatri2.set(lista[2])
        vatri3.set(lista[3])
        vatri4.set(lista[4])
        vatri5.set(lista[5])
        vatri6.set(lista[6])
        listarandom = random.sample(lista, 7)
        listarandom.remove(0)
        vatri1.set(listarandom[0])
        vatri2.set(listarandom[1])
        vatri3.set(listarandom[2])
        vatri4.set(listarandom[3])
        vatri5.set(listarandom[4])
        vatri6.set(listarandom[5])

    brandom = Button(jcadastro, text='Random', command=randomizar)
    brandom.grid(row=7, column=2, pady=10, ipadx=5)

    # LABEL/ENTRY NOME
    lbnome = Label(jcadastro, text='Nome:', font="-weight bold -size 9")
    lbnome.grid(row=0, column=5, sticky=N)
    enome = Entry(jcadastro, width=30)
    enome.grid(row=1, column=5, sticky=W, padx=(55, 10))

    # MENU DE OPÇÕES RAÇA
    lbraca = Label(jcadastro, text='Raça', font="-weight bold -size 9")
    lbraca.grid(row=0, column=6)
    mraca = StringVar(jcadastro)
    mraca.set('Escolha uma raça')
    w = OptionMenu(jcadastro, mraca, 'Humano', 'Elfo', 'Anão', 'Orc')
    w.grid(row=1, column=6, sticky=E, ipadx=3)

    # MENU DE OPÇÕES CLASSE
    lbclasse = Label(jcadastro, text='Classe', font="-weight bold -size 9")
    lbclasse.grid(row=0, column=7)
    mclasse = StringVar(jcadastro)
    mclasse.set('Escolha uma classe')
    z = OptionMenu(jcadastro, mclasse, 'Guerreiro', 'Mago', 'Ladino', 'Druida')
    z.grid(row=1, column=7, sticky=W)

    # LABEL DA VIDA
    lbevida = Label(jcadastro, text='')
    lbevida.grid(row=2, column=6, columnspan=2)

    # RADIOBUTTON SEXO
    sexo = StringVar(jcadastro, '1')
    Radiobutton(jcadastro, text="Masculino", variable=sexo, value='1').grid(row=3, column=6, columnspan=2)
    Radiobutton(jcadastro, text="Feminino ", variable=sexo, value='2').grid(row=4, column=6, columnspan=2)

    # CONFIRMAR FICHA
    btficha = Button(jcadastro, text='Salvar Ficha', command=bconfirmar, font="-weight bold -size 9")
    btficha.grid(row=6, column=6, columnspan=2, ipadx=20)

    # LABEL AVISO CONFIRMAR FICHA
    lbficha = Label(jcadastro, text='')
    lbficha.grid(row=7, column=6, columnspan=2, pady=(5, 0))

    # LABEL ATRIBUTOS
    lbefor = Label(jcadastro, text='+0 Racial ', fg='gray')
    lbefor.grid(row=1, column=3)
    lbeint = Label(jcadastro, text='+0 Racial ', fg='gray')
    lbeint.grid(row=2, column=3, sticky=W)
    lbecar = Label(jcadastro, text='+0 Racial ', fg='gray')
    lbecar.grid(row=3, column=3, sticky=W)
    lbecon = Label(jcadastro, text='+0 Racial ', fg='gray')
    lbecon.grid(row=4, column=3, sticky=W)
    lbesab = Label(jcadastro, text='+0 Racial ', fg='gray')
    lbesab.grid(row=5, column=3, sticky=W)
    lbedes = Label(jcadastro, text='+0 Racial. ', fg='gray')
    lbedes.grid(row=6, column=3, sticky=W)

    fchar = Frame(jcadastro, highlightbackground='gray', highlightthickness=3)
    fchar.grid(row=2, column=5, rowspan=6, padx=50)
    imagechar = PhotoImage(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\m.png")

    canvas = Canvas(fchar, width=185, height=165)
    canvas.pack()
    canvas.create_image(20, 20, anchor=NW, image=imagechar)

    mainloop()
    
