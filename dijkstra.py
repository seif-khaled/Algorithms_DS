import math 
import graphviz
from graphviz import Digraph
class dijkst:

    def __init__(self,nodes,graph,src):
        self.nodes=nodes
        self.graph=graph
        self.selected_nodes=[]
        self.nodes_values={}
        self.src=src
        self.adjancy_mat={}
        # self.adjancy_mat[self.src]={}
        for i in range(len(nodes)):
            if i==0:
                self.nodes_values[self.src]=0
                if nodes.index(self.src)>0:
                    self.nodes_values[self.nodes[i]]=math.inf
            else:
                if self.nodes[i]==self.src:
                    continue
                else:
                    self.nodes_values[self.nodes[i]]=math.inf
        self.min=self.nodes_values[src]
        self.at_src_node=1
        self.flag=0
        
    def find_minimum_select_node(self):
        if self.at_src_node==1:
            self.selected_nodes.append(self.src)
            self.at_src_node=0
            smallest_node=self.src
            return smallest_node
        else:
            self.min=math.inf
            smallest_node=-1
            for i in self.nodes_values:
                if i not in self.selected_nodes:
                    if self.nodes_values[i]<self.min:
                        self.min=self.nodes_values[i]
                        smallest_node=i
            self.selected_nodes.append(smallest_node)
            if smallest_node==-1:
                self.flag=1
                return "done exeuction"
            else:
                return smallest_node
        
        
    def find_all_adjacent_edges(self):
        current_node=self.find_minimum_select_node()
        if current_node=="done exeuction":
            return "done execution"
        else:    
            adjacent_nodes=self.graph[current_node]
            return current_node,adjacent_nodes
        
     
    def calculate_edges_assign_new_values_to_nodes(self):
        current_node_with_adjaccent_nodes=self.find_all_adjacent_edges()
        if current_node_with_adjaccent_nodes=="done execution":
            return self.flag
        else:    
            for i in self.graph[current_node_with_adjaccent_nodes[0]]:
                next_node=i
                
                res=self.nodes_values[current_node_with_adjaccent_nodes[0]]+current_node_with_adjaccent_nodes[1][i]
                if res<self.nodes_values[next_node]:
                    self.nodes_values[next_node]=res
            self.adjancy_mat[current_node_with_adjaccent_nodes[0]]={}
            for i in self.nodes:
                self.adjancy_mat[current_node_with_adjaccent_nodes[0]][i]=self.nodes_values[i]
                
            
    def execute(self):
            while(self.flag==0):
                x=self.calculate_edges_assign_new_values_to_nodes()
                if x==1:
                    break
                
#test case 1       
# graph={'A':{'B':2,'C':3},'B':{'C':4},'C':{}}
# nodes=['A','B','C']
# src='A'


#test case 2
graph={'A':{'B':2,'C':4},'B':{'D':7,'C':1},'C':{'E':3},'D':{'F':1},'E':{'F':5,'D':2},'F':{}}
nodes=['A','B','C','D','E','F']
src='E'

#test case 3 
# graph={'A':{'B':5,'D':3,'E':1},'B':{},'C':{'E':11},'D':{},'E':{}}
# nodes=['A','B','C','D','E']
# src='A'
#################################
# x=dijkst(nodes,graph,src)
# x.execute()
# print("distance form the source")
# for i in x.nodes_values:
#     print(i,x.nodes_values[i])
##########################################
x=dijkst(nodes,graph,src)
x.execute()
# print(sele)
print("\n")
print("selected\t", "edges")
# print("distance form the source")
for i in x.adjancy_mat:
    print(i,'\t',x.adjancy_mat[i])

print("\nvalues from source node ")
for i in x.nodes_values:
    print(i,x.nodes_values[i])
    
    
    
#####graph represenation###########
dot = Digraph()

for node in nodes:
    if node == src:
        dot.node(node, color='red', style='filled')
    else:
        dot.node(node)

for node, edges in graph.items():
    for neighbor, weight in edges.items():
        dot.edge(node, neighbor, label=str(weight))

dot.render('graph', format='pdf', view=True)


#######################


    