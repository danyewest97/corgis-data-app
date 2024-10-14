from flask import Flask, url_for, render_template, request
import random, string, main

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_home():
    return render_template('home.html')
    
@app.route("/turbines")
def render_turbines():
    return render_template('turbines.html')

@app.route("/turbineform")
def render_turbine_form():
    data = main.get_data("Turbine", request.args["key"], request.args["highlow"])
    keyString = str(request.args["key"]).lower()
    keyString = keyString.replace("_", " ")
    return render_template('turbines.html', response=main.turbineToString(data), keyhighlow="Here is the info on the turbine with the " + request.args["highlow"] + "est " + keyString + ": ")
    
@app.route("/projects")
def render_projects():
    return render_template('projects.html')

@app.route("/projectform")
def render_project_form():
    data = main.get_data("Project", request.args["key"], request.args["highlow"])
    keyString = str(request.args["key"]).lower()
    keyString = keyString.replace("_", " ")
    if (keyString == "Number Turbines"):
        keyString == "Number of Turbines"
    
    return render_template('projects.html', response=main.turbineToString(data), keyhighlow="Here is the info on one of the turbines in the project with the " + request.args["highlow"] + "est " + keyString + ": ")
    
@app.route("/locations")
def render_locations():
    return render_template('locations.html')

@app.route("/locationform")
def render_location_form():
    data = main.get_data("Site", request.args["key"], request.args["highlow"])
    keyString = str(request.args["key"]).lower()
    keyString = keyString.replace("_", " ")
    return render_template('locations.html', response=main.turbineToString(data), keyhighlow="Here is the info on the turbine with the " + request.args["highlow"] + "est " + keyString + ": ")

if __name__=="__main__":
    app.run(debug=False)
