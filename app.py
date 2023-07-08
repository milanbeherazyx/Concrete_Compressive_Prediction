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
    """
    Render the home page.
    """
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    """
    Handle the prediction request.
    """
    if request.method == 'GET':
        return render_template('home.html')
    # Get the input data from the form
    try:
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
    except (TypeError, ValueError):
        # Invalid input data, handle the error
        return render_template('home.html', error='Invalid input data')

    pred_df = data.get_data_as_data_frame()
    print(pred_df)

    predict_pipeline = PredictPipeline()

    try:
        results = predict_pipeline.predict(pred_df)
        result_value = results[0]
    except Exception as e:
        # Handle the prediction error
        return render_template('home.html', error='Prediction failed')

    return render_template('home.html', results=result_value)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
