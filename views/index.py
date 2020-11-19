from flask import Blueprint, request, session, render_template, redirect, url_for

index = Blueprint('index', __name__)

@index.route('/index', methods= ['GET', 'POST'])
def welcome_shop():
    if request.method == "GET":
        shop = request.args.get('shop')
        session['shop'] = shop
        return render_template("index.html", shop = shop)
    if request.method == "POST":
        return redirect('/configuration')