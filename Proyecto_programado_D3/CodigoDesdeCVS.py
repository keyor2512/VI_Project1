import csv
import plotly.graph_objects as go
from colour import Color
import json
class obtList:
    listTe=[]
    listpp=[]
    ids=[]
    parents=[]
    labels=[]
    contadorN=0
    listPos=[]
    coloresM=[]
    coloresM2=[]
    coloresM3=["lightgrey"]
    contC=-1
    valuesT=[]
    valuesT2=[]
    total=21
    totH2=0
    totH1=0
    Lvalues=[]
    LF=[]
    contG=-1
    tipo=0
    def __init__(self,nombreCSV,padre,tipo):
        self.tipo=tipo
        salto=False
        #abre el csv
        with open(nombreCSV+".csv", newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                if(salto):
                    self.listTe.append(row)
                    self.listpp.append(row[-1])
                else:
                    salto=True

                    
        #crea el primer padre
        self.ids=[padre]
        self.labels=[padre]
        self.parents=[""]
        self.listTe=(self.splitP(self.listTe))
##################################################################################################################################################################################################
        #aplica el splitP ya sea 1 vez o 2 veces dependiendo del atributo tipo, el cual se usa para los documentos e1 y e2 que tienen diferentes cantidad de hijos
        conto=0
        if(tipo==2):
            while(conto<len(self.listTe)):
                self.valuesT.append([0,[],[]])
                conto2=0
                self.listTe[conto][-1]=self.splitP(self.listTe[conto][-1])
                while(conto2<len(self.listTe[conto][-1])):
                    self.valuesT[-1][2].append(self.getN((self.listTe[conto][-1][conto2][-1])))
                    self.valuesT[-1][1].append(self.sumL(self.getN((self.listTe[conto][-1][conto2][-1]))))
                    self.Lvalues.extend(self.getN((self.listTe[conto][-1][conto2][-1])))
                    self.valuesT[-1][0]=self.valuesT[-1][0]+self.sumL(self.getN((self.listTe[conto][-1][conto2][-1])))
                    conto2+=1
                self.total=self.total+self.valuesT[-1][0]
                conto+=1
        else:
            self.Lvalues=self.listpp
        cont=0

##################################################################################################################################################################################################        
        #Crea el json con los datos obtenidos y lo guarda en un archivo
        with open(padre+".json", "w") as outfile:
            temd={}
            temd["name"]=padre
            temd["children"]=self.LtoDic(self.listTe)
            outfile.write(json.dumps(temd))
##################################################################################################################################################################################################
        #separa la lista generada en split en padres, labels e Ids
        self.asig(self.listTe,padre,0)
##################################################################################################################################################################################################
    #convierte la lista de listas en diccionarios anidados con la estructura necesaria para ser ingresada en el json
    def LtoDic(self,lista):
        dicci=[{}]
        cont=0
        while(cont<len(lista)):
            if(self.tipo==2):
                if(lista[cont][0]!=lista[cont-1][0]):
                    if(type(lista[cont])!=list):
                        self.contG+=1
                        print(self.Lvalues[self.contG])
                        return self.Lvalues[self.contG]
                    else:
                        dicci[-1]["name"]=lista[cont][1]
                        if(type(lista[cont][-1])!=list):
                            dicci[-1]["value"]=self.LtoDic(lista[cont][-1])
                        else:
                            dicci[-1]["children"]=self.LtoDic(lista[cont][-1])
                    dicci.append({})
            else:
                if(type(lista[cont])!=list):
                    self.contG+=1
                    print(self.Lvalues[self.contG])
                    return self.Lvalues[self.contG]
                else:
                    dicci[-1]["name"]=lista[cont][1]
                    if(type(lista[cont][-1])!=list):
                        dicci[-1]["value"]=self.LtoDic(lista[cont][-1])
                    else:
                        dicci[-1]["children"]=self.LtoDic(lista[cont][-1])
                dicci.append({}) 
            cont+=1
        return dicci
##################################################################################################################################################################################################
    #une las listas de valores, las de las sumas de los hijos con las de sus padres
    def settinVal(self):
        lista=[]
        cont=0
        while(cont<len(self.valuesT)):
            lista.append(self.valuesT[cont][0])
            cont2=0
            while(cont2<len(self.valuesT[cont][1])):
                  lista.append(self.valuesT[cont][1][cont2])
                  lista.extend(self.valuesT[cont][2][cont2])
                  cont2+=1
            cont+=1
        lista.insert(0,self.total)
        return lista
##################################################################################################################################################################################################
    #suma todos los valores similares, por ejemplo todos los valores de caballos pura sangre y los que no los convierte en un solo valor
    def getN(self,lista):
        lista2=[[0]]
        ultimo=lista[0][0]
        cont=0
        while(cont<len(lista)):
            if(lista[cont][0]==ultimo):
                lista2[-1][0]+=float(lista[cont][-1])
                cont+=1
            else:
                lista2.append([0])
                ultimo=lista[cont][0]
        return self.quitL(lista2)
##################################################################################################################################################################################################    
    #recibe una lista de numeros y devuelve el total de la suma de estos 
    def sumL(self,lista):
        cont=0
        tot=0
        while(cont<len(lista)):
            tot+=lista[cont]
            cont+=1
        return tot

##################################################################################################################################################################################################
    #concatena 2 listas, siendo la segunda una lista de listas, toma un valor en posicion x de la lista 1 y le concatena todos los valores de la lista 2 en la posicion x
    def unir(self,lista1,lista2):
        cont=0
        LF=[]
        while(cont<len(lista1)):
            LF.append(lista1[cont][1])
            cont2=0
            while(cont2<len(lista1[cont][2])):
                 LF.append(lista1[cont][2][cont2])
                 
                 LF.extend(lista2[cont2])
                 cont2+=1
            cont+=1
        return LF
##################################################################################################################################################################################################
    #genera una degradacion de color con los colores ingresados
    def LC(self):
        cont=0
        while(cont<len(self.coloresM)):
            self.coloresM2.append(list(Color(self.coloresM[cont]).range_to(Color("white"),20)))
            cont+=1
##################################################################################################################################################################################################
    #funcion que quita las listas de listas dentro de una lista convirtiendola en una lista plana
    def quitL(self,lista):
        lista2=[]
        cont=0
        while(cont<len(lista)):
            lista2.append(lista[cont][0])
            cont+=1
        return lista2
##################################################################################################################################################################################################
    #funcion principal que separa el CVS en listas de listas
    def splitP(self,lista):
        count=0
        count2=0
        listT=[]
        if(len(lista)>3):
            listT.append([lista[0][0],lista[0][1],[]])
            while len(lista)>0:
                if(lista[0][0]==listT[count2][0]):
                   listT[count2][2].append(lista[0][2:])
                   lista=lista[1:]
                   
                else:
                    listT.append([lista[0][0],lista[0][1],[]])
                    count2+=1
            return listT
        else:
            return

 ##################################################################################################################################################################################################       
    #funcion que utiliza la listas de listas y genera la lista de Ids,Labels,Parents
    def asig(self,lista,parent,pos):
        cont4=0
        while(cont4<len(lista)):
            if(type(lista[cont4][-1])!=list):
                if(self.ids[-1]!=lista[cont4][1]):
                    self.ids.append(lista[cont4][1])
                    self.labels.append(lista[cont4][1])
                    self.parents.append(parent)
                    self.listPos.append(pos)
            else:
                self.ids.append(lista[cont4][1])
                self.labels.append(lista[cont4][1])
                self.parents.append(parent)
                self.listPos.append(pos)
                lista[cont4][-1]=self.asig(lista[cont4][-1],lista[cont4][1],pos+1)
            cont4+=1
        return
##################################################################################################################################################################################################
    #funcion que coloca los numeros en sus posiciones (ya no se usa)
    def nums(self,lista):
        listp=[]
        cont4=0
        while(cont4<len(lista)):
            if(type(lista[cont4][-1])!=list):
                lista[cont4][2]=self.listpp[self.contadorN]
                self.contadorN=self.contadorN+1
            else:
                lista[cont4][-1]=self.nums(lista[cont4][-1])
            cont4+=1
        return lista
##################################################################################################################################################################################################
    #funcion recursiva que aplica splitP las veces que sean necesarias (ya no se usa)
    def splitRecur (self,lista):
        count2=0
        ll=[]
        if(lista!=None):
            while(count2<len(lista)):
                
                if(type(lista[count2][-1])==list):
                    lista[count2][-1]=self.splitRecur(self.splitP(lista[count2][-1]))
                    count2+=1
                else:
                    return lista
            return lista
        return
##################################################################################################################################################################################################
    #concatena todos los valores de una lista, en otra lista (ya no se usa)
    def concNum(lista):
        self.listV.append(sumL(lista))
        cont=0
        while(cont<len(lista)):
            self.listV.append(lista[cont])
##################################################################################################################################################################################################            
    #coloca los colores utilizando las degradaciones creadas anteriormente
    def setColors(self):
        cont=0
        while(cont<len(self.listPos)):
              if(self.listPos[cont]==0):
                  
                  self.contC=self.contC+1
              self.coloresM3.append((self.coloresM2[self.contC][self.getPos(cont)]).get_hex_l())
              cont+=1
##################################################################################################################################################################################################              
    #devuelven los valores
    def getIds(self):
        return self.ids
    def getParents(self):
        return self.parents
    def getLabels(self):
        return self.labels
    def getPos(self,posi):
        return self.listPos[posi]
    def getColors(self):
        return self.coloresM3
    def getValues(self):
        return self.settinVal()

    
    
    
