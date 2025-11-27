
# ✅ **README.md (Complete & Professional)**

````markdown
# 🏡 House Price Prediction Web App  
Using Machine Learning (SVC Model) & Flask

This project is a **machine learning–powered web application** that predicts house prices based on multiple property features such as bedrooms, bathrooms, living area, lot size, condition, location, etc.  

The model is trained using **Support Vector Classifier (SVC)**, and the frontend is powered by an elegant, responsive Bootstrap UI with dark/light mode support.  

---

## 🚀 Features

### 🔹 **Machine Learning**
- Trained SVC model (`model_svc.pkl`)
- Encodes categorical data using LabelEncoder
- Reads processed dataset (`processed_data.csv`)
- Predicts price using 15 key features

### 🔹 **Flask Web Application**
- `/` route serves prediction form  
- `/predict` route processes user input & returns predicted price  
- Serves dropdown values dynamically from dataset

### 🔹 **Frontend UI**
- Fully responsive UI  
- Dark/Light theme toggle  
- Clean Bootstrap layout  
- Icons from FontAwesome  
- Beautiful gradients & shadows  

---

## 🧠 How It Works

### 🔸 1. Load Model  
```python
model_svc = pickle.load(open('model_svc.pkl', 'rb'))
````

### 🔸 2. Read Dataset for Dropdowns

```python
data = pd.read_csv('processed_data.csv')
```

### 🔸 3. Apply Label Encoding for Categorical Features

```python
label_encoders['city'].fit_transform(data['city'])
```

### 🔸 4. Predict Price

After form submission, features are collected and fed to the model:

```python
predicted_price = model_svc.predict([features])[0]
```

---

## 📁 Project Structure

```
├── app.py
├── model_svc.pkl
├── processed_data.csv
├── templates/
│   └── index.html
├── static/ (optional)
│   ├── styles.css
│   └── script.js
└── README.md
```

---

## 🛠️ Installation & Setup

### **1. Clone the Repository**

```bash
git clone https://github.com/habiba-cyber/Tik-Tac-Toe
cd Tik-Tac-Toe
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, create it manually:

```
flask
sklearn
pandas
numpy
```

### **3. Run the App**

```bash
python app.py
```

Your application starts at:

```
http://127.0.0.1:5000/
```

---

## 🧰 Technologies Used

| Component     | Technology               |
| ------------- | ------------------------ |
| Backend       | Python, Flask            |
| ML Model      | Scikit-Learn (SVC)       |
| Frontend      | HTML5, CSS3, Bootstrap 5 |
| Icons         | FontAwesome              |
| Data Handling | pandas, pickle           |

---

## 🖼️ Screenshots

(Add your own screenshots—UI looks beautiful!)

---

## 📊 Prediction Inputs

The user provides:

* Bedrooms
* Bathrooms
* Floors
* Square Foot Living
* Square Foot Lot
* Waterfront
* View Quality
* Condition
* Year Built
* Year Renovated
* Street
* City
* StateZip
* Sqft Above
* Sqft Basement

These values are preprocessed, encoded, and fed to the model.

---

## 🧪 Model File

Ensure the following files exist:

| File                 | Purpose                                       |
| -------------------- | --------------------------------------------- |
| `model_svc.pkl`      | Trained price prediction model                |
| `processed_data.csv` | Dataset used to generate dropdowns & encoders |

---

## 📦 Deployment

You can deploy on:

* **Render**
* **Railway**
* **Heroku**
* **PythonAnywhere**
* **AWS EC2 / Lightsail**

