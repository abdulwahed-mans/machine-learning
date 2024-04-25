# chat/views.py
from django.shortcuts import render
from .forms import ProductForm
from .ml_model import predict_sentiment
import pickle

# Load the serialized ML model
with open('serialized_model.pkl', 'rb') as f:
    vectorizer, classifier = pickle.load(f)

def predict_product(request):
    product_name = None
    prediction = None

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            # Vectorize the input
            input_vectorized = vectorizer.transform([product_name])
            # Use the model to make predictions
            prediction = classifier.predict(input_vectorized)[0]

    else:
        form = ProductForm()

    return render(request, 'chat/product_form.html', {'form': form, 'product_name': product_name, 'prediction': prediction})
