import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
df = pd.read_csv('e2.csv')
ll=df.Trade_Value.array
total=0
cont=0
while(cont<len(ll)):
    total+=ll[cont]
    cont+=1
print("ddd")
print(total)
def obList(lista):
    lista2=[]
    lista2.append(lista[0])
    count=0
    while(count<len(lista)):
        if(lista2[-1]!=lista[count]):
            lista2.append(lista[count])
        count+=1
    return lista2
ids=["Prueba"]
ids.extend(obList(df.Section.array))
ids.extend(obList(df.HS2.array))
ids.extend(obList(df.HS4.array))
ids.extend(obList(df.HS6.array))
labels=ids
parents=[""]
lv=[]
cont=0
while(cont<len(obList(df.Section.array))):
    lv.append("Prueba")
    cont+=1
parents.extend(lv)
parents.extend(df.Section.array)
parents.extend(df.HS2.array)
parents.extend(df.HS4.array)

print(len(labels))
print(len(parents))
art =go.Figure(go.Icicle(
    ids=ids,
    labels=labels,
    parents=parents,
    #marker_colors = listas.getColors()
    root_color="lightblue",
    textfont=dict(
        family="sans serif",
        size=18,
        color="crimson"
    )
))
art.update_layout(
    #uniformtext=dict(minsize=10, mode='hide'),
    margin = dict(t=50, l=25, r=25, b=25)
)


art.update_layout(margin = dict(t=50, l=25, r=25, b=25))
art.update_traces(textposition='middle center')
#art.show()



