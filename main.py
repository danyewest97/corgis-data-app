import json, sys

def print_data():
    with open("static/data.json") as file:
        data = json.load(file);
    
    print(data)

def get_data(category, key, highlow):
    with open("static/data.json") as file:
        data = json.load(file);
    
    
    if (highlow == "high"):
        highest = -sys.maxsize - 1
        for element in data:
            if highest < element[category][key]:
                result = element
                highest = element[category][key]
        return result
        
    elif (highlow == "low"):
        print()
        


def turbineToString(turbine):
    result = []
    
    # Adding the location
    site = "Site: "
    site += turbine["Site"]["County"] + ", "
    site += turbine["Site"]["State"] + ", "
    site += str(turbine["Site"]["Latitude"]) + " degrees latitude, "
    site += str(turbine["Site"]["Longitude"]) + " degrees longitude."
    result.append(str(site))
    
    # Adding the turbine data
    turbine += "Turbine Info: "
    turbine += str(turbine["Site"]["Latitude"]) + " degrees latitude, "
    
    result.append(str(turbine))
    
    return result
    