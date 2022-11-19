import os
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__, static_folder=os.path.abspath('static'))

@app.route('/')
def home():
    return jsonify({'intro': "symptom-analysis"}), 200

    

model_1 = joblib.load(open('Model/model_file.sav', 'rb'))
def predict(array):
        x = np.array([[i for i in array]])

        pred = model_1.predict(x)

        if pred[0] == 0:
            print(pred)
            return jsonify({'result': "A"}), 200
        elif pred[0] == 1:
            print(pred)
            return jsonify({'result': "B"}), 200
        elif pred[0] == 2:
            print(pred)
            return jsonify({'result': "C"}), 200
        elif pred[0] == 3:
            print(pred)
            return jsonify({'result': "D"}), 200
        elif pred[0] == 4:
            print(pred)
            return jsonify({'result': "E"}), 200
        else:
            print(pred)
            return jsonify({'result': "F"}), 200

@app.route("/predict", methods=["POST", "GET"])
def calculatePrice():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        array = request.json
        intArray = array['array']
        print(intArray)
        try:
            if intArray != None:
                print(type(intArray))
                print("File found")
                return predict(intArray)
            else:
                print("File not found")
                return jsonify({'result': 'Failed'}), 404
        except Exception as e:
            print(e)
            return jsonify({'result': 'Failed'}),   404
    else:
        return jsonify({'result': 'Failed'}), 404
        

if __name__ == '__main__':
    app.run(debug=True)
