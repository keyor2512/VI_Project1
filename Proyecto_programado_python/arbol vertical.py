import plotly.graph_objects as go
import CodigoDesdeCVS
import CodigoDesdeCVS22
coloresMainA=['teal', [[1, '#693933'], [0.5, '#c58f88'], [0, '#ffffff']],
              [[1, '#e74642'], [0.5, '#f3a3a1'], [0, '#ffffff']],
              [[1, '#ac5bb8'], [0.5, '#d5addc'], [0, '#ffffff']],
              [[1, '#49ad4d'], [0.5, '#a2d8a4'], [0, '#ffffff']],
              [[1, '#0075bd'], [0.5, '#5ec2ff'], [0, '#ffffff']],
              [[1, '#ff6c45'], [0.5, '#ffb5a2'], [0, '#ffffff']]]

listasA=CodigoDesdeCVS.obtList("e1","Origins",1)
listasB=CodigoDesdeCVS22.obtList("e1","Origins",1)
cont=0
import numpy as np
Cpadres=6
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
    tiling = dict(orientation='v'),
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
        tiling = dict(orientation='v'),
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
        'text': "Origins 2019",
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
