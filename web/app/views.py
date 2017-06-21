from app import app

@app.route('/')
def hello_world():
    return 'Flask is much dockerized!!!'
