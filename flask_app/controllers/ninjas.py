from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninja():
    every_dojo = Dojo.get_all_dojos()
    return render_template("ninja.html", every_dojo = every_dojo)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    print(request.form)
    return redirect('/ninjas')
