class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None






class LinkedList:
    def __init__(self):
        self.n=None
        self.head=None
    def insert_list_at_end(self,l):
        if self.head==None:
            for i in range(len(l)):
                if self.head!=None:
                    current=self.head
                    while(current.next!=None):
                        current=current.next
                    current.next=Node(l[i])
                else:
                    self.head=Node(l[i])
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            for i in range(len(l)):
                if i==0:
                    current.next=Node(l[i])
                elif i>0:
                    current=self.head
                    while(current.next!=None):
                        current=current.next
                    current.next=Node(l[i])
    def insert_at_begin(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            current=Node(data)
            current.next=self.head
            self.head=current
    def print_linked_list(self):
        current=self.head
        while(current!=None):
            print(current.data,end=" ")
            current=current.next
    def print_head(self):
        print("head:",self.head.data)
    def insert_at_index(self,data,indx):
        current=self.head
        n=Node(data)
        i=0
        if (indx==0):
            self.insert_at_begin(data)
        else:
            while(i+1 != indx and current!= None):
                current=current.next
                i+=1
            if current!= None:
                n.next=current.next
                current.next=n
            else:
                print(" index out of range")
    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            current=self.head
            n=Node(data)
            while(current.next!=None):
                current=current.next
            current.next=n
    def show_item(self,indx):
        i=0
        current=self.head
        while(True):
            if current==None:
                print("index out of range")
                break
            if i==indx and current!=None:
                print("node at index ",i,"equals ",current.data)
                break
            else:
                current=current.next
                i+=1
    def delete_node(self,indx):
        i=0
        current=self.head
        prev=None
        if indx==0:
            self.head=current.next
            current=None
        else:
            while(True):
                if current==None:
                    print("index out of range")
                    break
                if i==indx and current!=None:
                    prev.next=current.next
                    current=None
                    break
                else:
                    i+=1
                    prev=current
                    current=current.next
            
                
        
        
        
                           

x=LinkedList()
x.insert_at_begin(5)
x.insert_at_begin(3)
# # x.insert_at_begin(8)
# # x.insert_at_index(7,1)
x.insert_at_end(18)
x.insert_list_at_end([24,9,6,266])
# x.print_head()
# x.delete_node(1)
x.delete_node(5)
x.delete_node(5)
# x.delete_node(3)
# x.print_head()
# x.show_item(2)
x.print_linked_list()

            



