
#!/usr/bin/python
import flask
from flask import jsonify
from terrarium import Terrarium


app = flask.Flask(__name__)

tank = Terrarium()

@app.route('/mist', methods=['POST'])
def mist():
  try: 
    tank.mist(3)
  except Exception as e: 
    return repr(e), 409
  else:
    return '', 204

@app.route('/data', methods=['GET'])
def data(): 
  humidity, temperature = tank.get_data()
  data = {'humidity': humidity,
          'temperature': temperature}
  return jsonify(data), 200

@app.route('/temperature', methods=['GET'])
def temperature():
  return tank.get_temp(), 200

@app.route('/humidity', methods=['GET'])
def humidity():
  return tank.get_humidity(), 200

@app.route('/water', methods=['GET'])
def water():
  try:
    return tank.get_water_level(), 200
  except Exception as e:
    print(e)

app.run(host='0.0.0.0')
