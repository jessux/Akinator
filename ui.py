from Tkinter import *
import akinator
import questions

q =questions.question()

while len(q.questionAVenir ) >0:
    q.repondreQuestion()

listeReponse={}
for i in q.questionPasse:
    if i[1] == 3 or i[1] == 1:
        listeReponse[i[0]["attrib"]]="True"
    else:
        listeReponse[i[0]["attrib"]]="False"

print q.instanceMoteur.getMaxScore()
suite=raw_input("Est-ce bien ca ? (y/n) : ")
if suite == "y":
    print "Super !"
else:
    q.instanceMoteur.db.addCapitale(raw_input("Nom de la capitale : "),listeReponse)
