#app.py

from flask import Flask, request, jsonify
import geopandas as gpd
import json

app = Flask(__name__)

path = 'data/perm_AOI/perm_AOI.shp'
df = gpd.read_file(path)

def read_poly(df, idx=2049):
    row = df[df.ORIG_FID == idx]
    poly = row.geometry
    return json.loads(poly.to_json())

@app.route('/api/get_poly')
def get_poly2():
    idx = int(request.args.get('idx'))
    print(idx)
    poly = read_poly(df, idx)
    return poly


@app.route('/')
def index():
    return f'<a href="http://localhost:5000/api/get_poly?idx=10">get poly</a>'

if __name__ == '__main_':
    app.run(debug=True, port=5000)  #run app in debug mode on port 5000
