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

# TODO: Train your model
# TODO: Validate your model

########################## STEP 2: Store the model #############################

# Create the outputs folder - save any outputs you want managed by AzureML here
os.makedirs('./outputs', exist_ok=True)

# TODO: Store your model

################################################################################
