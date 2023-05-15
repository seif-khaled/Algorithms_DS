import re
import math 
string_ex="2+((8+2*3)/2)-1"
expected_output="2823*+2/+1-"
##################################
def evaluate_infix(string):
    operators=['+','-','*','/','^']
    parnatheises_stack=[]
    parnatheises_stack_index=0
    if (len(string)==0) or (string[0] in operators) or (string[len(string)-1] in operators):
        return "invalid expression",False
    else:
        double_operator=0
        same_operator=0
        unequal_parantheises=0
        for i in range(len(string)):
            if i==len(string)-1:
                break
            if string[i]==string[i+1] and string[i] in operators:
                same_operator=1
                return "same operator found consecutively",False
            elif string[i] in operators and string[i+1] in operators:
                double_operator=1
                return "double operator found consecutively",False
        for i in range(len(string)) :
            if i==len(string)-1 and len(parnatheises_stack)>0:
                unequal_parantheises=1
                return "unbalanced parantheises found",False
                
            if string[i]=='(':
                parnatheises_stack.append(string[i])
                parnatheises_stack_index+=1
            elif string[i]==')':
                if len(parnatheises_stack)!=0:
                    parnatheises_stack.pop(parnatheises_stack_index-1)
                    parnatheises_stack_index-=1
                elif len(parnatheises_stack)==0:
                    unequal_parantheises=1
                    return "unbalanced parantheises found",False
        if unequal_parantheises==0 and same_operator==0 and double_operator==0:
            return "expression is valid",True 
                
                                
# print(evaluate_infix("/(/(1*2)-*"))

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
                 postfix_expression+=" "
                 postfix_expression+=string[index]
                 postfix_expression+" "
                 last_operand_index=index
             elif last_operand_index==0 or (index -last_operand_index)==1:
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
# print(infix_to_postfix("A*(B+C)/D"))
# print(infix_to_postfix("(~a^~b)v(~c)"))
# print(infix_to_postfix("~((a^b)^(fvcc))"))
print(infix_to_postfix("(~a^c)vf ^ ((xvyvz)^(~avy))"))
# print(infix_to_postfix("15+20*30"))
# print(infix_to_postfix("((A+B)-C*(D/E))+F"))
# print(infix_to_postfix("((A + Bver) - C * (D / E)) + F"))
# print(infix_to_postfix("((F+R)-(p^(a-s)))"))
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

# x=[1,2,3,4,2,2]
# x.remove(2)
# print(x)