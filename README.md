# ❤️ Heart Disease Detection System

A Machine Learning-based web application that predicts the risk of heart disease using patient medical data. This project uses a **Random Forest Classifier** trained on a heart disease dataset and provides predictions through an interactive **Streamlit web interface**.

---

# 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help in timely diagnosis and treatment.

This Heart Disease Detection System allows users to enter medical parameters and instantly receive a prediction about heart disease risk.

The project is built using:
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle
- Machine Learning

---

# 🚀 Features

- Real-time heart disease prediction
- User-friendly Streamlit interface
- Risk probability score display
- Fast prediction using trained ML model
- Random Forest Classifier implementation
- Easy setup and deployment

---

# 🛠 Tech Stack

## Programming Language
- Python

## Frontend
- Streamlit

## Machine Learning
- Scikit-learn
- Random Forest Classifier

## Libraries
- Pandas
- NumPy
- Pickle

---

# 📂 Project Structure

```bash
Heart Disease Detection/
│
├── app.py
├── model.py
├── heart.csv
├── heart_model.pkl
├── requirements.txt
└── README.md
```

## File Description

### app.py
Contains the Streamlit web application code for user interaction and prediction.

### model.py
Contains machine learning model training code using Random Forest Classifier.

### heart.csv
Dataset used for training the model.

### heart_model.pkl
Saved trained machine learning model.

### requirements.txt
Contains all required Python dependencies.

### README.md
Project documentation.

---

# 📊 Dataset Information

This project uses the Heart Disease Dataset.

## Input Features

| Feature | Description |
|--------|-------------|
| age | Age of patient |
| sex | Gender |
| cp | Chest pain type |
| trestbps | Resting blood pressure |
| chol | Cholesterol level |
| fbs | Fasting blood sugar |
| restecg | Resting ECG result |
| thalach | Maximum heart rate achieved |
| exang | Exercise induced angina |
| oldpeak | ST depression induced by exercise |
| slope | Slope of peak exercise ST segment |
| ca | Number of major vessels |
| thal | Thalassemia |

## Target Variable

- 0 = No Heart Disease
- 1 = Heart Disease Detected

---

# 🤖 Machine Learning Model

This project uses **Random Forest Classifier**.

## Model Configuration

- Algorithm: Random Forest Classifier
- n_estimators = 300
- max_depth = 12
- train_test_split = 80:20
- stratify = True
- random_state = 42

## Why Random Forest?

Random Forest was chosen because:

- High prediction accuracy
- Handles non-linear relationships
- Reduces overfitting
- Works well with structured medical datasets
- No feature scaling required

---

# 🔄 Workflow

1. Load dataset from heart.csv
2. Select input features and target variable
3. Split data into training and testing sets
4. Train Random Forest model
5. Evaluate model accuracy
6. Save trained model as heart_model.pkl
7. Build Streamlit interface
8. Take user input
9. Convert categorical values into numeric values
10. Predict heart disease
11. Display result with probability score

---

# ⚙️ Installation Guide

## Step 1: Clone Repository

```bash
git clone https://github.com/your-username/heart-disease-detection.git
```

## Step 2: Move into Project Folder

```bash
cd heart-disease-detection
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Train the Model

```bash
python model.py
```

This will:
- Train the Random Forest model
- Evaluate accuracy
- Generate heart_model.pkl

---

## Run the Streamlit Application

```bash
streamlit run app.py
```

---

# 🖥 Application Interface

The web application allows users to input:

- Age
- Gender
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- Oldpeak
- Slope
- Number of Major Vessels
- Thalassemia

Then click:

```bash
Predict
```

to get:

- Heart Disease Prediction
- Risk Probability Score

---

# 📈 Example Prediction

## Input

```bash
Age: 54
Sex: Male
Chest Pain Type: Asymptomatic
Blood Pressure: 140
Cholesterol: 250
Exercise Induced Angina: Yes
```

## Output

```bash
⚠️ Heart Disease Detected
Risk Probability: 87.45%
```

---

# 🔍 Code Explanation

## model.py

This file:

- Loads heart.csv dataset
- Splits dataset into train/test
- Trains Random Forest model
- Calculates accuracy
- Saves trained model

Key functions used:

```python
pd.read_csv()
train_test_split()
RandomForestClassifier()
accuracy_score()
pickle.dump()
```

---

## app.py

This file:

- Loads trained model
- Builds Streamlit interface
- Takes user input
- Encodes categorical data
- Creates NumPy array
- Predicts output
- Displays probability score

Key functions used:

```python
pickle.load()
st.number_input()
st.selectbox()
st.button()
model.predict()
model.predict_proba()
```

---

# 🚧 Future Improvements

Possible enhancements:

- Add login authentication
- Store patient prediction history
- Deploy online
- Add REST API
- Add doctor dashboard
- Add PDF report generation
- Improve model accuracy
- Add hyperparameter tuning
- Add confusion matrix visualization

---

# ⚠️ Limitations

- Educational project only
- Small dataset
- Limited evaluation metrics
- Not suitable for real medical diagnosis
- No database integration

---

# ⚠️ Disclaimer

This application is created for educational and demonstration purposes only.

It should NOT be used as a substitute for professional medical diagnosis.

Always consult a healthcare professional.

---

# 👨‍💻 Author

**INDRANIL BHAUMIK**

Python Developer | Machine Learning Enthusiast

---

# ⭐ GitHub Support

If you found this project useful, please give it a ⭐ on GitHub.
