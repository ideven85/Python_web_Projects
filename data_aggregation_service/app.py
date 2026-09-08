import flask
from flask import Flask,request,jsonify
import mlflow.sklearn
app = Flask(__name__)

model = mlflow.sklearn.load_model("runs:/<run_id>/model")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["input"]
    pred = model.predict([data])
    return jsonify({"prediction": int(pred[0])})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)