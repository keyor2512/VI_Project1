import csv
import plotly.graph_objects as go
from colour import Color
import json

from numpy.lib.function_base import append
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
    padre=""
    lNums=[]
    VValues=[]
    listSizes=[]
    coloresPa=["#AFCBFF","#D7F9FF","#F9FBF2","#FFEDE1","#FFA970","#D4E2A1"]
    contColor=-1
    def __init__(self,nombreCSV,padre,tipo):
        self.tipo=tipo
        self.padre=padre
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

        self.listTe=(self.splitP(self.listTe))
       
##################################################################################################################################################################################################
        #aplica el splitP ya sea 1 vez o 2 veces dependiendo del atributo tipo, el cual se usa para los documentos e1 y e2 que tienen diferentes cantidad de hijos
        conto=0
        if(tipo==2):
            while(conto<len(self.listTe)):
                self.valuesT.append([0,[],[]])
                self.lNums.append([0])
                conto2=0
                self.listTe[conto][-1]=self.splitP(self.listTe[conto][-1])
                
                while(conto2<len(self.listTe[conto][-1])):
                    self.valuesT[-1][2].append(self.getN((self.listTe[conto][-1][conto2][-1])))
                    self.valuesT[-1][1].append(self.sumL(self.getN((self.listTe[conto][-1][conto2][-1]))))
                    self.Lvalues.extend(self.getN((self.listTe[conto][-1][conto2][-1])))
                    self.valuesT[-1][0]=self.valuesT[-1][0]+self.sumL(self.getN((self.listTe[conto][-1][conto2][-1])))
                    self.lNums[-1][0]=self.lNums[-1][0]+self.sumL(self.getN((self.listTe[conto][-1][conto2][-1])))
                    self.lNums[-1].append(self.sumL(self.getN((self.listTe[conto][-1][conto2][-1]))))
                    self.lNums[-1].extend(self.getN((self.listTe[conto][-1][conto2][-1])))
                    conto2+=1
                self.total=self.total+self.valuesT[-1][0]
                conto+=1
                self.listSizes.append(self.valuesT[-1][0])
        else:
            self.Lvalues=self.listpp
            while(conto<len(self.listTe)):
                self.valuesT.append([0,[]])
                self.lNums.append([0])
                conto2=0
                while(conto2<len(self.listTe[conto][-1])):
                    
                    self.lNums[-1][0]=self.lNums[-1][0]+float(self.listTe[conto][-1][conto2][-1])
                    self.lNums[-1].append(self.listTe[conto][-1][conto2][-1])
                    self.valuesT[-1][-1].append(self.listTe[conto][-1][conto2][-1])
                    conto2+=1
                self.valuesT[-1][0]=self.sumL(self.valuesT[-1][-1])
                self.total=self.total+self.valuesT[-1][0]
                conto+=1
                self.listSizes.append(self.valuesT[-1][0])
##################################################################################################################################################################################################        
        #Crea el json con los datos obtenidos y lo guarda en un archivo
        if(tipo==1):
            with open(padre+".json", "w") as outfile:
                temd={}
                temd["name"]=padre
                temd["type"]="#4D7BD1"
                temd["level"]="#4D7BD1"
                temd["children"]=self.LtoDic(self.listTe)
                outfile.write(json.dumps(temd))
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
                    #print(self.Lvalues[self.contG])
                    return self.Lvalues[self.contG]
                else:
                    dicci[-1]["name"]=lista[cont][1]
                    if(self.tipo==1):
                            dicci[-1]["type"]=self.coloresPa[self.contColor]
                            dicci[-1]["level"]=self.coloresPa[self.contColor]
                    if(type(lista[cont][-1])!=list):
                        dicci[-1]["value"]=self.LtoDic(lista[cont][-1])
                    else:
                        dicci[-1]["children"]=self.LtoDic(lista[cont][-1])
                dicci.append({}) 
            cont+=1
        self.contColor+=1
       
        return dicci
