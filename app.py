#app.py

from flask import Flask, request, jsonify
import geopandas as gpd
import json

app = Flask(__name__)

df_target = gpd.read_file('XY4326/tmp_target/tmp_target.shp')

df_all = gpd.read_file('XY4326/tmp2/tmp2.shp')
df_all['inter_all'] = df_all.inter_all.apply(lambda x: eval(x) if x.endswith(']') else [])

def read_poly(df, idx=2049):
    row = df[df.ORIG_FID == idx]
    poly = row.geometry
    return json.loads(poly.to_json())

def get_near(df, idx=[1,3,4,5]):
    row = df.loc[idx]
    poly = row.geometry
    return json.loads(poly.to_json())



def sample(df, idxs=[1, 2, 3, 4, 5, 6, 7, 8]):
    ret = []
    for idx in idxs:
        tmp = df[df.ORIG_FID == idx]
        area = tmp.Shape_Area.values.sum()
        length = tmp.Shape_Leng.values.sum()
        ret.append({
            'id': idx,
            'area': area,
            'length': length,
            'map_fields': read_poly(df, idx),
            'map_ground_truth': get_near(df_target, tmp.iloc[0].inter_all),
            'status': 'new',
            'verified': False,
        })
    return {'data': ret}

@app.route('/api/get_poly')
def get_poly2():
    idx = int(request.args.get('idx'))
    print(idx)
    poly = read_poly(df_all, idx)
    return poly


@app.route('/api/get_all_fields')
def get_poly3():
    return sample(df_all, [455,  460,  471,  473,  486,  487,  490,  494,  496,  499,  504, 511,  523,  528,  529,  535,  537,  538,  543,  558,  559,  560])



@app.route('/')
def index():
    return f'<a href="http://localhost:5000/api/get_poly?idx=10">get poly</a>' f'<a href="http://localhost:5000/api/get_all_fields">get all</a>'

if __name__ == '__main_':
    app.run(debug=True, port=5000)  #run app in debug mode on port 5000
