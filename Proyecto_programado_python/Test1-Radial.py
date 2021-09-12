#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                       Visualización de Información
#                                                           By Keylor&Jeremy
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
import plotly.express as px
import pandas as pd
import json 
ruth="C:\\Users\\Jerem\\Documents\\Repositorios\\VI_Project1\\Proyecto_programado_python\\exports.json"
colum_HS4=[]
colum_values = []
colum_sections=[]
colum_HS2=[]
# Seteo datos en las variables
with open(ruth) as json_file:
    for pColum in json.load(json_file):
        colum_sections.append(pColum['Section'])
        colum_HS2.append(pColum['HS2'])
        colum_HS4.append(pColum['HS4'])
        colum_values.append(pColum['Trade Value'])
df=pd.DataFrame(dict(sections=colum_sections, HS2=colum_HS2, HS4=colum_HS4, values=colum_values))
df["products"] = "Export 2019"
# Figuro como graficar con colores claros, siguiendo la tematica del contexto de la informacion y el impacto que tendra al leerla el usuario.
fig=px.sunburst(df, path=['products', 
                            'sections', 
                            'HS2', 
                            'HS4'], 
                    values='values', 
                    color='sections', 
                    color_discrete_map={'Wood Products':'#DB9567', 
                                     'Animal Products':'#F5E49A', 
                                     'Foodstuffs':'#A4E0CD', 
                                     'Vegetable Products':'#C8FF90',
                                     'Animal and Vegetable Bi-Products':'#A58CA6',
                                     'Mineral Products':'#67B6DB',
                                     'Chemical Products':'#FFA033',
                                     'Plastics and Rubbers':'#ADA8B6',
                                     'Animal Hides':'#F8C992',
                                     'Paper Goods':'#DFFCF6',
                                     'Textiles':'#818FDB',
                                     'Footwear and Headwear':'#FFD0B5',
                                     'Stone And Glass':'#DEE092',
                                     'Precious Metals':'#C3D0E0',
                                     'Metals':'#A2A0A3',
                                     'Machines':'#6C786E',
                                     'Transportation':'#9A69FA',
                                     'Instruments':'#DEC76A',
                                     'Weapons':'#945962',
                                     'Miscellaneous':'#394A5C',
                                     'Arts and Antiques':'#A1CAF0'}) # Se evaluo que los colores fuersen agradables a la vista, todos por igual.
fig.show()
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                       Visualización de Información
#                                                           By Keylor&Jeremy
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------


# (function) sunburst: (data_frame=None, names=None, values=None, parents=None, path=None, ids=None, 
#                     color=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, 
#                     color_discrete_sequence=None, color_discrete_map=None, hover_name=None, hover_data=None, 
#                     custom_data=None, labels=None, title=None, template=None, width=None, height=None, branchvalues=None,
#                     maxdepth=None) -> (FigureWidget | Any)

#Colores claros
#F1EE59, #D98A50, #EB65F0, #568ADB, #67FF8B, #5BD4DB, #DB3705

#Funcion para convertir de csv a excell

#import csv 

# def csv_to_json(csvFilePath, jsonFilePath):
#     jsonArray = []
      
#     with open(csvFilePath, encoding='utf-8') as csvf: 
#         csvReader = csv.DictReader(csvf) 

#         for row in csvReader: 
#             jsonArray.append(row)
  
#     with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
#         jsonString = json.dumps(jsonArray, indent=4)
#         jsonf.write(jsonString)
          
# csvFilePath = r'C:\\Users\\Jerem\\Documents\\Repositorios\\VI_Project1\\Proyecto_programado_python\\exports.csv'
# jsonFilePath = r'C:\\Users\\Jerem\\Documents\\Repositorios\\VI_Project1\\Proyecto_programado_python\\exports.json'
# #csv_to_json(csvFilePath, jsonFilePath)

























# import CodigoDesdeCVS
# listasP=CodigoDesdeCVS.obtList("\\Users\\Jerem\\Documents\\Repositorios\\VI_Project1\\Datos_Excell\\e2","Origins",1)

#print(listasP.listTe)

#print(listasP.getSortL())
#[15, 5, 4, 6, 14, 16, 17, 3, 9, 1, 10, 19, 0, 12, 11, 8, 13, 2, 7, 18, 20]

# listasP.getResultTreeRadial()

# print( listasP.list_products_1 )
# print( listasP.list_products_2 )
# print( listasP.list_products_3 )

