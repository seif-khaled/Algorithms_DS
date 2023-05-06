import re
import math 
string_ex="2+((8+2*3)/2)-1"
expected_output="2823*+2/+1-"
#################################
def infix_to_postfix(string):
    stack=[]
    operators=['+','-','*','/','^']
    # weights={'+':1,'-':1,'*':2,'/':2}
    weights={'+':1,'-':1,'*':2,'/':2,'^':3}
    postfix_expression=""
    index=0
    stack_index=0
    while(index<len(string)):
        # print("inside while 2   ")
        if index==len(string)-1:
            
            if(string[index]!=")"):
                postfix_expression+=string[index]
            # remaning=1
            # print(postfix_expression)
            while(len(stack)!=0):
                if stack[stack_index-1]=='(':
                    stack.pop(stack_index-1)
                    stack_index-=1
                    # pass
                # print(postfix_expression)
                else:
                    
                    postfix_expression+=stack[stack_index-1]
                # print(postfix_expression)
                    stack.pop(stack_index-1)
                    stack_index-=1
                # print(stack)
            
        elif string[index]=='(':
            stack.append(string[index])
            stack_index+=1
        elif string[index]==')':
            # print("found closing brace")
            while(stack[stack_index-1]!='('):
                postfix_expression+=stack[stack_index-1]
                stack.pop(stack_index-1)
                stack_index-=1
                
            if stack[stack_index-1]=='(':
                stack.pop(stack_index-1)
                stack_index-=1
        elif (string[index] not in operators) and (string[index]!='(' and string[index]!=')') :
             postfix_expression+=string[index]
            #  print("i added",postfix_expression)
        elif string[index] in operators:
            if len(stack)==0:
                stack.append(string[index])
                stack_index+=1
                # print(stack)
            elif len(stack)!=0:
                
                if stack[stack_index-1]=='(':
                    stack.append(string[index])
                    stack_index+=1
                    
                elif (stack[stack_index-1] != '(' ) and weights[string[index]] > weights[stack[stack_index-1]]:
                    stack.append(string[index])
                    stack_index+=1
                    # print("stack bigger",stack)
                
                elif  stack[stack_index-1] != '(' and weights[string[index]] <= weights[stack[stack_index-1]]:
                    # print("inside last if",stack[stack_index-1],string[index])
                    flag=0
                    while(flag==0):
                        
                        if((len(stack)==0) or (stack[stack_index-1] == '(' or weights[string[index]]>weights[stack[stack_index-1]])):
                            flag=1
                        
                        elif stack[stack_index-1] != '(' and weights[string[index]]<= weights[stack[stack_index-1]]:
                           
                            postfix_expression+=stack[stack_index-1]
                            stack.pop(stack_index-1)
                            stack_index-=1
                            
                    if((len(stack)==0) or ( (stack[stack_index-1] == '(') or weights[string[index]]>weights[stack[stack_index-1]])) :
                        stack.append(string[index])
                        stack_index+=1
                        
                        
                        
       
        index+=1
    return postfix_expression
# print(infix_to_postfix("((2+3)/20)*6-20"))
# print(infix_to_postfix("((2+3)/20)*6(20/5*9)"))
# print(infix_to_postfix("3*(4+2)*5"))
# print(infix_to_postfix("A*(B+C)/D"))
# print(infix_to_postfix("2+((8+2*3)/2)-1"))
print(infix_to_postfix(("a+b*(c^d-e)^(f+g*h)-i")))
############################################