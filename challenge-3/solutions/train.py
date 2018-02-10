# Spark configuration and packages specification. The dependencies defined in
# this file will be automatically provisioned for each run that uses Spark.

import os

import pickle

from azureml.logging import get_azureml_logger
from azureml.dataprep import package

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# initialize the logger
logger = get_azureml_logger()

########################## STEP 1: Train the model #############################

df = package.run('Data analysis.dprep', dataflow_idx=0)

df_train, df_validation = train_test_split(df, test_size=0.2)

feature_names = ['sqft_above', 'sqft_basement', 'grade', 'condition', 'bedrooms', 'waterfront','floors', 'sqft_lot']

features = df_train[feature_names].values
y = df_train[['price']].values

model = LinearRegression()
model.fit(features, y)

validation_features = df_validation[feature_names].values
validation_y = df_validation[['price']].values

score = model.score(validation_features, validation_y)

logger.log('Score', score)

########################## STEP 2: Store the model #############################

# Create the outputs folder - save any outputs you want managed by AzureML here
os.makedirs('./outputs', exist_ok=True)

with open('./outputs/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

################################################################################
