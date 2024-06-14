import pickle
from sklearn.pipeline import Pipeline

def load_sklearn_model():
    with open("models/pickle/model.pkl", "rb") as file:
        model = pickle.load(file)
    return model


MODEL: Pipeline = load_sklearn_model()
