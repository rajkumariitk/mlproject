# Any code that is related to data transformation , that will be written here

import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.Logger import logging

import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):


        try:
            numerical_feature = ['reading score', 'writing score']
            categorical_feature = [
                'gender', 
                'race/ethnicity',
                  'parental level of education',
                    'lunch',
                      'test preparation course'
                      ]
            
        except:
            pass