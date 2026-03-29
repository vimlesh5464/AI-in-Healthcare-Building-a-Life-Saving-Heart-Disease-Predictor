from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the full pipeline (preprocessor + model)
pipeline = joblib.load('heart_disease_pipeline.pkl')

# Feature names (same as during training)
features = ['age','sex','cp','trestbps','chol','fbs','restecg',
            'thalach','exang','oldpeak','slope','ca','thal']

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Collect form data
        data = {}
        for feature in features:
            value = request.form.get(feature)
            if value is not None:
                # Convert numeric/categorical features
                if feature in ['age','trestbps','chol','thalach','oldpeak']:
                    data[feature] = [float(value)]
                else:
                    data[feature] = [int(value)]

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Predict using the full pipeline (preprocessor + model)
        pred = pipeline.predict(df)[0]
        prediction = int(pred)  # 0 = No Disease, 1 = Disease

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)