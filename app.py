import numpy as np
import pandas as pd
import pickle
import ast

import requests_file
from flask import *

app = Flask(__name__ , static_url_path='/static')
@app.route('/')
def Home():
    return render_template('index.html')
@app.route('/page2')
def secondPage():
    return render_template('index1.html')
@app.route('/goto_page2')
def goto_page2():
    return redirect(url_for('secondPage'))
@app.route("/predict" , methods = ['POST'])
def predict():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        file_content = uploaded_file.read().decode('utf-8').strip()
        file_contents = file_content.replace('[', '').replace(']', '')
        string_array = file_contents.split(',')
        print("file_content: ", file_content)
        float_list = ast.literal_eval(file_content)
        print("String_array: ", string_array)
        data = np.array(float_list , dtype=float)
        print("data1: ", data , data.dtype, data.shape)
        data = np.reshape(data, (-1, 23))
        print("data2: ", data.dtype, data.shape)
        model = pickle.load(open('model.pkl', 'rb'))
        asd = model.predict(data)
        print("asd", asd)
        val = asd[0, 0]
        if val < 0.50:
            return render_template('index1.html', results="Predicted Value is {:.3f}, Patient is less likely to get Seizure.".format(val))
        else:
            return render_template('index1.html', results= "Predicted Value is {:.3f}, Patient is likely to get Seizure." .format(val))
    else:
        return render_template('index1.html')
if __name__=="__main__":
    print("Starting the Flask Application!")
    app.run(debug=True)
