#app.py

from flask import Flask, request, jsonify
import geopandas as gpd


app = Flask(__name__)

path = 'data/perm_AOI/perm_AOI.shp'
df = gpd.read_file(path)
def read_poly(df, idx=2049):
    row = df[df.ORIG_FID == idx].copy()
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
