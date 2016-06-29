from Tkinter import *
import akinator
import questions
import shutil
import ttk
from ttk import Button,Style

q =questions.question()

listeReponse={}
def Ok():
    Texte.set("Super !")
    quit()


def update(cap,discriminant,question):
    for i in q.questionPasse:
        if i[1] == 3 or i[1] == 1:
            listeReponse[i[0]["attrib"]] = "True"
        else:
            listeReponse[i[0]["attrib"]] = "False"

    q.instanceMoteur.db.addCapitale(cap.get(), listeReponse)
    shutil.copy2("out.csv", "villesTF.csv")
    q.instanceMoteur.db.addDiscriminant(discriminant.get(),cap.get(),question.get())
    shutil.copy2("out.csv", "villesTF.csv")
    shutil.copy2("out1.csv", "question.csv")
    quit()

def Ko():
    non = Toplevel()
    non.grab_set()
    labl= Label(non,text="Nom de la capitale:")
    labl.pack()
    cap = StringVar()
    discriminant = StringVar()
    question=StringVar()
    capitale = Entry(non,textvariable=cap)
    capitale.pack()
    lab1 = Label(non, text="Discriminant : ")
    lab1.pack()
    disc = Entry(non, textvariable=discriminant)
    disc.pack()
    lab2 = Label(non, text="Question : ")
    lab2.pack()
    quest = Entry(non, textvariable=question)
    quest.pack()
    valid = Button(non, text ='Save', command = lambda: update(cap,discriminant,question))
    valid.pack()

def NouveauLance():
    global q
    global q1
    if(len(q.questionAVenir)!=0):
        q1 = q.repondreQuestion()
        Texte.set(q1["question"])
    else:
        Texte.set("Est-ce bien ca ?\n"+str(q.instanceMoteur.getMaxScore()))
        print q.instanceMoteur.getMaxScore()
        fin = Toplevel()
        fin.grab_set()
        Labelres = Label(fin, textvariable=Texte, fg='red', bg='white')
        Labelres.pack()
        a = Button(fin, text='Oui', command=Ok)
        a.pack()
        b = Button(fin, text='Non', command=Ko)
        b.pack()

def Oui():
    global q
    global q1
    try:
        q.updateResponse(q1,3)
    finally:
        NouveauLance()

def Non():
    global q
    global q1
    try:
        q.updateResponse(q1, -3)
    finally:
        NouveauLance()

def PEOui():
    global q
    global q1
    try:
        q.updateResponse(q1, 1)
    finally:
        NouveauLance()

def PENon():
    global q
    global q1
    try:
        q.updateResponse(q1, -1)
    finally:
        NouveauLance()

def JNSP():
    global q
    global q1
    try:
        q.updateResponse(q1, 0)
    finally:
        NouveauLance()

def precedent():
    pass

Mafenetre = Tk()
style=ttk.Style()
style.configure('TButton',foreground="blue",relief="RAISED")
bgimg = PhotoImage(file="bg.gif")
bg = Label(Mafenetre,image=bgimg)
bg.place(x=0,y=0,relwidth=1,relheight=1)
Mafenetre.title('Capitator')
Mafenetre.geometry('500x500+400+400')

Texte = StringVar()
NouveauLance()
LabelResultat = Label(Mafenetre, textvariable = Texte, fg ='red',font=("Helvetica", 12))
LabelResultat.pack(side = TOP, padx = 5, pady = 15)


BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = BOTTOM, padx = 5, pady = 5)

BoutonOui = Button(Mafenetre, text ='Oui', command = Oui)
BoutonOui.place(x=205,y=145)
BoutonPEOui = Button(Mafenetre, text ='Peu etre que oui', command = PEOui)
BoutonPEOui.place(x=197,y=175)
BoutonJNSP= Button(Mafenetre, text ='Je ne sais pas', command = JNSP)
BoutonJNSP.place(x=203,y=205)
BoutonPENon =Button(Mafenetre, text ='Peu etre que non', command = PENon)
BoutonPENon.place(x=195,y=235)
BoutonNon =Button(Mafenetre, text ='Non', command = Non)
BoutonNon.place(x=205,y=265)
Mafenetre.mainloop()