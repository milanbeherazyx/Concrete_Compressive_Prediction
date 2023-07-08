import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            return model.predict(data_scaled)
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
        
class CustomData:
    def __init__(  self,
        Cement: float,
        Blast_Furnace_Slag: float,
        Fly_Ash: float,
        Water: float,
        Superplasticizer: float,
        Coarse_Aggregate: float,
        Fine_Aggregate: float,
        Age: int):

        self.Cement = Cement

        self.Blast_Furnace_Slag = Blast_Furnace_Slag

        self.Fly_Ash = Fly_Ash

        self.Water = Water

        self.Superplasticizer = Superplasticizer

        self.Coarse_Aggregate = Coarse_Aggregate

        self.Fine_Aggregate = Fine_Aggregate
        
        self.Age = Age

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Cement": [self.Cement],
                "Blast_Furnace_Slag": [self.Blast_Furnace_Slag],
                "Fly_Ash": [self.Fly_Ash],
                "Water": [self.Water],
                "Superplasticizer": [self.Superplasticizer],
                "Coarse_Aggregate": [self.Coarse_Aggregate],
                "Fine_Aggregate": [self.Fine_Aggregate],
                "Age": [self.Age],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys) from e

