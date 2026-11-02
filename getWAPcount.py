#Network Port-Matrix Automation Tool - getWAPcount.py

#This module defines the get_WAPcount() function




#The get_WAPcount() function prompts the user for the WAP count on each stack
#Adds a "wap-count" key-value pair to each switch-stack dictionary
#Adds to the NESTED dictionary 'stack_data' and returns 'stack_data'

def get_WAPcount(stack_data):
    #For each stack in the stack_data dictionary, ask the user for the corresponding wap count
    for stack_name in stack_data:
        wap_count = int(input(f"Enter the WAP count for {stack_name}: "))
        #Add the wap count as key-value pair in the corresponding's stack dictionary
        stack_data[stack_name]["wap_count"] = wap_count
    return stack_data