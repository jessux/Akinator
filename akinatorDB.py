
# -*- coding: utf8 -*-
import csv


class bdd:
    def __init__(self):
        self.file = "villesTF.csv"

    def affiche(self):
        liste = []
        for row in self.bdd:
            liste.append(row)
        return liste
            
    def setCapitaleListe(self):
        with open(self.file ,"r") as csvfile:
            bdd = csv.DictReader(csvfile)
            liste=[]
            for capitale in bdd:
                liste.append({capitale["capitald"] : 0})
        return liste

    def getCapitaleId(self,column):
        with open(self.file ,"r") as csvfile:
            bdd = csv.DictReader(csvfile)
            cap=[]
            for row in bdd:
                if row[column] == "True":
                    cap.append(row["capitald"])
        return cap

    def getNbCapitales(self):
        count = 0
        with open(self.file , "r") as csvfile:
            bdd = csv.reader(csvfile)
            for row in bdd:
                count += 1
        return count

    def parseTrueFalse(self,liste):
        tab=[]
        with open(self.file, "rb") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for elem in row:
                    if elem != "capitald":
                        if elem in liste.keys():
                            tab.append(liste[str(elem)])
                        else:
                            tab.append("False")
                return tab

    
    def addCapitale(self,capitale,listeAttributs):
        with open(self.file,"rb") as csvfile:
            with open("out.csv","wb") as out:
                reader = csv.reader(csvfile)
                writer = csv.writer(out)
                row = reader.next()
                all = [row]
                modif = False
                for row in enumerate(reader):
                    if row[1][0] == capitale:
                        tmp = self.updateCapitale(capitale,listeAttributs)
                        tmp1 = []
                        print tmp,tmp1
                        for col in all[0]:
                            tmp1.append(tmp[col])
                            print tmp1
                        all.append(tmp1)
                        modif = True
                    else:
                        all.append(row[1])
                if not modif:
                    newCap = [capitale]
                    newCap.extend(self.parseTrueFalse(listeAttributs))
                    all.append(newCap)
                writer.writerows(all)
                
    def getAttrib(self,capitale):
        with open(self.file ,"r") as csvfile:
            bdd = csv.DictReader(csvfile)
            cap=[]
            for row in bdd:
                if row["capitald"] == capitale:
                    cap.append(row)
        return cap
    
    def updateCapitale(self,capitale,listeAttibuts):
        attrib = self.getAttrib(capitale)        
        for at in listeAttibuts:
            if int(at[1]) > 0:
                attrib[0][at[0]["attrib"]] = "True"
            else:
                attrib[0][at[0]["attrib"]] = "False"

        return attrib[0]             
                
    def addDiscriminant(self,columnName,capitale):
        with open(self.file,"rb") as csvfile:
            with open("out.csv","wb") as out:
                reader = csv.reader(csvfile)
                writer = csv.writer(out)
                all = []
                row = reader.next()
                row.append(columnName)
                all.append(row)
                for row in enumerate(reader):
                    if row[1][0] == capitale:
                        all.append(row[1]+["True"])
                    all.append(row[1]+["False"])
                writer.writerows(all)
                
    
        
if __name__ == "__main__" :
    
    bdd = bdd()
    #maliste = bdd.setCapitaleListe()
    
    ## GMT ?
