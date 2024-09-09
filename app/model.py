import joblib

class CropRecommendationModel:
    def __init__(self):
        # Load the trained model
        self.model = joblib.load('app/models/crop_recommendation_model.pkl')

    def recommend_crop(self, features):
        # Convert features into the format required by the model and predict
        # This is just a placeholder; adjust according to your model's requirements
        # For example, you may need to convert the features dictionary to a DataFrame
        import pandas as pd
        features_df = pd.DataFrame([features])
        prediction = self.model.predict(features_df)
        return prediction[0]
