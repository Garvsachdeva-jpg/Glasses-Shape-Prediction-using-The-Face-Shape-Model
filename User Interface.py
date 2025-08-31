import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# --- Config ---
IMG_SIZE = (128, 128)
CLASS_NAMES = ['oval', 'Round', 'Square', 'Heart', 'Long']

# --- Spectacle Recommendations ---
spectacle_suggestions = {
    "Oval": ["Square", "Rectangle", "Geometric"],
    "Long": ["Tall frames", "Wayfarers", "Oversized"],
    "Round": ["Rectangle", "Angular", "Cat-eye"],
    "Square": ["Round", "Oval", "Rimless"],
    "Heart": ["Light-colored", "Rimless", "Bottom-heavy"],
    
}

# --- Load model and label encoder ---
model = load_model("simple_face_shape_model.h5")  # Ensure model file is in the same folder
label_encoder = LabelEncoder()
label_encoder.fit(CLASS_NAMES)

# --- Preprocess uploaded or captured image ---
def preprocess_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    if image is not None:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_resized = cv2.resize(image_rgb, IMG_SIZE)
        image_normalized = image_resized.astype('float32') / 255.0
        return image_rgb, np.expand_dims(image_normalized, axis=0)
    return None, None

# --- Streamlit UI ---
st.title("📸 Face Shape & Spectacle Style Recommender")
st.write("Upload or capture a face image to predict the face shape and get perfect spectacle suggestions! 👓")

# === Upload or Camera input ===
upload_option = st.radio("Choose input method:", ["Upload Image", "Use Camera"])

image_rgb = None
image_input = None

if upload_option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image_rgb, image_input = preprocess_image(uploaded_file)

elif upload_option == "Use Camera":
    captured_image = st.camera_input("Take a picture")
    if captured_image:
        image_rgb, image_input = preprocess_image(captured_image)

# === If image is processed successfully ===
if image_input is not None:
    st.image(image_rgb, caption="Input Image", use_container_width=True)

    # --- Prediction ---
    prediction = model.predict(image_input)
    predicted_index = np.argmax(prediction[0])
    predicted_label = label_encoder.inverse_transform([predicted_index])[0]
    confidence = prediction[0][predicted_index]

    # --- Output ---
    st.markdown(f"### 🧠 Predicted Face Shape: *{predicted_label.upper()}*")
    st.markdown(f"*Confidence:* {confidence:.2f}")

    # --- Spectacle Suggestion ---
    suggestions = spectacle_suggestions.get(predicted_label, [])
    if suggestions:
        st.markdown("### 👓 Recommended Spectacle Styles:")
        for style in suggestions:
            st.write(f"- {style}")
    else:
        st.warning("No suggestion found for this face shape.")