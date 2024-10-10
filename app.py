from flask import Flask, url_for, render_template, request
import random, string, main

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_home():
    return render_template('home.html')
    
@app.route("/turbines")
def render_turbines():
    data = main.get_data("Turbine", "Capacity", "high")
    return render_template('turbines.html', response=main.turbineToString(data))
    
@app.route("/projects")
def render_projects():
    return render_template('home.html', response=data)
    
@app.route("/locations")
def render_locations():
    return render_template('home.html', response=data)

if __name__=="__main__":
    app.run(debug=False)
