import plotly.graph_objects as go
import CodigoDesdeCVS

coloresMainA=['blugrn', [[1, '#e74642'], [0.5, '#f3a3a1'], [0, '#ffffff']],
              [[1, '#49ad4d'], [0.5, '#a2d8a4'], [0, '#ffffff']],
              [[1, '#ff6c45'], [0.5, '#ffb5a2'], [0, '#ffffff']],
              [[1, '#e60e14'], [0.5, '#f78285'], [0, '#ffffff']],
              [[1, '#6c6c6c'], [0.5, '#b5b5b5'], [0, '#ffffff']],
              [[1, '#9fd236'], [0.5, '#cfe99b'], [0, '#ffffff']],
              [[1, '#0075bd'], [0.5, '#5ec2ff'], [0, '#ffffff']],
              [[1, '#753027'], [0.5, '#d2847b'], [0, '#ffffff']],
              [[1, '#693933'], [0.5, '#c58f88'], [0, '#ffffff']],
              [[1, '#736d6c'], [0.5, '#b9b6b5'], [0, '#ffffff']],
              [[1, '#ac5bb8'], [0.5, '#d5addc'], [0, '#ffffff']],
              [[1, '#6a44c0'], [0.5, '#b5a2e0'], [0, '#ffffff']],
              [[1, '#58565f'], [0.5, '#aba9b1'], [0, '#ffffff']],
              [[1, '#2ab7a9'], [0.5, '#8be4dc'], [0, '#ffffff']],
              [[1, '#c1c7cb'], [0.5, '#e0e3e5'], [0, '#ffffff']],
              [[1, '#812b43'], [0.5, '#d58098'], [0, '#ffffff']],
              [[1, '#363d95'], [0.5, '#8e93d6'], [0, '#ffffff']],
              [[1, '#955936'], [0.5, '#d6a88e'], [0, '#ffffff']],
              [[1, '#e74642'], [0.5, '#f3a3a1'], [0, '#ffffff']],
              [[1, '#5a9536'], [0.5, '#a9d68e'], [0, '#ffffff']],
              [[1, '#b72828'], [0.5, '#e58989'], [0, '#ffffff']]]
#coloresMainP=["gray","brown","purple","blue","green","black"]
listasA=CodigoDesdeCVS.obtList("e2","Imports",2)
#listasA=CodigoDesdeCVS.obtList("e2","probando",coloresMainA)
#print(listasA.getValues()[:100])
#print(listasA.getIds()[-1])
#print(listasA.getParents()[-1])
#values=listasA.getValues()
cont=0
import numpy as np
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
    values=listasA.getInf(-1)[3],
    
    #color=np.log10(listasA.getInf(-1)[3][0]),
    #color_continuous_scale=["red", "green", "blue"],
   # marker=dict(
       # colors=coloresMainA,
       # colorscale='RdBu',
       # cmid=listasA.getInf(-1)[3]),
    
    #color_continuous_midpoint=np.average(values=listasA.getInf(-1)[3]),
    #values=listasA.getInf(-1)[3],
    root_color="lightblue",
    maxdepth=2,
    visible=True,
    marker_colorscale = coloresMainA[0],
    textfont=dict(
        family="Times",
        size=30,
        color="black"
    )))
while(cont<Cpadres):
    a=[]
    a.extend(coloresMainA[cont+1])
    a.reverse()
    art.add_trace(go.Icicle(
        ids=listasA.getInf(cont)[0],
        labels=listasA.getInf(cont)[1],
        parents=listasA.getInf(cont)[2],
        values=listasA.getInf(cont)[3],
        
       # marker=dict(
          #  colors=coloresMainA,
          #  colorscale='RdBu',
          #  cmid=listasA.getInf(cont)[3]),
        #color_continuous_midpoint=np.average(listasA.getInf(cont)[3]),
        #marker_colors = listas.getColors()
        root_color="lightblue",
        maxdepth=2,
        visible=False,
        
        marker_colorscale = a,
        textfont=dict(
            family="Times",
            size=40,
            color="black"
        )))
    print(cont)
    cont+=1    

    
art.update_layout(  
    uniformtext=dict(minsize=10, mode='hide'),
   title={
        'text': "Imports 2019",
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Courier New, monospace",
        size=15,
        color="RebeccaPurple"),
    height=845,
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
print(listasA.getSortL())

#art.update_xaxes(autorange=False)
#art.update_xaxes(categoryorder="category ascending")
art.update_layout(margin = dict(t=50, l=25, r=25, b=25))
art.update_traces(textposition='middle center',textfont=dict(
        family="times",
        size=30))
art.show()
