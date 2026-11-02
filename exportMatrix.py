#Network Port-Matrix Automation Tool - displayMatrix.py

#This module imports the csv module and defines the export_WAPmatrix() function




#Import Python's csv module to access csv functionality
import csv

#The export_WAPmatrix() function exports the complete WAP Port Matrix to a csv file
#The final output is a generated WAP Port Matrix csv file 
def export_WAPmatrix(stack_data, site_code):

    filename=f"{site_code}_WAP_Port_Matrix.csv"

    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        for stack_name, stack_info in stack_data.items():

            # Write the stack name
            writer.writerow([stack_name])

            # Write each WAP-port assignment
            for wap_name, port in stack_info["WAP_Port_Matrix"].items():
                writer.writerow([f"{wap_name} -> {port}"])

            # Add a blank row between stacks
            writer.writerow([])

    print(f"\nCSV file created: {filename}")