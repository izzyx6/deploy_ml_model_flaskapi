from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load(open('model.joblib', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    """[summary]

    Returns:
        [type]: [description]
    """    For rendering results on User Interface
    '''
    features = request.form.values()

    prediction = model.predict(features)

    return render_template('index.html', data = prediction)


if __name__ == "__main__":
    app.run(debug=True)