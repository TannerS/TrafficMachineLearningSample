from flask import Flask, jsonify
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from flask import request
from flask import send_from_directory

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
    return send_from_directory(app.static_folder + '/html/', 'insert.html')

@app.route('/addData', methods=['POST'])
def addDataPost():

    added_data = {"road_id": int(request.args.get("road_id")),
              "direction": int(request.args.get("direction")),
              "day_of_week": int(request.args.get("day_of_week")),
              "time_of_day": int(request.args.get("time_of_day"))}

    input_data_array = [added_data["road_id"], added_data["direction"], added_data["day_of_week"], added_data["time_of_day"]]

    input_data.append(input_data_array)

    output_data.append(int(request.args.get("traffic_status")))

    return "Added Data"

@app.route('/predict', methods=['GET'])
def predictGet():
    return send_from_directory(app.static_folder + '/html/', 'prediction.html')

@app.route('/predict', methods=['POST'])
def predictPost():

    model.fit(input_data, output_data)

    prediction_data = {"road_id": int(request.args.get("road_id")),
              "direction": int(request.args.get("direction")),
              "day_of_week": int(request.args.get("day_of_week")),
              "time_of_day": int(request.args.get("time_of_day"))}

    prediction_data_array = [prediction_data["road_id"], prediction_data["direction"], prediction_data["day_of_week"], prediction_data["time_of_day"]]

    prediction = model.predict(prediction_data_array)

    result = [prediction[0]]

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