##################################################################################################################################################################################################
    #une las listas de valores, las de las sumas de los hijos con las de sus padres
    def settinVal(self):
        lista=[]
        cont=0
        while(cont<len(self.valuesT)):
            lista.append(self.valuesT[cont][0])
            if(self.tipo==2):
                cont2=0
                while(cont2<len(self.valuesT[cont][1])):
                      lista.append(self.valuesT[cont][1][cont2])
                      lista.extend(self.valuesT[cont][2][cont2])
                      cont2+=1
            else:
                lista.extend(self.valuesT[cont][1])
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
            tot+=float(lista[cont])
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
    def asig(self,lista,parent,pos,Itipo):
            cont4=0
            while(cont4<len(lista)):
                if(lista[cont4]!="" and len(lista[cont4])>0):
                    if(type(lista[cont4]==list)):
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
                            self.asig(lista[cont4][-1],lista[cont4][1],pos+1,Itipo)
                    else:
                        self.ids.append(lista[cont4])
                        self.labels.append(lista[cont4])
                        self.parents.append(parent)
                        self.listPos.append(pos)
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
    def getInf(self,Itipo):
        self.listPos=[]
        self.parents=[""]
        self.VValues=[]
        if(Itipo<0):
           
            self.ids=[self.padre]
            self.labels=[self.padre]
            self.asig(self.listTe,self.padre,0,Itipo)
            cont=0
            self.VValues=self.getValues()
        else:
            self.ids=[self.listTe[Itipo][1]]
            self.labels=[self.listTe[Itipo][1]]
            self.parents=[""]

            self.asig(self.listTe[Itipo][-1],self.listTe[Itipo][1],0,Itipo)
            cont=0
            self.VValues=self.lNums[Itipo]
        self.VValues[0]=1
        return [self.ids,self.labels,self.parents,self.VValues]
    def getListTe(self):
        return self.listTe
    def getSortL(self):
        listTemp=[]
        listTemp.extend(self.listSizes)
        listTemp.sort()
        listTemp.reverse()
        listPosPos=[]
        cont1=0
        cont2=0
        while(cont1<len(listTemp)):
            if(listTemp[cont1]==self.listSizes[cont2]):
                listPosPos.append(cont2)
                cont1+=1
                cont2=0
            else:
                cont2+=1
        return listPosPos
    def getTupla(self):
        cont=0
        tupla="("
        lTemp="("
        while(cont<len(self.listTe)):
            if(cont!=0):
                tupla+=","
            cont2=0
            lTemp="("
            while(cont2<len(self.listTe[cont][-1])):
                if(cont2!=0):
                    lTemp+=","

                lTemp+=self.listTe[cont][-1][cont2][1]+" "+str(round(float(self.listTe[cont][-1][cont2][3])))

                cont2+=1
            tupla+=(lTemp+")")
            cont+=1
        return tupla+");"
        
    def getContinentes(self):
        cont=0
        tupla=[]
        while(cont<len(self.listTe)):
            tupla.append(self.listTe[cont][1])
            cont+=1
            
        return tupla

    def getListaPaises(self):
        cont=0
        tupla=[[]]
        lTemp=[]
        while(cont<len(self.listTe)):
            cont2=0
            while(cont2<len(self.listTe[cont][-1])):
                lTemp.append(self.listTe[cont][-1][cont2][1]+" "+str(round(float(self.listTe[cont][-1][cont2][3]))))
                cont2+=1
            tupla.append(lTemp)
            lTemp=[]
            cont+=1
            
        return tupla
        
    def getListaPaisesPoblacion(self):
        cont=0
        tupla=[[]]
        lTemp=[]
        while(cont<len(self.listTe)):
            cont2=0
            while(cont2<len(self.listTe[cont][-1])):
                lTemp.append(self.listTe[cont][-1][cont2][3])
                cont2+=1
            tupla.append(lTemp)
            lTemp=[]
            cont+=1
            
        return tupla

    def contar(self, m):
        d = 0
        while(m >= 1):
            m = m/10
            d = d+1
        return d
	

