import numpy as np
import pandas as pd
import pickle
import ast
from datetime import datetime
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static')
print(airflow.__version__)
global model
def load_model():
    global model
    model = pickle.load(open('model.pkl', 'rb'))

def run_flask_app():
    global model
    model = pickle.load(open('model.pkl', 'rb'))
    uploaded_file = request.files['file']
    file_content = uploaded_file.read().decode('utf-8').strip()
    file_contents = file_content.replace('[', '').replace(']', '')
    string_array = file_contents.split(',')
    print("file_content: ", file_content)
    float_list = ast.literal_eval(file_content)
    print("String_array: ", string_array)
    data = np.array(float_list, dtype=float)
    print("data1: ", data, data.dtype, data.shape)
    data = np.reshape(data, (-1, 23))
    print("data2: ", data.dtype, data.shape)
    asd = model.predict(data)
    print("asd", asd)
    val = asd[0, 0]
    if val < 0.50:
        return render_template('index1.html', results="Predicted Value is {:.3f}, Patient is less likely to get Seizure.".format(val))
    else:
        return render_template('index1.html', results="Predicted Value is {:.3f}, Patient is likely to get Seizure.".format(val))

dag = DAG(
    'flask_airflow_dag',
    description='DAG for Flask and Airflow integration',
    schedule_interval=None,
    start_date=datetime(2023, 5, 25),
)

load_model_task = PythonOperator(
    task_id='load_model_task',
    python_callable=load_model,
    dag=dag,
)

run_flask_app_task = PythonOperator(
    task_id='run_flask_app_task',
    python_callable=run_flask_app,
    dag=dag,
)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/page2')
def secondPage():
    return render_template('index1.html')

@app.route('/goto_page2')
def goto_page2():
    return redirect(url_for('secondPage'))

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        return run_flask_app()
    else:
        return render_template('index1.html')

if __name__ == "__main__":
    print("Starting the Flask Application!")
    app.run(host='0.0.0.0', port=2000)