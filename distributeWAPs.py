#Network Port-Matrix Automation Tool - distributeWAPs.py

#This module will determine how many WAPs each switch gets

#The distribute_waps() function accepts switch_count and wap_count integer values
#Distributes the total wap count accross the switches in the stack
#If wap count is not divisible by switch count, extras are added to first switches accordingly
#Returns a LIST data type

def distribute_waps(switch_count, wap_count):
    base = wap_count // switch_count
    extra = wap_count % switch_count

    distribution = []

    for switch in range(switch_count):

        if switch < extra:
             distribution.append(base + 1)
        else:
             distribution.append(base)

    return distribution

#To call function:
#distribute_waps(4, 100)