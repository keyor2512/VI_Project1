import plotly.graph_objects as go
import CodigoDesdeCVS
#coloresMainA=["gray","brown","purple","blue","green","black","pink","orange","red","gray","brown","green","yellow","gray","brown","pink","red","purple","brown","black","red"]
#coloresMainP=["gray","brown","purple","blue","green","black"]
listasA=CodigoDesdeCVS.obtList("e2","probando",2)
#listasA=CodigoDesdeCVS.obtList("e2","probando",coloresMainA)
#print(listasA.getValues()[:100])
#print(listasA.getIds()[-1])
#print(listasA.getParents()[-1])
#values=listasA.getValues()
cont=0
#print(values[0])
#ids=listasA.getIds()
#parents=listasA.getParents()
#labels=[]
#cont=0
#while(cont<len(listasA.getLabels())):
 #   labels.append(listasA.getLabels()[cont]+" :"+str(listasA.getValues()[cont]))
  #  cont+=1
  
ll=listasA.getInf(20)[1]
ll[0]="das"
Cpadres=21
art =go.Figure()
def Show(num):
    global Cpadres
    lista=[]
    cont=0
    while(cont<Cpadres+1):
        if(cont==num):
            lista.append(True)
        else:
            lista.append(False)
        cont+=1
    return lista

def getDicButt():
    global Cpadres
    cont=0
    LR=[]
    while(cont<len(listasA.getListTe())+1):
        
        if(cont==0):
            name="All"
        else:
            name=listasA.getListTe()[cont-1][1]
        
        LR.append(dict(
            args=[{"visible":Show(cont)}],
            label=name,
            method="update"
            ))
        cont+=1
    
    return LR
cont=0
art.add_trace(go.Icicle(
    ids=listasA.getInf(-1)[0],
    labels=listasA.getInf(-1)[1],
    parents=listasA.getInf(-1)[2],
    root_color="lightblue",
    maxdepth=2,
    visible=True,
    textfont=dict(
        family="Times",
        size=30,
        color="black"
    )))
while(cont<Cpadres):  
    art.add_trace(go.Icicle(
        ids=listasA.getInf(cont)[0],
        labels=listasA.getInf(cont)[1],
        parents=listasA.getInf(cont)[2],
        #values=values,
        #marker_colors = listas.getColors()
        root_color="lightblue",
        maxdepth=2,
        visible=False,
        textfont=dict(
            family="Times",
            size=30,
            color="black"
        )))
    cont+=1    

    
art.update_layout(  
    uniformtext=dict(minsize=10, mode='hide'),
    margin = dict(t=50, l=25, r=25, b=25),
    
    
)


art.update_layout(
    updatemenus=[
        dict(
            type = "buttons",
            direction = "up",
            buttons=list(getDicButt()),
            pad={"r": 0, "t": 0},
            showactive=True,
            x=0,
            xanchor="right",
            y=1,
            yanchor="top"
        ),
    ]
)
print({"data"})

#art.update_xaxes(autorange=False)
#art.update_xaxes(categoryorder="category ascending")
#art.update_layout(margin = dict(t=50, l=25, r=25, b=25))
art.update_traces(textposition='middle center')
art.show()
