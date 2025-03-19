# to open the model file

import joblib

loaded_model = joblib.load("final_model/Final_trained_lr_model.pkl")

print(type(loaded_model))
print(loaded_model)
