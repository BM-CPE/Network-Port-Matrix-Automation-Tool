#Network Port-Matrix Automation Tool - getWAPnames.py

#This module defines the get_WAPnames() function
#
#
#Before calling the function, 2 new variables were introduced in main.py: closet_counter = {} & start_number 
#closet_counter{}: to help keep track of stacks within the same closet 
#start_number:     to name the waps correctly
#The getWAPnames() function generates a list of WAP names for each stack and returns as list[] data type




def get_WAPnames(stack_name, wap_count, start_number):
    #Replace 1st 3 characters 'stk' with 'wap'
    base_name = "wap" + stack_name[3:]

    #Create the list for the waps
    wapNames = []

    #Create wap names according to the wap count
    #This starts wap naming at 1: for i in range(1, wap_count+1):
    
    #This starts wap naming at 'start_number' and ends at 'start_number' + 'wap_count':
    for i in range(start_number, start_number + wap_count):
	#Number the waps
        wap_name = base_name[:-2] + f"{i:02}"
	#Store the wap names in a list
        wapNames.append(wap_name)
    return wapNames