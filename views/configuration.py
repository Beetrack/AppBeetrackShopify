from flask import Blueprint, request, session, render_template, redirect, flash
from api.beetrack import BeetrackApiHandler

configuration = Blueprint('configuration', __name__)

@configuration.route('/configuration', methods= ['GET', 'POST'])
def add_api_key():
    if request.method == "GET":
        shop = request.args.get('shop')
        session['shop'] = shop
        return render_template("configuration.html")

    elif request.method == 'POST':
        beetrack_api_key = request.form['api_key']
        verify_beetrack_account = BeetrackApiHandler(beetrack_api_key).verify_apikey()
        if verify_beetrack_account:
            session["beetrack_api_key"] = beetrack_api_key
            return redirect('/install')
        else:
            flash("Wrong API KEY, check your configurations.")
            return render_template('configuration.html')
    else:
         return render_template('error.html')
