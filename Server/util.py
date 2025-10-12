import json
import pickle
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # Try multiple possible paths for deployment flexibility
    base_dir = os.path.dirname(__file__)
    
    # First try the artifacts directory (for deployment)
    model_path = os.path.join(base_dir, 'artifacts', 'bangalore_home_prices_model')
    columns_path = os.path.join(base_dir, 'artifacts', 'columns.json')
    
    # If not found, try the Model directory (for local development)
    if not os.path.exists(model_path):
        model_path = os.path.join(base_dir, '../Model/bangalore_home_prices_model')
        columns_path = os.path.join(base_dir, '../Model/columns.json')
    
    print(f"Looking for model at: {model_path}")
    print(f"Looking for columns at: {columns_path}")


    try:
        with open(columns_path, 'r') as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]

        with open(model_path, 'rb') as f:
            __model = pickle.load(f)

        print("loading saved artifacts...done")
    except FileNotFoundError as e:
        print(f"Error: Could not find required files. {e}")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Files in current directory: {os.listdir('.')}")
        raise
    except Exception as e:
        print(f"Error loading artifacts: {e}")
        raise

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP nagar', 1000, 3, 3))