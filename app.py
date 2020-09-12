#app.py

from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app
farms = [1,2,3,4,5]


@app.route('/query-example')
def query_example():
    language = request.args.get('language')
    return 'Todo... '+ str(language)

@app.route('/form-example')
def formexample():
    return 'Todo...'

@app.route('/get_farmer')
def jsonexample():
    idx = request.args.get('idx')
    return f'Farmer is {farms[int(idx)]}'

@app.route('/')
def index():
    idx = 1
    return f'Farmer is {farms[int(idx)]}'

if __name__ == '__main_':
    app.run(debug=True, port=5000)  #run app in debug mode on port 5000
