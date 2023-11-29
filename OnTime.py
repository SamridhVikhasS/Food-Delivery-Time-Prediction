from tensorflow.keras.models import model_from_json

json_file = open("Food Delivery Time Prediction.json","r")
load_model_json = json_file.read()
model = model_from_json(load_model_json)
model.load_weights("Model Weights.h5")

def map_input(var,val):
    weather = {'Sunny': 0, 'Stormy': 1, 'Sandstorms': 2, 'Cloudy': 3, 'Fog': 4, 'Windy': 5}
    traffic = {'Low': 0, 'Medium': 1, 'High': 2, 'Jam': 3}
    order = {'Snack': 0, 'Drinks': 1, 'Buffet': 2, 'Meal': 3}
    vehicle = {'Motorcycle': 0, 'Scooter': 1, 'Electric Scooter': 2, 'Bicycle': 3}
    fest = {"No":0,"Yes":1}
    city = {'Urban': 0, 'Metropolitan': 1, 'Semi-Urban': 2}
    var_dict = {"weather":weather,"traffic":traffic,"order":order,"vehicle":vehicle,"fest":fest,"city":city}
    var_map = var_dict[var]
    return var_map[val]

def predict_time(*args):
    return model.predict([args])[0][0]