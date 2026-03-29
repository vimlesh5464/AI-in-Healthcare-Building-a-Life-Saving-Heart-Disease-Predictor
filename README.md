Heart Disease Prediction Project
Project Overview:

This project predicts the risk of heart disease in patients using machine learning. It allows users to input medical data such as age, sex, chest pain type, blood pressure, cholesterol, and other features, and outputs a prediction of heart disease risk.

The main goal is to help in early detection and preventive care by providing predictive insights to doctors and patients.

Features:
Predicts presence or absence of heart disease.
Provides low-risk / high-risk predictions.
Uses multiple machine learning models (CatBoost, Random Forest, XGBoost) for evaluation.

Displays feature importance to highlight key medical indicators.
Interactive web interface built with Flask, HTML, and CSS.

Dataset:
Original dataset: heart(1).xls
Contains features like:
Age, Sex, Chest Pain Type (cp), Blood Pressure (trestbps), Cholesterol (chol)
Fasting Blood Sugar (fbs), Resting ECG (restecg), Max Heart Rate (thalach)
Exercise-induced angina (exang), ST depression (oldpeak), Slope, Major Vessels (ca), Thal
Target variable: 0 = No Heart Disease, 1 = Heart Disease


Installation & Setup:

Clone the repository
git clone <your-repo-link>
cd Day-4

Create virtual environment:
python -m venv ml_env

Activate environment
On Mac/Linux:
source ml_env/bin/activate

On Windows:
ml_env\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the Flask app:
python app.py
Open your browser
Go to http://127.0.0.1:5000

 to use the app.
Project Structure
Day-4/
├── app.py                  # Main Flask app
├── heart_disease_pipeline.pkl # Trained ML pipeline
├── heart(1).xls            # Dataset
├── templates/
│   └── index.html          # HTML frontend
├── static/
│   └── style.css           # CSS file
├── catboost_info/          # CatBoost training metadata
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation


How it Works:
User inputs patient medical data via the web form.
Data is preprocessed and passed to the trained ML model.
Model predicts whether the patient has heart disease (1) or no heart disease (0).
Optional: Feature importance visualizations help understand key indicators.


Challenges Faced:
Handling missing values and categorical features.
Selecting the right model to avoid overfitting.
Integrating preprocessing, model training, and visualization into a single workflow.
Evaluating model performance across multiple metrics.

Future Improvements:
Use a larger and more diverse dataset.
Incorporate longitudinal patient data for better predictions.
Explore deep learning models for improved accuracy.
Deploy as a clinical decision support system or mobile health app.

Tools & Libraries:
Python: pandas, NumPy, scikit-learn, CatBoost, XGBoost
Web Development: Flask, HTML, CSS
Visualization: Matplotlib, Seaborn

Author:
Your Name – Vimlesh Gupta
GL Bajaj Group of Institutions, Mathura