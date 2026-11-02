#Network Port-Matrix Automation Tool - getSiteData.py


#This module contains the site database dictionary and defines the get_siteData() function



#The site database is a dictionary data type: site_database = {}
#The database contains NESTED dictionaries for each site:
#Dictionary name == site code
#key == stack name
#value == switch count 

site_database = {

    "DC105": {
        "stkDC105a01a01": 4,
        "stkDC105a01a02": 4,
        "stkDC105a01a03": 3,
        "stkDC105a01a04": 2,
        "stkDC105a02a01": 3,
        "stkDC105a02a02": 3,
        "stkDC105a03a01": 2,
        "stkDC105a03a02": 2,
        "stkDC105a03b01": 4,
        "stkDC105a03b02": 4,
        "stkDC105b01a01": 4,        
        "stkDC105b01a02": 4,
        "stkDC105b02a01": 2,
        "stkDC105b03a01": 4,
        "stkDC105b03b01": 1,
    },

    "DC101": {
        "stkDC101a01a01": 4,
        "stkDC101a01a02": 4,
        "stkDC101a02a01": 3,
        "stkDC101b02a01": 2,
    },

    "DC255": {
        "stkDC255a01a01": 4,
        "stkDC255a01a02": 4,
        "stkDC255a02a01": 3,
    },

    "RS824": {
        "stkRS824a01a01": 3,
        "stkRS824b02a01": 3,
    }

}




#The get_siteData() function returns the site's stack names and switch count according to the site code entered
#The site's switch-stack data is returned as a SINGLE dictionary data type
#The site code is also returned and stored

def get_siteData():

    site_code = input("Enter site code: ").upper()

    match site_code:

        case "DC105":
            return site_database["DC105"], site_code

        case "DC101":
            return site_database["DC101"], site_code

        case "DC255":
            return site_database["DC255"], site_code

        case "RS824":
            return site_database["RS824"], site_code
        
        case _:
            print("Invalid site code.")
            return None, None
        
