from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Cement=float(request.form.get('Cement')),
            Blast_Furnace_Slag=float(request.form.get('Blast_Furnace_Slag')),
            Fly_Ash=float(request.form.get('Fly_Ash')),
            Water=float(request.form.get('Water')),
            Superplasticizer=float(request.form.get('Superplasticizer')),
            Coarse_Aggregate=float(request.form.get('Coarse_Aggregate')),
            Fine_Aggregate=float(request.form.get('Fine_Aggregate')),
            Age=int(request.form.get('Age'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()

        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0")