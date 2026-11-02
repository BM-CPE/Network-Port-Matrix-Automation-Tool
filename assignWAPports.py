#Network Port-Matrix Automation Tool - getRedundancy.py

#This module defines the wap_portAssignment() function




#The wap_portAssignment() function completes the WAP PORT MATRIX for each stack
#Returns a dictionary{} data type: WAP_PORT_MATRIX

def wap_portAssignment(wapNames, wapPortList):
    
    #Create the new dictionary
    WAP_PORT_MATRIX = {}

    #Concatenates wap name with corresponding port
    for wap_name, port in zip(wapNames, wapPortList):
        #print(f"{wap_name} {port}")
        WAP_PORT_MATRIX[wap_name] = port
    
    return WAP_PORT_MATRIX