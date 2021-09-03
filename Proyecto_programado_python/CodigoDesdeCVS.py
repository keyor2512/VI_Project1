import csv
import plotly.graph_objects as go
listTe=[]
listF=[]
salto=False
listpp=[]
cont3=0
cont=1
############################################################
#Datos a cambiar
nombreCSV="data1"
Padre="Probando"
############################################################
ids=[Padre]
labels=[Padre]
parents=[""]
with open("./Datos_Excell/"+nombreCSV+".csv", newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        if(salto):
            listTe.append(row)
            #print(row[-1])
            listpp.append(row[-1])
        else:
            salto=True
            
def splitP(lista):
    count=0
    count2=0
    listT=[]
    if(len(lista)>3):
        listT.append([lista[0][1],[]])
        while len(lista)>0:
            if(lista[0][1]==listT[count2][0]):
               listT[count2][1].append(lista[0][2:])
               lista=lista[1:]
               
            else:
                listT.append([lista[0][1],[]])
                count2+=1
        return listT
    else:
        return          
def splitRecur (lista):
    count2=0
    ll=[]
    if(type(lista)==list):
        if(len(lista)>3):
            while(count2<len(lista)):
                ll=splitP(lista[count2][1])
                lista[count2][1]=splitRecur(ll)
                count2+=1
                
            return lista
        else:
            return
    else:
        return
def getnum(numero):
    return listpp[numero]
def nums(lista):
    global cont3
    listp=[]
    cont4=0
    while(cont4<len(lista)):
        if(type(lista[cont4][1])!=list):
            lista[cont4][1]=getnum(cont3)
            cont3+=1
        else:
            lista[cont4][1]=nums(lista[cont4][1])
        cont4+=1
    return lista
def asig(lista,parent):
    cont4=0
    global ids,parents,labels
    while(cont4<len(lista)):
        if(type(lista[cont4][1])!=list):
            ids.append(lista[cont4][0])
            labels.append(lista[cont4][0])
            parents.append(parent)
        else:
            ids.append(lista[cont4][0])
            labels.append(lista[cont4][0])
            parents.append(parent)
            lista[cont4][1]=asig(lista[cont4][1],lista[cont4][0])
        cont4+=1
    return
asig(nums(splitRecur(splitP(listTe))),Padre)


#grafico
fig =go.Figure(go.Icicle(
 ids=ids,
  labels=labels,
  parents=parents,
    root_color="lightgrey"
))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
