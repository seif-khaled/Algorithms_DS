import re
import math 
string_ex="2+((8+2*3)/2)-1"
expected_output="2823*+2/+1-"
#################################
def infix_to_postfix(string):
    stack=[]
    # operators=['+','-','*','/','^']
    operators=['v','~','^']
    weights={'~':3,'^':2,'v':1}
    # weights={'+':1,'-':1,'*':2,'/':2,'^':3}
    postfix_expression=""
    output_queue=[]
    output_queue_index=0
    last_operand_index=0
    current_operand_index=0
    index=0
    stack_index=0
    while(index<len(string)):
        if index==len(string)-1:
            #in case you are working with the repetition sign * like in theory or in regex patterns remove the part which says string[index] not in operators in line 25
            if(string[index]!=")") and (string[index]!='(') and (string[index] not in operators):
                postfix_expression+=string[index]
                postfix_expression+=" "
            while(len(stack)!=0):
                if stack[stack_index-1]=='(':
                    stack.pop(stack_index-1)
                    stack_index-=1
                else:
                    postfix_expression+=" "
                    postfix_expression+=stack[stack_index-1]
                    postfix_expression+=" "
                    stack.pop(stack_index-1)
                    stack_index-=1
                # print(stack)
            
        elif string[index]=='(':
            stack.append(string[index])
            stack_index+=1
        elif string[index]==')':
            # print("found closing brace")
            while(stack[stack_index-1]!='('):
                postfix_expression+=" "
                postfix_expression+=stack[stack_index-1]
                postfix_expression+=" "
                stack.pop(stack_index-1)
                stack_index-=1
                
            if stack[stack_index-1]=='(':
                stack.pop(stack_index-1)
                stack_index-=1
        elif (string[index] not in operators) and (string[index]!='(' and string[index]!=')') :
             if (index -last_operand_index)>1:
                 print("diffrence betwene operands is huge",string[index])
                 postfix_expression+=" "
                 postfix_expression+=string[index]
                 postfix_expression+" "
                 last_operand_index=index
             elif last_operand_index==0 or (index -last_operand_index)==1:
                print("diffrencer betwen operands is okay",string[index])
                postfix_expression+=string[index]
                last_operand_index=index
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
                
                elif  stack[stack_index-1] != '(' and weights[string[index]] <= weights[stack[stack_index-1]]:
                    flag=0
                    while(flag==0):
                        
                        if((len(stack)==0) or (stack[stack_index-1] == '(' or weights[string[index]]>weights[stack[stack_index-1]])):
                            flag=1
                        
                        elif stack[stack_index-1] != '(' and weights[string[index]]<= weights[stack[stack_index-1]]:
                            postfix_expression+=" "
                            postfix_expression+=stack[stack_index-1]
                            postfix_expression+=" "
                            stack.pop(stack_index-1)
                            stack_index-=1
                            
                    if((len(stack)==0) or ( (stack[stack_index-1] == '(') or weights[string[index]]>weights[stack[stack_index-1]])) :
                        stack.append(string[index])
                        stack_index+=1
                        
       
        index+=1
    return postfix_expression.split()
# print(infix_to_postfix("((2+3)/20)*6-20"))
# print(infix_to_postfix("((2+3)/20)*6(20/5*9)"))
# print(infix_to_postfix("3*(4+2)*5"))
# print(infix_to_postfix("A*(B+C)/D"))
# print(infix_to_postfix("2+((8+2*3)/2)-1")=="2823*+2/+1-")
# print(infix_to_postfix("2+((8+2*3)/2)-1"))
# print(infix_to_postfix(("a+b*(c^d-e)^(f+g*h)-i")))
# print(infix_to_postfix("a^bvc"))
# print(infix_to_postfix("(~a^~b)v(~c)"))
print(infix_to_postfix("~((a^b)^(fvcc))"))
# print(infix_to_postfix("15+20*30"))
# print(infix_to_postfix("11^(12^13)"))
# print(("1 2    3 4     5").split())
############################################
# def evaluate_postifx(post_string):
#     index=0
#     stack=[]
#     operators=[]
#     while(index<len(post_string)):
#         if post_string[index] not in operators:
#             stack.append()
#         index+=1