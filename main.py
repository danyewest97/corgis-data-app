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
        lowest = sys.maxsize
        for element in data:
            if lowest > element[category][key]:
                result = element
                lowest = element[category][key]
        return result
        


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
    turbineInfo = "Turbine Info: "
    turbineInfo += "Capacity: " + str(turbine["Turbine"]["Capacity"]) + " kilowatts, "
    turbineInfo += "hub height: " + str(turbine["Turbine"]["Hub_Height"]) + " meters, "
    turbineInfo += "rotor diameter: " + str(turbine["Turbine"]["Rotor_Diameter"]) + " meters, "
    turbineInfo += "swept area: " + str(turbine["Turbine"]["Swept_Area"]) + " square meters, "
    turbineInfo += "total height: " + str(turbine["Turbine"]["Total_Height"]) + " meters."
    
    result.append(str(turbineInfo))
    
    # Adding the project data
    projectData = "Project Info: "
    projectData += "Capacity: " + str(turbine["Project"]["Capacity"]) + " megawatts, "
    projectData += "number of turbines: " + str(turbine["Project"]["Number_Turbines"]) + " turbines."
    
    result.append(str(projectData))
    
    return result


def get_data_by_state(category, key, highlow, state):
    if (state == "<none>"):
        return get_data(category, key, highlow)
    
    
    with open("static/data.json") as file:
        data = json.load(file);
    
    
    if (highlow == "high"):
        highest = -sys.maxsize - 1
        for element in data:
            if highest < element[category][key]:
                if element["Site"]["State"] == state:
                    result = element
                    highest = element[category][key]
        return result
        
    elif (highlow == "low"):
        lowest = sys.maxsize
        for element in data:
            if lowest > element[category][key]:
                result = element
                lowest = element[category][key]
        return result


def get_state_options():
    with open("static/data.json") as file:
        data = json.load(file);
    
    states = ["<none>"] # Adding a none option at the start for the user to look at all wind turbines in the US, instead of just one state
    
    for element in data:
        found = 0
        for state in states:
            if element["Site"]["State"] == state:
                found = 1
        if found != 1:
            states.append(element["Site"]["State"])
            found = 0
    
    return states


def get_state_data(state):
    result = []
    
    result.append("<h1>temp</h1>")
    return result