import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn.linear_model import LinearRegression
import pandas as pd

app = Flask(__name__)
# model = pickle.load(open('regression_model.pkl','rb'))
model = pd.read_pickle(r'regression_model.pkl')

@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    print(prediction[0])

    #output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="Predicted AQI is {}".format(prediction[0]))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)



if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")