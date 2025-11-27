
import pickle
import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
model_svc = pickle.load(open('model_svc.pkl', 'rb'))  # Model Loading

# Load the processed dataset to extract categorical values for dropdowns
data = pd.read_csv('processed_data.csv')

# Store original categorical values before encoding
original_streets = data['street'].unique()
original_cities = data['city'].unique() 
original_statezips = data['statezip'].unique()

# Create LabelEncoders for categorical columns
label_encoders = {
    'waterfront': LabelEncoder(),
    'view': LabelEncoder(),
    'condition': LabelEncoder(),
    'street': LabelEncoder(),
    'city': LabelEncoder(),
    'statezip': LabelEncoder()
}

# Fit the label encoders on the dataset (only on the categorical columns)
for col in label_encoders:
    data[col] = label_encoders[col].fit_transform(data[col])

# Home route to render the form with dropdown options
@app.route('/')
def home():
    # Use original values for dropdowns
    return render_template('index.html', 
                         streets=original_streets, 
                         cities=original_cities, 
                         statezips=original_statezips)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Extract and preprocess the form data
    features = [
        float(request.form['bedrooms']),
        float(request.form['bathrooms']),
        float(request.form['sqft_living']),
        float(request.form['sqft_lot']),
        float(request.form['floors']),
        int(request.form['waterfront']),
        int(request.form['view']),
        int(request.form['condition']),
        float(request.form['sqft_above']),
        float(request.form['sqft_basement']),
        int(request.form['yr_built']),
        int(request.form['yr_renovated']),
        label_encoders['street'].transform([request.form['street']])[0],  # Encoding categorical variables
        label_encoders['city'].transform([request.form['city']])[0],
        label_encoders['statezip'].transform([request.form['statezip']])[0]
    ]

    # Make prediction using the model
    predicted_price = model_svc.predict([features])[0]

    return render_template('index.html', prediction_text=f'Predicted Price: ${predicted_price:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
