from .settings import CURR_PATH
import joblib
import os


def load_model(model_file):
    model = joblib.load(os.path.join(CURR_PATH, '../model', model_file))
    return model

def make_prediction(query):
    model = load_model('pipeline.joblib')
    response = model.predict([query])[0]
    return response