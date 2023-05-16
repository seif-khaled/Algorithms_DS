import math
import random
def generate_random_arr(size):
    return [random.randrange(100,50) for i in range(0,size) ]

def binary_search(arr,element):
    low=0
    high=len(arr)-1
    mid=int((low+high)/2)
    flag=0
    while(flag==0):
        if high<low:
            flag=1
            return -1
        if element==arr[mid]:
            flag=1
            return mid
        else:
            if element<arr[mid]:
                high=mid-1
            elif element>arr[mid]:
                low=mid+1
        mid=int((low+high)/2)

# index=eval((input()))
# x=["FizzBuzz" if i %3 ==0 and i%5 ==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i  for i in range(1,index+1)]
# print(x)
##############################
# x=generate_random_arr(1000)
# element=random.choice(x)
# x.sort()
# print(x)
# print(element)