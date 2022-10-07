from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo


@app.route('/')
def click_me():
    return render_template("click_me.html")

@app.route('/dojos')
def dojo_list():
    dojos = Dojo.get_all_dojos()
    return render_template("dojo.html", every_dojo = dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():

    Dojo.create_dojo(request.form)
    print(request.form)
    return redirect('/dojos')

@app.route('/one_dojo/<int:id>')
def one_dojo(id):
    data = {
        "id":id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("one_dojo.html", dojo = dojo)
