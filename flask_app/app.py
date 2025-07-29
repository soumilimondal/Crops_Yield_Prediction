from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained Joblib model
crop_model = joblib.load("model.joblib")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/crop', methods=['GET', 'POST'])
def crop():
    if request.method == 'POST':
        try:
            # Get user inputs
            nitrogen = float(request.form['N'])
            phosphorus = float(request.form['P'])
            potassium = float(request.form['K'])
            temperature = float(request.form['Temp'])
            humidity = float(request.form['Hum'])
            ph = float(request.form['Ph'])
            rainfall = float(request.form['Ra'])

            # print(f"Inputs: N={nitrogen}, P={phosphorus}, K={potassium}, Temp={temperature}, Hum={humidity}, pH={ph}, Rainfall={rainfall}")

            # Convert inputs to numpy array and predict
            input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
            prediction = crop_model.predict(input_data)[0]
            
            
            # print(f"Predicted Crop: {prediction}")
            # Redirect to pred_crop with prediction
            return redirect(url_for('pred_crop', pcrop=prediction))

        except Exception as e:
            return f"Error: {e}"

    return render_template('crop.html')

@app.route('/pred_crop', methods=['GET', 'POST'])
def pred_crop():
    pcrop = request.args.get('pcrop')  # Get prediction from URL parameters
    return render_template('pred_crop.html', pcrop=pcrop)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
