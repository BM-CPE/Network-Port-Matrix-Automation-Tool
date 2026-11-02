#Network Port-Matrix Automation Tool - displayMatrix.py

#This module defines the display_WAPmatrix() function




#The display_WAPmatrix() function formats ALL stack matrices
#The final WAP port matrix lists all the WAPs and their assigned port
#The matrix is segmented by stack names to provide a clear, structured layout

def display_WAPmatrix(stack_data):
    for stack_name, stack_info in stack_data.items():
        print()
        print(stack_name)

        for wap_name, port in stack_info["WAP_Port_Matrix"].items():
            print(f"{wap_name} -> {port}")