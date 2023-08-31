class myarray:
    def __init__(self,arr=[],leng=0):
        self.arr=arr
        # self.arr=sorted(self.arr)
        self.leng=len(arr)
    def ADD(self,item):
        self.arr=self.arr+[item]
        self.leng+=1
    def POP(self):
        # self.arr=self.arr[0:self.leng-1]
        del self.arr[self.leng-1]
        self.leng-=1
    def print_array(self):
        return self.arr,self.leng
    def ins(self,item,index):
        if index>=self.leng:
            print("index out of range")
        else:
            temp=self.arr[index]
            if self.leng-1==index:
                # print("hi")
                self.arr[index]=item
                self.arr=self.arr+[temp]
                self.leng+=1
            else:
                right=self.arr[index:]
                left=self.arr[0:index]
                self.arr=left+[item]+right
                self.leng+=1
    

                
    def find_item(self,item):
        #linear search
        for i in range(len(self.arr)):
            if self.arr[i]==item:
                return True,i
        return False,-1
        #binary search(array needs to be sorted )
        # self.arr=sorted(self.arr)
        # low=0
        # high=len(self.arr)-1
        # mid=int((low+high)/2)
        # flag=0
        # while(flag==0):
        #     if high<low:
        #         flag=1
        #         return -1
        #     if item==self.arr[mid]:
        #         flag=1
        #         return mid
        #     else:
        #         if item<self.arr[mid]:
        #             high=mid-1
        #         elif item>self.arr[mid]:
        #             low=mid+1
        #     mid=int((low+high)/2)
        
        



arr=myarray([1,4,5,6],4)
print(arr.find_item(4))
arr.ADD(10)
arr.POP()
arr.ins(12,1)
print(arr.find_item(4))
arr.POP()
print(arr.find_item(4))
print(arr.print_array())