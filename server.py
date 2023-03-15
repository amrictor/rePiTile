
#!/usr/bin/python
import flask
from flask import jsonify
from terrarium import Terrarium


app = flask.Flask(__name__)

@app.route('/mist', methods=['POST'])
def mist():
  try: 
    Terrarium.mist(3)
  except(Exception): 
    return Exception.args, 409
  else:
    return '', 204

@app.route('/data', methods=['GET'])
def data(): 
  humidity, temperature = Terrarium.get_data()
  data = {'humidity': humidity,
          'temperature': temperature}
  return jsonify(data), 200

@app.route('/temperature', methods=['GET'])
def water():
  return Terrarium.get_temp(), 200

@app.route('/humidity', methods=['GET'])
def water():
  return Terrarium.get_humidity(), 200

@app.route('/water', methods=['GET'])
def water():
  return Terrarium.get_water_level(), 200

app.run(host='0.0.0.0')
