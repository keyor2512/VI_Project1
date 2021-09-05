import plotly.graph_objects as go
import CodigoDesdeCVS
#coloresMainP=["gray","brown","purple","blue","green","black"]
#coloresMainP=["gray","brown","purple","blue","green","black"]
#listasP=CodigoDesdeCVS.obtList("e1","probando",coloresMainP)
listasP=CodigoDesdeCVS.obtList("e1","Origins",1)
print(listasP.getTupla())
#print(len(listasP.getValues()))
paises =go.Figure(go.Icicle(
    ids=listasP.getInf(1)[0],
    labels= listasP.getInf(1)[1],
    parents=listasP.getInf(1)[2],
    root_color="lightblue",
    maxdepth=2,
    textfont=dict(
        family="sans serif",
        size=18,
        color="crimson"
    ),
    
    tiling = dict(
        orientation='v'
        )
))
paises.update_layout(autosize=True)
paises.update_traces(textposition='middle center')

paises.update_layout(
    uniformtext=dict(minsize=10, mode='hide'),
    margin = dict(t=50, l=25, r=25, b=25)
)
paises.update_layout(margin = dict(t=50, l=25, r=25, b=25))
#print(listasP.getLL())
#print(listasP.getLista())
#paises.show()

