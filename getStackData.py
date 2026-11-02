#Network Port-Matrix Automation Tool - getStackData.py


#This module defines the get_stackData() function 

#This function creates a a dictionary FOR EACH STACK in the site 
#A switch-count key-value pair is assigned to each stack
#The stack_data variable is returned as NESTED dictonary data type
#Example: stack_data = {
#           'stk1':{'sw_count':3}, 
#           'stk2':{'sw_count':4}
#            }


def get_stackData(stackInfo):
    #Create a new dictionary
    stack_data = {}
    #Create a nested dictionary for each stack, use key-value pair: switch_count: n
    for stack_name, switch_count in stackInfo.items():
        
        stack_data[stack_name] = {
            "switch_count": switch_count
        }    
    return stack_data