#Network Port-Matrix Automation Tool - getWAPnames.py


#This module defines the reserve_ports() function




#The reserve_ports() function reserves the wap switch-ports
#The WAP ports are reserved according to the the wapDistribution list
#Returns a port_groups{} dictionary data type

def reserve_ports(wapDistribution):

    port_groups = {}

    for switch_number, wap_count in enumerate(wapDistribution, start=1):

        start_port = 48 - wap_count + 1

        ports = []

        for port in range(start_port, 49):
            ports.append(f"Gi{switch_number}/0/{port}")

        port_groups[switch_number] = ports

    return port_groups   
