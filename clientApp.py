from flask import Flask,request,jsonify,render_template
from flask_cors import CORS, cross_origin
from bert import Ner
import nltk
nltk.download('punkt')

app = Flask(__name__)
CORS(app)

model = Ner("out_base")
print("model:", model)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    text = request.json["text"]
    try:
        out = model.predict(text)
        return jsonify({"result":out})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

if __name__ == "__main__":
    app.run('0.0.0.0',port=5000)