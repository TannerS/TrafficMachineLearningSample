from flask import Flask, jsonify
from sklearn import linear_model
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from flask import Response
from flask import request
# from flask_bower import Bower
from flask import send_from_directory
from sklearn import svm
import sys
import json

app = Flask(__name__)

model = make_pipeline(PolynomialFeatures(2), Ridge())

input_data = []
output_data = []

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return send_from_directory(app.static_folder + '/html/', 'index.html')


@app.route('/addData')
def addDataGet():
    # return app.send_static_file('/html/insert.html')
    return send_from_directory(app.static_folder + '/html/', 'insert.html')

@app.route('/addData', methods=['POST'])
def addDataPost():

    added_data = {"road_id": int(request.args.get("road_id")),
              "direction": int(request.args.get("direction")),
              "day_of_week": int(request.args.get("day_of_week")),
              "time_of_day": int(request.args.get("time_of_day"))}

    print(added_data)

    input_data_array = [added_data["road_id"], added_data["direction"], added_data["day_of_week"], added_data["time_of_day"]]

    input_data.append(input_data_array)

    print(input_data)

    output_data.append(int(request.args.get("traffic_status")))

    print(output_data)

    return "Added Data"

@app.route('/predict', methods=['GET'])
def predictGet():
    # return app.send_static_file('/html/prediction.html')
    return send_from_directory(app.static_folder + '/html/', 'prediction.html')\


@app.route('/predict', methods=['POST'])
def predictPost():

    print("INPUT: " + str(input_data))
    print("OUTPUT: " + str(output_data))
    model.fit(input_data, output_data)

    prediction_data = {"road_id": int(request.args.get("road_id")),
              "direction": int(request.args.get("direction")),
              "day_of_week": int(request.args.get("day_of_week")),
              "time_of_day": int(request.args.get("time_of_day"))}

    prediction_data_array = [prediction_data["road_id"], prediction_data["direction"], prediction_data["day_of_week"], prediction_data["time_of_day"]]

    prediction = model.predict(prediction_data_array)

    result = [prediction[0]]

    print("OUTPUT2: " + str(result))

    return jsonify(result=result)



# Bower(app)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(port=3000)
