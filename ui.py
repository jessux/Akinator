from Tkinter import *
import akinator
import questions

q =questions.question()

while len(q.questionAVenir ) >0:
    q.repondreQuestion()

