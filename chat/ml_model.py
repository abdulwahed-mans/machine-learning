# chat/ml_model.py
import pickle

# Load the serialized model
with open('serialized_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_sentiment(text):
    # Preprocess the text input (e.g., tokenize, vectorize)
    # Perform sentiment analysis using the loaded model
    sentiment = model.predict([text])[0]
    return sentiment
