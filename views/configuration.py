from flask import Blueprint, request, session, render_template, redirect, flash
from api.beetrack import BeetrackApiHandler

configuration = Blueprint('configuration', __name__)

@configuration.route('/configuration', methods= ['GET', 'POST'])
def create_api_key():
    if request.method == "GET":
        shop = session['shop']
        return render_template("configuration.html", shop = shop)
    elif request.method == 'POST':
        beetrack_api_key = request.form['api_key']
        verify_beetrack_key = verify_api_key(beetrack_api_key)
        return verify_beetrack_key
    else:
         return render_template('error.html')

def verify_api_key(beetrack_api_key):
    verify_beetrack_account = BeetrackApiHandler(beetrack_api_key).verify_apikey()
    if verify_beetrack_account:
        session["beetrack_api_key"] = beetrack_api_key
        return redirect('/install')
    else:
        flash("Wrong API Key: {}, check your Beetrack account configurations.".format(beetrack_api_key))
        shop = session["shop"]
        return render_template('configuration.html', shop = shop)
