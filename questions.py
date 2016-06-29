# -*- coding: utf8 -*-

import akinator
import csv
import random

class question:
    def __init__(self):
        self.id = random.randrange(0,11)
        self.instanceMoteur = akinator.moteur()
        self.questionPasse =[]
        self.questionAVenir= []
        self.initQuestion()

    def poserQuestion(self):
        with open("question.csv","r") as questionFile:
            questions = csv.DictReader(questionFile)
            for question in questions:
                if int(question["id"]) == self.id:
                    if self.id != self.nextQuestion(question["attrib"]):
                        self.id = self.nextQuestion(question["attrib"])
                    else:
                        self.id = int(self.questionAVenir[random.randrange(0,len(self.questionAVenir))]["id"])
                    return question


    def initQuestion(self):
        with open("question.csv","r") as questionFile:
            questions = csv.DictReader(questionFile)
            for question in questions:
                self.questionAVenir.append(question)
                
    def nextQuestion(self,attrib):
        nextQuestionScore = []
        question = self.instanceMoteur.getVillesToQuestion(attrib)
        for attribToVerif in self.questionAVenir:
            questionCompare = self.instanceMoteur.getVillesToQuestion(attribToVerif["attrib"])
            for elem in questionCompare:
                if elem not in question:
                    questionCompare.pop(questionCompare.index(elem))
            nextQuestionScore.append([attribToVerif["id"],len(questionCompare)])
        mini = 999999
        tmp = 0
        for q in nextQuestionScore:
            if q[1] <= mini:
                mini = q[1]
                tmp = q[0]
        return int(tmp)
    
    def repondreQuestion(self):
        #q= self.poserQuestion()
        #return q["question"]
        return self.poserQuestion()

    def updateResponse(self,q,val):
        self.instanceMoteur.updateScore(q["attrib"],int(val))
        self.questionPasse.append([q,int(val)])
        self.questionAVenir.pop(self.questionAVenir.index(q))


if __name__ == '__main__':

    q = question()
