from flask import Flask, render_template,request
import  joblib
import os
import numpy as np

app = Flask(__name__)
model = joblib.load(os.path.join("artifacts", "model", "model.pkl"))
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        
        # Extracting features from the form
        sepal_length = float(request.form['SepalLengthCm'])
        sepal_width = float(request.form['SepalWidthCm'])
        petal_length = float(request.form['PetalLengthCm'])
        petal_width = float(request.form['PetalWidthCm'])
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Making prediction
        prediction = model.predict(features)
        prediction = prediction[0]
    return render_template('index.html', prediction=prediction)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    