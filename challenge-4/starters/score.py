import pickle

from azureml.api.schema.dataTypes import DataTypes
from azureml.api.schema.sampleDefinition import SampleDefinition
from azureml.api.realtime.services import generate_schema
from azureml.assets import get_local_path

model = None


def init():
    """
    This method initializes the service.
    The goal is to assign the global variable model with your model.
    """

    global model

    local_path = get_local_path('assets/model.pkl.link')

    #TODO: Load your model from the local_path

def run(data):
    """
    This method is used to make predictions. Notice that you need to return a JSON string from this method
    with the results in a format that the user of your service understands.

    :param data: The input data for the model
    :return: Returns the JSON output for the service
    """
    import json

    # TODO: Make a prediction and return the result


def generate_api_schema():
    import os
    import pandas as pd

    print("create schema")

    # TODO: Modify this sample input so that it matches the features used in your model.
    sample_input = {
        'sqft_above': 100.0,
        'sqft_basement': 120.0,
        'grade': 3,
        'condition': 1,
        'bedrooms': 3,
        'waterfront': 1,
        'floors': 2,
        'sqft_lot': 10000
    }

    sample_df = pd.DataFrame([sample_input])

    inputs = {
        'data': SampleDefinition(DataTypes.PANDAS, sample_df),
    }

    os.makedirs('outputs', exist_ok=True)

    print(generate_schema(inputs=inputs, filepath="outputs/schema.json", run_func=run))


# Implement test code to run in IDE or Azure ML Workbench
if __name__ == '__main__':
    # Import the logger only for Workbench runs
    from azureml.logging import get_azureml_logger

    logger = get_azureml_logger()

    import argparse
    import json
    import pandas as pd

    parser = argparse.ArgumentParser()
    parser.add_argument('--generate', action='store_true', help='Generate Schema')
    args = parser.parse_args()

    if args.generate:
        generate_api_schema()

    init()

    # TODO: Change this to the features that are actually used by your model.
    input = pd.DataFrame([{
        'sqft_above': 100.0,
        'sqft_basement': 120.0,
        'grade': 3,
        'condition': 1,
        'bedrooms': 3,
        'waterfront': 1,
        'floors': 2,
        'sqft_lot': 10000
    }])

    result = run(input)

    logger.log("Result", result)
