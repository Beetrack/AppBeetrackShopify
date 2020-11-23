from flask import Blueprint, request

base = Blueprint('base', __name__)

@base.route('/', methods= ['GET', 'POST'])
def integrate():
    event = request.args.get('shop')