# -*- coding: utf8 -*-

import akinatorDB
from collections import Counter

class moteur:
    def __init__(self):
        self.db = akinatorDB.bdd()
        self.scoreTab = self.db.setCapitaleListe()

    def updateScore(self,attrib,score):
        capitaleListe =  self.db.getCapitaleId(attrib)
        for capitales in capitaleListe:
            for cap in self.scoreTab:
                if cap.has_key(capitales):
                    cap[capitales] += score
        if self.getProbaFind() > 95.0:
            self.getMaxScore()

    def getMaxScore(self): 
        maxi = 0
        capitale = []
        for score in self.scoreTab:
            if score.values() > maxi :
                maxi = score.values()
                capitale = [score]
            elif score.values() == maxi:
                maxi = score.values()
                capitale.append(score)
        return capitale

    def getVillesToQuestion(self,attrib):
        return self.db.getCapitaleId(attrib)
        

    def getProbaFind(self):
        liste = self.getMaxScore()
        return 100.0-(float(len(liste))/float(self.db.getNbCapitales()))*100

    def getNbVillesReponse(self):
        return len(self.getMaxScore())

    
    # def __init__(self):
        # self.attribs = {}
        # self.liste= []
        # self.c = {}
        # self.match = []

    # def addAttrib(self,attrib):
        # self.attribs[attrib] = 1

    # def printAttribList(self):
        # for elem in self.attribs:
            # print elem
            
    # def getFatherMatchingAttrib(self):
        # self.parent_map = {}
        # for p in db.bdd.findall("ville"):
            # for c in p:
                # if c.text in self.parent_map:
                    # if self.attribs.has_key(c.text):
                        # self.parent_map[c.text].append(p.get('name'))
                # else:
                    # if self.attribs.has_key(c.text):
                        # self.parent_map[c.text] = [p.get('name')]
    
    # def getMatch(self):
        
        # for elem in self.parent_map.itervalues():
            # for val in elem:
                # self.liste.append(val)
        # self.c= Counter( self.liste )
        # maxi = -1
        # for key , val in self.c.iteritems():
            # if val > maxi:
                # maxi = val
        # for key,val in self.c.iteritems():
            # if val == maxi:
                # self.match.append(key)

                
