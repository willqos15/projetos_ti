from tkinter import * #Biblioteca Interface

#JANELA PRINCIPAL
class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        #Banco de Dados
        import pymysql
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='123456')
        cursor = conexao.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ficha_bd")

        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='ficha_bd')
        cursor = conexao.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS tbl_person(char_id INT AUTO_INCREMENT PRIMARY KEY, char_nome VARCHAR(255) UNIQUE, char_sexo VARCHAR(255), char_raca VARCHAR(255), char_classe VARCHAR(255), char_vida INT, char_for INT, char_int INT, char_car INT, char_con INT, char_sab INT, char_des INT)")

        '''#MUSICA
        import pygame
        pygame.init()
        pygame.mixer.music.load('C://Users//William//PycharmProjects//RPGPYTHON//rpg//Lord of the Rings Theme Song.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        #MUSICA'''

        #pygame.mixer.unpause()

        # IMAGEM DE FUNDO
        imagemdefundo = PhotoImage(file="C:\\Users\\William\\PycharmProjects\\RPGPYTHON\\rpg\\midia\\fantasyart.png")
        self.w = Label(self, image=imagemdefundo)
        self.w.imagemdefundo = imagemdefundo
        self.w.pack()
        #self.w.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        self.pack()
        self.bg = imagemdefundo

        # BOTÕES
        import JanelaCadastro 
        import JanelaListaPerson 
        self.cperson = Button(self, text='Criar Personagem', command=JanelaCadastro.criarjc)
        self.cperson.place(x=300, y=190)

        self.asperson = Button(self, text='Lista de Personagens', command=JanelaListaPerson.criarjlp)
        self.asperson.place(x=295, y=230)
        
        def csair():
            app.master.destroy()
        
        self.sair = Button(self, text='Sair', command=csair)
        self.sair.place(x=335, y=270)


#CONFIGURAÇÕES DA JANELA
app = Application()
app.master.title('RPG Python Tkinter')
app.master.geometry("700x467+350+100")
app.master.resizable(0, 0)
#app.master.maxsize(width=700,height=467)
#app.master.minsize(width=700,height=467)
mainloop()
