# Concrete Compressive Strength Prediction

This project aims to predict the compressive strength of concrete based on various input features. It utilizes machine learning regression models to make accurate predictions.

![Concrete Compressive Prediction](Concrete_Compressive_Strength_Prediction.jpg)

## Introduction

The Concrete Compressive Strength Prediction project utilizes machine learning techniques to predict the compressive strength of concrete. By analyzing the relationship between various input features such as cement, blast furnace slag, fly ash, water, superplasticizer, coarse aggregate, fine aggregate, and age, the project provides an accurate estimate of the compressive strength.

The project includes a Flask web application that allows users to input concrete properties and obtain the predicted compressive strength. It also provides functionality to train and evaluate different regression models.

## Dataset

The dataset used for this project is located in the `data` directory. The file `concrete_data.csv` contains the concrete compressive strength data along with the corresponding input features. The dataset is used for training the regression models.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/milanbeherazyx/Concrete_Compressive_Prediction.git
```

2. Navigate to the project directory:

```shell
cd Concrete_Compressive_Prediction
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Requirements

The project requires the following dependencies:

- Flask==2.0.2
- numpy==1.21.2
- pandas==1.3.3
- scikit-learn==0.24.2

Create a virtual environment (optional) and activate it before installing the dependencies. You can use the following commands:

```shell
python -m venv venv
source venv/bin/activate
```

These dependencies can also be found in the `requirements.txt` file.

## Usage

To run the Flask web application, execute the following command:

```shell
python app.py
```

Access the application in your web browser by visiting `http://localhost:5000`. Use the input form to enter the concrete properties and click the "Predict" button to obtain the predicted compressive strength.

To train and evaluate different regression models, modify the code in the `train_pipeline.py` script according to your requirements. Run the script to train the models and save them in the `models` directory.

## Contributing

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, please create a pull request. Ensure that you follow the project's coding conventions and provide clear commit messages.

