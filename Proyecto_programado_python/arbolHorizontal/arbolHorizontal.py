import plotly.graph_objects as go
import CodigoDesdeCVS
import CodigoDesdeCVS22
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
colores=["#35a520","#49ab34","#5bb245","#6bb955","#7abf64","#88c674","#96cc83","#a3d392"]
listasA=CodigoDesdeCVS.obtList("e2","Imports",2)
listasB=CodigoDesdeCVS22.obtList("e2","Imports",2)
cont=0
import numpy as np
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
    while(cont<len(listasB.getListTe())+1):
        if(cont==0):
            name="All"
        else:
            name=listasA.getListTe()[cont-1][1]#[:15]+"..."
        LR.append(dict(
            args=[{"visible":Show(cont)}],
            label=name,
            method="update"
            ))
        cont+=1
    
    return LR
cont=0
art.add_trace(go.Icicle(
    ids=listasB.getInf(-1)[0],
    labels=listasB.getInf(-1)[1],
    parents=listasB.getInf(-1)[2],
    values=listasB.getInf(-1)[3],
    root_color="#169e00",
    maxdepth=-1,
    visible=True,
    marker_colorscale = coloresMainA[0],
    textfont=dict(
        family="Times",
        size=15,
        color="black"
    )))
while(cont<Cpadres):
    a=[]
    a.extend(coloresMainA[cont+1])
    a.reverse()
    art.add_trace(go.Icicle(
        ids=listasB.getInf(cont)[0],
        labels=listasB.getInf(cont)[1],
        parents=listasB.getInf(cont)[2],
        values=listasB.getInf(cont)[3],
        root_color="#169e00",
        maxdepth=-1,
        visible=False,
        
        marker_colorscale = a,
        textfont=dict(
            family="Times",
            size=15,
            color="black"
        )))
    cont+=1    

    
art.update_layout(  
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
art.update_layout(margin = dict(t=50, l=25, r=25, b=25))
art.update_traces(textposition='middle center')
art.show()
