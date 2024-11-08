# chest-cancer-detection
# AayushAI: AI-Powered Lung Cancer Screening

**Author:** AnishReddy13

**Description:**

AayushAI is an AI-powered web application designed to assist in the early detection of lung cancer, specifically adenocarcinoma, by analyzing chest CT scans. This project was developed by students from Teegala Krishna Reddy Engineering College.

**Key Features:**

*   AI-powered analysis of chest CT scans for early detection of adenocarcinoma.
*   Fast and efficient results.
*   Designed to assist healthcare professionals in their diagnosis.
*   Prioritizes data security and privacy.

**How to Use:**
 **Download the Dataset:**
   * Download the dataset from [Google Drive Link](https://drive.google.com/drive/folders/1Dj3Hd_NsTJ6IlxNuhIiCWSY33dkQLaNa?usp=sharing) or [Alternative Download Link (if applicable)].
   * Extract the dataset to a directory of your choice.
**Update Dataset Path:**
   * Open the `model_training.py` file (if provided).
   * Modify the `directory` path in the `ImageDataGenerator` to point to the location where you extracted the dataset. For example:
     ```python
     train_data = data_gen.flow_from_directory(
         directory=r"C:\path\to\your\dataset", 
         # ... rest of your code
     )
     ```
     
1.  **Clone the repository:** `https://github.com/anishreddy13/chest-cancer-detection.git`
2.  **Navigate to the project directory:
3.  **Run the Flask application:** `python app.py`
4.  **Open your web browser and go to:** `http://127.0.0.1:5001/`

**Modules Required:**

*   TensorFlow
*   Keras
*   Flask
*   NumPy
*   OpenCV (cv2)
*   Matplotlib (for model training visualization)
*   Scikit-learn (for model evaluation)

**Install Modules:**

```bash
pip install tensorflow keras flask numpy opencv-python matplotlib scikit-learn

Project Structure:

app.py: Contains the Flask application code for handling image uploads and predictions.
chest_cancer_model.h5: The trained machine learning model.
templates/index.html: The HTML code for the web interface.
uploads/: Directory to store uploaded images temporarily.
static/: Directory to store static files (CSS, JavaScript).
README.md: This file.
Contributing:

Contributions are welcome! Feel free to open issues or submit pull requests.

Disclaimer:

This tool is intended for educational and preliminary assessment purposes only. It is essential to consult with a qualified healthcare professional for a complete diagnosis and treatment plan.
