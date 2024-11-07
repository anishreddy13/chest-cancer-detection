import os
import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Initialize the Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')  # Updated static_folder

# Load your trained machine learning model
model = load_model('chest_cancer_model.h5')  # Updated with the correct path

# Define a function to make predictions
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image

    prediction = model.predict(img_array)
    if prediction[0][0] > 0.5:
        return "No cancer detected"
    else:
        return "Cancer detected"

# Route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')  # This will look for index.html in the 'templates' folder

# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Check if the 'uploads' directory exists, if not, create it
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    if 'image' not in request.files:
        return jsonify({'message': 'No file uploaded'})

    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No file selected'})

    # Save the uploaded file
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Make the prediction
    result = predict_image(file_path)
    os.remove(file_path)  # Clean up the uploaded file
    return jsonify({'message': result})

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
