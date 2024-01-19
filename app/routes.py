from flask import request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"

@app.route('/add')
def add():
    data = request.args.get('data',None)
    _list = list(map(int,data.split(',')))

    total = sum(_list)
    return 'Result =  ' + str(total)

def sum(arg):
    try:
        total = 0
        for val in arg:
             total += val
    except Exception:
        return "Error occured!", 500
    return total