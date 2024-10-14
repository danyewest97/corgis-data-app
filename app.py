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
    return render_template('turbines.html', response=main.turbineToString(data), highlow=request.args["highlow"], key=keyString)
    
# @app.route("/projects")
# def render_projects():
    # return render_template('home.html', response=data)
    
# @app.route("/locations")
# def render_locations():
    # return render_template('home.html', response=data)

if __name__=="__main__":
    app.run(debug=False)
