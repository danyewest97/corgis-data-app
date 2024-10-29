import json, sys

def print_data():
    with open("static/data.json") as file:
        data = json.load(file);
    
    print(data)

def get_data(category, key, highlow):
    with open("static/data.json") as file:
        data = json.load(file);
    
    
    if key == "Capacity":
        if category == "Project":
            units = "megawatts"
        else:
            units = "kilowatts"
    
    if key == "Hub_Height":
        units = "meters"
    
    if key == "Rotor_Diameter":
        units = "meters"
    
    if key == "Swept_Area":
        units = "square meters"
    
    if key == "Total_Height":
        units = "meters"
    
    if key == "Number_Turbines":
        units = "turbines"
    
    
    
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
    
    elif (highlow == "average"):
        result = []
        total = 0
        numPoints = 0
        for element in data:
                total += element[category][key]
                numPoints += 1
        result.append(str(round(total/numPoints, 2)) + " " + units)
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
    
    
    if key == "Capacity":
        if category == "Project":
            units = "megawatts"
        else:
            units = "kilowatts"
    
    if key == "Hub_Height":
        units = "meters"
    
    if key == "Rotor_Diameter":
        units = "meters"
    
    if key == "Swept_Area":
        units = "square meters"
    
    if key == "Total_Height":
        units = "meters"
    
    if key == "Number_Turbines":
        units = "turbines"
    
    
    
    if (highlow == "high"):
        highest = -sys.maxsize - 1
        for element in data:
            if element["Site"]["State"] == state:
                if highest < element[category][key]:
                    result = element
                    highest = element[category][key]
        return result
        
    elif (highlow == "low"):
        lowest = sys.maxsize
        for element in data:
            if element["Site"]["State"] == state:
                if lowest > element[category][key]:
                    result = element
                    lowest = element[category][key]
        return result
    elif (highlow == "average"):
        result = []
        total = 0
        numPoints = 0
        for element in data:
            if element["Site"]["State"] == state:
                    total += element[category][key]
                    numPoints += 1
        result.append(str(round(total/numPoints, 2)) + " " + units)
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


def get_years():
    years = []
    with open("static/data.json") as file:
        data = json.load(file);
    
    for element in data:
        if element["Year"] not in years:
            years.append(element["Year"])
    
    years.sort()
    return years


def get_state_data(state):
    result = []
    
    result.append("<h1>Here is the wind turbine info on " + state + ":</h1>")
    result.append("<p>If all the wind turbines in " + state + " worked together at maximum capacity, they could produce " + str(int(get_state_total("Turbine", "Capacity", state) / 1000)) + " megawatts of power!")
    return result


def get_state_total(category, key, state):
    with open("static/data.json") as file:
        data = json.load(file);
    
    
    total = 0
    for element in data:
        if element["Site"]["State"] == state:
            total += element[category][key]
    return total

def get_data_for_pie():
    result = ""
    states = get_state_options()
    totals = []
    for state in states:
        emptyState = {
            "Name": state,
            "Total": 0
        }
        if emptyState["Name"] != "<none>":
            totals.append(emptyState)
    
    with open("static/data.json") as file:
        data = json.load(file);
    
    
    totalInUS = 0
    for turbine in data:
        for state in totals:
            if turbine["Site"]["State"] == state["Name"]:
                state["Total"] += 1
                totalInUS += 1
    
    total = 0;
    for state in totals:
        result += "{ y: " + str((state["Total"] / totalInUS) * 100) + ", label: \"" + state["Name"] + "\" }," + "\n"
        total += (state["Total"] / totalInUS) * 100
    
    return result


def get_data_for_bar():
    result = []
    
    years = get_years()
    totals = []
    for year in years:
        emptyYear = {
            "Year": year,
            "Total": 0
        }
        totals.append(emptyYear)
    
    
    with open("static/data.json") as file:
        data = json.load(file);
    
    for element in data:
        for year in totals:
            if element["Year"] == year["Year"]:
                year["Total"] += 1
    
    
    for year in totals:
        result.append({"x": year["Year"], "y": year["Total"]})
    
    return json.dumps(result)


def get_state_data_for_bar(state):
    result = []
    
    years = get_years()
    totals = []
    for year in years:
        emptyYear = {
            "Year": year,
            "Total": 0
        }
        totals.append(emptyYear)
    
    
    with open("static/data.json") as file:
        data = json.load(file);
    
    for element in data:
        for year in totals:
            if element["Year"] == year["Year"]:
                if element["Site"]["State"] == state:
                    year["Total"] += 1
    
    firstYear = 0
    for year in totals:
        if firstYear == 0:
            if year["Total"] != 0:
                result.append({"x": year["Year"], "y": year["Total"]})
                firstYear = 1
        else:
            result.append({"x": year["Year"], "y": year["Total"]})
    
    return json.dumps(result)