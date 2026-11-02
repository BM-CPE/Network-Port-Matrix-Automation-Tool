#Network Port-Matrix Automation Tool - getRedundancy.py

#This module defines the get_redundancy() function




#The get_redundancy() function returns the final reserved-ports list, in correct order, with redundancy applied
#The function applies redundancy by ensuring that no consecutive WAPs are connected to the same switch (if switch_count > 1)
#Returns a list[] data type

def get_redundancy(reservedPorts):

    wapList = []

    max_rounds = max(
        len(ports)
        for ports in reservedPorts.values()
    )

    for round_number in range(max_rounds):

        for switch_number, ports in reservedPorts.items():

            if round_number < len(ports):

                wapList.append(
                    ports[round_number]
                )
    return wapList