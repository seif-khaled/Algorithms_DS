import math 
import graphviz
import sys
class dijkst:

    def __init__(self,nodes,graph,src):
        self.nodes=nodes
        self.graph=graph
        self.selected_nodes=[]
        self.nodes_values={}
        self.src=src
        for i in range(len(nodes)):
            if i==0:
                self.nodes_values[self.src]=0
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
                # print("yes")
                # sys.exit()
            else:
                return smallest_node
        
        
    def find_all_adjacent_edges(self):
        current_node=self.find_minimum_select_node()
        if current_node=="done exeuction":
            return "done execution"
        else:    
            # current_node=self.find_minimum_select_node()
            # print(current_node)
            adjacent_nodes=self.graph[current_node]
            return current_node,adjacent_nodes
        
     
    def calculate_edges_assign_new_values_to_nodes(self):
        current_node_with_adjaccent_nodes=self.find_all_adjacent_edges()
        
        # print(current_node_with_adjaccent_nodes)
        if current_node_with_adjaccent_nodes=="done execution":
            return self.flag
        else:    
            # current_node_with_adjaccent_nodes=self.find_all_adjacent_edges()
            for i in self.graph[current_node_with_adjaccent_nodes[0]]:
                next_node=i
                # print(i)
                # print(current_node_with_adjaccent_nodes[0][i])
                res=self.nodes_values[current_node_with_adjaccent_nodes[0]]+current_node_with_adjaccent_nodes[1][i]
                if res<self.nodes_values[next_node]:
                    self.nodes_values[next_node]=res
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
src='A'
#################################
x=dijkst(nodes,graph,src)
x.execute()

for i in x.nodes_values:
    print(i,x.nodes_values[i])

# print(x.nodes_values)


#######################
# print(graph)
# for i in graph:
#     print(i,graph[i])
# print(('a',{'c':14,'d':5}))
        
            
        
                
        
        # self.nodes_values={0:0}
    
    
    
    
    
# x={0:0}
# print(x[0])