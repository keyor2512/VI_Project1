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
ids=listasA.getIds()
parents=listasA.getParents()
labels=[]
cont=0
while(cont<len(listasA.getLabels())):
    labels.append(listasA.getLabels()[cont]+" :"+str(listasA.getValues()[cont]))
    cont+=1
art =go.Figure(go.Icicle(
    ids=ids,
    labels=labels,
    parents=parents,
    #values=values,
    #marker_colors = listas.getColors()
    root_color="lightblue",
    maxdepth=2,
    textfont=dict(
        family="Times",
        size=20,
        color="black"
    )
    #,autosize=False
    #,branchvalues = "total"
    
))
art.update_layout(  
    uniformtext=dict(minsize=10, mode='hide'),
    margin = dict(t=50, l=25, r=25, b=25)
)
#art.update_xaxes(autorange=False)
#art.update_xaxes(categoryorder="category ascending")
#art.update_layout(margin = dict(t=50, l=25, r=25, b=25))
art.update_traces(textposition='middle center')
art.show()
