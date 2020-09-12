#app.py

from flask import Flask, request, jsonify
import geopandas as gpd


app = Flask(__name__)

df = gpd.read_file('data/Поля_Полигональные2.shp')

def read_poly(df):
    row = df[df.ORIG_FID == 2049].copy()
    poly = row.geometry
    return poly.to_json()


@app.route('/get_poly')
def get_poly():
    poly = read_poly(df)
    return jsonify({
        'geometries': [poly]
    })

@app.route('/api/get_poly')
def get_poly2():
    poly = read_poly(df)
    return jsonify({
        'geometries': [poly]
    })


@app.route('/')
def index():
    return f'<a href="http://localhost:5000/get_poly">get poly</a>'

if __name__ == '__main_':
    app.run(debug=True, port=5000)  #run app in debug mode on port 5000
