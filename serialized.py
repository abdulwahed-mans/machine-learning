import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample training data
X_train = ["Apple", "Chocolate", "Banana", "Candy", "Milk"]
y_train = ["Healthy", "Unhealthy", "Healthy", "Unhealthy", "Healthy"]

# Sample testing data
X_test = ["Chips", "Yogurt", "Soda"]
y_test = ["Unhealthy", "Healthy", "Unhealthy"]

# Vectorize the input data
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Initialize and train the classifier
classifier = LogisticRegression()
classifier.fit(X_train_vectorized, y_train)

# Predict on the test data
y_pred = classifier.predict(X_test_vectorized)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the trained model to a file named serialized_model.pkl
model_path = 'serialized_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump((vectorizer, classifier), f)