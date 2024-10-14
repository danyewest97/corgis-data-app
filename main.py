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
    turbineInfo1 = "Turbine Info: "
    turbineInfo1 += "Capacity: " + str(turbine["Turbine"]["Capacity"]) + " kilowatts, "
    turbineInfo1 += "hub height: " + str(turbine["Turbine"]["Hub_Height"]) + " meters, "
    turbineInfo1 += "rotor diameter: " + str(turbine["Turbine"]["Rotor_Diameter"]) + " meters, "
    
    # Each entry in the result list is shown as a new line on the site
    # Making another turbineInfo variable to display turbine info on 2 separate lines
    turbineInfo2 = ""
    turbineInfo2 += "swept area: " + str(turbine["Turbine"]["Swept_Area"]) + " square meters, "
    turbineInfo2 += "total height: " + str(turbine["Turbine"]["Total_Height"]) + " meters."
    
    result.append(str(turbineInfo1))
    result.append(str(turbineInfo2))
    
    # Adding the project data
    
    
    return result
    