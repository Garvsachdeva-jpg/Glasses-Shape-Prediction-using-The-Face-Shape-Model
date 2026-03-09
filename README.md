🚀 Overview
This repository contains a complete pipeline to:

Classify a user's face shape (Oval, Square, Round, Heart, or Oblong) using a Convolutional Neural Network (CNN).

Recommend specific glasses frames that complement those unique facial features.

Deployed the model via a user-friendly interface for real-time predictions:
https://glasses-shape-prediction-using-the-face-shape-model.streamlit.app/

🛠️ Tech Stack
Language: Python

Deep Learning: TensorFlow / Keras (CNN architecture)

UI Framework: Streamlit / Tkinter (as seen in User Interface.py)

Image Processing: OpenCV, PIL

📂 Project Structure
model.py: Script for loading and running inference on the neural network.

simple_face_shape_model.h5: The pre-trained weights for the Face Shape Classifier.

User Interface.py: The frontend application that allows users to upload photos and get results.

requirements.txt: List of necessary dependencies to get the project running.

⚙️ Installation & Usage
1. Clone the repository
Bash
git clone https://github.com/Garvsachdeva-jpg/Glasses-Shape-Prediction-using-The-Face-Shape-Model.git
cd Glasses-Shape-Prediction-using-The-Face-Shape-Model
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Run the Application
Bash
python "User Interface.py"
🧠 How it Works
The logic follows the "Rule of Opposites" in fashion:
| Face Shape | Recommended Frames | Why? |
| :--- | :--- | :--- |
| Round | Rectangular / Geometric | Adds angles to soften roundness. |
| Square | Round / Oval | Softens a strong jawline. |
| Heart | Bottom-heavy / Cat-eye | Balances a wider forehead. |
| Oval | Most shapes (especially Walnut) | Maintains natural balance. |

