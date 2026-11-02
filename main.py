#Network Port-Matrix Automation Tool - main.py
#Bryan Martinez

#This software tool generates Wireless Access Point (WAP) Port Matrices autonomously
#Replaces a time-consuming manual network engineering process 
#Increases productivity and efficiency by producing instant results




#Import the following functions from the their respective python module:
from getSiteData import get_siteData
from getStackData import get_stackData
from getWAPcount import get_WAPcount
from distributeWAPs import distribute_waps
from getWAPnames import get_WAPnames
from reservePorts import reserve_ports
from getRedundancy import get_redundancy
from assignWAPports import wap_portAssignment
from displayMatrix import display_WAPmatrix
from exportMatrix import export_WAPmatrix




#1. Call the get_siteData() function 
#Prompts for site code input
#Returns switch-stack names and switch-count
#Returns a SINGLE dictionary and the site code
site_data, site_code = get_siteData()
#print(site_code)




#2. Call the get_stackData() function
#Creates nested dictionaries for each stack
#Returns switch-stack names and switch-count
#Returns NESTED dictionary file type: stack_data 
stack_data = get_stackData(site_data)




#3. Call the get_wapCount() function
#Displays the stack names and ask user to enter wap count for each stack
#Adds wap count key-value pair to the stack data dictionary
stack_data = get_WAPcount(stack_data)




#4. Call the distribute_waps() function
#Distributes the WAPs evenly amongst switches
#Indicates how many WAPs will be connected to each switch in the stack
#Returns a distribution list data type
#The for loop adds the distribution-list key-value pair to each stack's dictionary
for stack_name, stack_info in stack_data.items():

    wapDistribution = distribute_waps(
        stack_info["switch_count"],
        stack_info["wap_count"]
    )
    stack_info["wap_distribution"] = wapDistribution
#print(stack_data)




#5. Call get_WAPnames() function
#First, a closet_counter{} dictionary is created 
#The dictionary keeps count of the number of stacks in any MDF/IDF closet 
#This is required to name the WAPs correctly if there is more than 1 stack in any MDF/IDF closet
#The for loop will check for this information and then will call the get_WAPnames() function
#The function then appends a wap-names list to stack dictionary

closet_counter = {}
#Loop through the stacks to determine their MDF/IDF
for stack_name, stack_info in stack_data.items():

    closet_id = stack_name[:-2]

    #Determine the WAP start number
    if closet_id not in closet_counter:
        start_number = 1
    else:
        start_number = closet_counter[closet_id]

    #Get the wap names
    wapNames = get_WAPnames(
        stack_name,
        stack_info["wap_count"],
        start_number
        )
    #Append the stack dictionary
    stack_info["wap_names"] = wapNames
    #Update the counter
    closet_counter[closet_id] = start_number + stack_info["wap_count"]
    #The statement above starts the new count at 'previous total wap count + 1' (ex: if previous wap_count=18, then new start_number=19)
#print(stack_data)




#6. Call the reserve_ports() function
#Reserves the all WAP switch-ports for each stack
#Returns a dictonary data type containing the reserved ports for each stack AND switch
#The for loop appends the reserved ports to each stack in the stack dictionary
for stack_name, stack_info in stack_data.items():

    reservedPorts = reserve_ports(
        stack_info["wap_distribution"])
    
    stack_info["reserved_ports"] = reservedPorts
#print(stack_data)




#7. Call the get_redundancy() function
#Ensures that no consecutive WAPs are connected to the same switch (if switch_count > 1)
#Adds redundancy to all wap ports 
#Returns a list[] data type containing the FINAL reserved-ports list
#The for loop appends the reserved-port list to each stack in the stack dictionary
for stack_name, stack_info in stack_data.items():

    wapPortList = get_redundancy(
        stack_info["reserved_ports"])
    
    stack_info["wap_port_list"] = wapPortList
#print(stack_data)




#8. Call the wap_portAssignment() function
#Completes the WAP PORT MATRIX for each stack
#Returns a dictionary{} named WAP_Port_Matrix
#The for loop appends the WAP_Port_Matrix to eaxh stack in the stack dictionary
for stack_name, stack_info in stack_data.items():

    WAP_Port_Matrix = wap_portAssignment(
        stack_info["wap_names"],
        stack_info["wap_port_list"]
        )
    
    stack_info["WAP_Port_Matrix"] = WAP_Port_Matrix
#print(stack_data)    




#9. Call the display_WAPmatrix() function
#Formats the site's complete WAP port Matrix
#Displays the site's complete WAP Port Matrix to the console
#display_WAPmatrix(stack_data)




#10. Call the export_WAPmatrix() function
#Exports the complete WAP Port Matrix to a csv file
#Generate the site's complete WAP Port Matrix csv file  - Final Output
export_WAPmatrix(stack_data, site_code)