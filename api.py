from flask import Flask,request,jsonify,render_template

app= Flask(__name__)
latitude=None
longitude=None


@app.route('/',methods=['POST','GET'])
def upload_data():
    latitude=request.form['latitude']
    longitude=request.form['longitude']

    print(f'latitude= {latitude}  longitude={longitude}')

    return render_template('index.html',latitude=latitude,longitude=longitude)          

if __name__=="__main__":
    app.run(debug=True)