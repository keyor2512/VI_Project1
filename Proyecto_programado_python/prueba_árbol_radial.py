import random
from ete3 import Tree, TreeStyle, NodeStyle, faces, AttrFace, CircleFace, TextFace
import CodigoDesdeCVS
import math

# Excell 
listasP=CodigoDesdeCVS.obtList("/home/kali/Desktop/RepoElectiva/VI_Project1/Proyecto_programado_python/e1","Origins",1)

# Create a faces ready to read the name attribute of nodes
#nameFace = faces.AttrFace("name", fsize=20, fgcolor="#009000")

# # Coloco labels
# labels = listasP.getContinentes()   
# hash = {}

# for i in labels:
#     hash.setdefault(i,0)

def layout(node):
    if node.is_leaf():
        # Add node name to laef nodes
        N = AttrFace("name", fsize=14, fgcolor="black")
        faces.add_face_to_node(N, node, 0)

        # print(labels)
        #Label
        # longNameFace = faces.TextFace(hash.get(node.name,"name"))
        # faces.add_face_to_node(longNameFace, node, column=0)

        # # Sets the style of leaf nodes
        # node.img_style["size"] = 12
        # node.img_style["shape"] = "circle"
        # node.img_style["fgcolor"] = "#000000"
    #If node is an internal node
    # else:
    #     # Sets the style of internal nodes
    #     node.img_style["size"] = 6
    #     node.img_style["shape"] = "circle"
    #     node.img_style["fgcolor"] = "#000000"

    if "weight" in node.features:
        # Creates a sphere face whose size is proportional to node's
        # feature "weight"
        C = CircleFace(radius=node.weight, color="RoyalBlue", style="sphere")
        # Let's make the sphere transparent
        C.opacity = 0.3
        #C.label = 
    
        # And place as a float face over the tree
        faces.add_face_to_node(C, node, 0, position="float")



def get_example_tree():
    # Random tree
    #listasP.getTupla().replace(" ","_")
    t = Tree(listasP.getTupla())

    # Some random features in all nodes
    cont = 0
    num = 0
    ct = 0
    poblaciones = listasP.getListaPaisesPoblacion()
    poblaciones.pop(0)
    largo = len(poblaciones)
    for n in t.traverse():
        n.add_features(weight=random.randint(0,50))
        # a = n.get_leaf_names
        # print(type(a))
        # largo_lista_interna = len(poblaciones[ct])
        # if largo_lista_interna != 13 and num != 13 and ct != 5:
            

        #     if num == largo_lista_interna:
        #         ct = ct+1
        #         num = 0

        #     cont = listasP.contar(round(float(poblaciones[ct][num])))
        #     print(ct)
        #     print(cont)
        #     print(num)
        #     print(largo_lista_interna)
        #     #print(str(round(float(poblaciones[ct][num]))))
        #     # if num >= largo_lista_interna:
        #     #     n.add_features(weight=10)
        #     # else:
        #     #cont = listasP.contar(round(float(poblaciones[ct][num])))
            

        #     if cont == 1:
        #         n.add_features(weight=6)
        #     elif cont == 2:
        #         n.add_features(weight=9)
        #     elif cont == 3:
        #         n.add_features(weight=12)
        #     elif cont == 4:
        #         n.add_features(weight=13)
        #     elif cont == 5:
        #         n.add_features(weight=15)
        #     elif cont == 6:
        #         n.add_features(weight=19)
        #     elif cont == 7:
        #         n.add_features(weight=23)
        #     elif cont == 8:
        #         n.add_features(weight=26)
        #     elif cont == 9:
        #         n.add_features(weight=29)
                
        #     num += 1
            

    # Create an empty TreeStyle
    ts = TreeStyle()

    # Set our custom layout function
    ts.layout_fn = layout

    # Draw a tree
    ts.mode = "c"

    # We will add node names manually
    ts.show_leaf_name = False

    # Coloco labels
    t.add_face(TextFace( listasP.getContinentes() ),column=0,position = "branch-top")

    # Colores
    nst1 = NodeStyle()
    nst1["bgcolor"] = "LightSteelBlue"
    nst2 = NodeStyle()
    nst2["bgcolor"] = "Moccasin"
    nst3 = NodeStyle()
    nst3["bgcolor"] = "DarkSeaGreen"
    nst4 = NodeStyle()
    nst4["bgcolor"] = "pink"
    nst5 = NodeStyle()
    nst5["bgcolor"] = "brown"
    nst6 = NodeStyle()
    nst6["bgcolor"] = "yellow"

    for n in t.traverse():
        n.dist = 0

    tree = listasP.getListaPaises()
    
    n1 = t.get_common_ancestor(tree[1])
    n1.set_style(nst1)  
    n2 = t.get_common_ancestor(tree[2])
    n2.set_style(nst2)
    n3 = t.get_common_ancestor(tree[3])
    n3.set_style(nst3)
    n4 = t.get_common_ancestor(tree[4])
    n4.set_style(nst4)
    n5 = t.get_common_ancestor(tree[5])
    n5.set_style(nst5)
    n6 = t.get_common_ancestor(tree[6])
    n6.set_style(nst6)

    ts.root_opening_factor = 1
    # Show branch data
    #ts.show_branch_length = True
    #ts.show_branch_support = True

    
    
    return t, ts

if __name__ == "__main__":
    t, ts = get_example_tree()

    #t.render("bubble_map.png", w=600, dpi=300, tree_style=ts)
    t.show(tree_style=ts)



#cont=0
    #for i in t.traverse():
        #if labels.__len__ == cont:
        #    break
        #else:
            #t.add_face(TextFace(labels[i]), column=i, position = "branch-bottom")
            #i.add_face(TextFace(labels[cont]), column=cont, position = "branch-bottom")
            #cont+=1
    
    #print(labels)
