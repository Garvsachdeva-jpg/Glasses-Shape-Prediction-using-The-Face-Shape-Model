import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# --- Config ---
IMG_SIZE = (128, 128)
CLASS_NAMES = ['Oval', 'Round', 'Square', 'Heart', 'Long']

# --- Spectacle Recommendations ---
spectacle_suggestions = {
    "Oval": ["Square", "Rectangle", "Geometric"],
    "Long": ["Tall frames", "Wayfarers", "Oversized"],
    "Round": ["Rectangle", "Angular", "Cat-eye"],
    "Square": ["Round", "Oval", "Rimless"],
    "Heart": ["Light-colored", "Rimless", "Bottom-heavy"],
}

# --- Load model and label encoder ---
@st.cache_resource
def load_prediction_model():
    """Loads the pre-trained face shape prediction model."""
    try:
        return load_model("simple_face_shape_model.h5")
    except (FileNotFoundError, IOError) as e:
        st.error(f"⚠️ Model file not found! Please ensure 'simple_face_shape_model.h5' is in the correct directory. Details: {e}")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred while loading the model: {e}")
        st.stop()


@st.cache_resource
def load_face_cascade():
    """Loads the Haar cascade for face detection."""
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    return cv2.CascadeClassifier(cascade_path)

model = load_prediction_model()
face_cascade = load_face_cascade()

label_encoder = LabelEncoder()
label_encoder.fit(CLASS_NAMES)

# --- Image Processing ---
def preprocess_image(uploaded_file):
    """
    Reads an uploaded file, detects the largest face, preprocesses it,
    and returns both the original image with the face highlighted and the
    processed face image for the model.
    """
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    if image is None:
        st.error("Could not decode image. Please upload a valid image file.")
        return None, None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        image_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    if len(faces) == 0:
        st.warning("⚠️ No face detected. Please try another image with a clearer view of the face.")
        return image_rgb, None

    # Assume the largest detected face is the main one
    (x, y, w, h) = max(faces, key=lambda item: item[2] * item[3])
    
    # Draw a rectangle around the face on the original image
    cv2.rectangle(image_rgb, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Crop the face
    face_roi = image_rgb[y:y+h, x:x+w]

    # Preprocess for model
    face_resized = cv2.resize(face_roi, IMG_SIZE)
    face_normalized = face_resized.astype('float32') / 255.0
    image_input = np.expand_dims(face_normalized, axis=0)
    
    return image_rgb, image_input


def make_prediction(image_input):
    """Makes a prediction and returns the label and confidence."""
    prediction = model.predict(image_input)
    predicted_index = np.argmax(prediction[0])
    predicted_label = label_encoder.inverse_transform([predicted_index])[0]
    confidence = prediction[0][predicted_index]
    return predicted_label, confidence

# --- Streamlit UI ---
st.set_page_config(layout="wide")
st.title("📸 Face Shape & Spectacle Style Recommender")
st.write("Upload or capture a face image to predict the face shape and get perfect spectacle suggestions! 👓")

st.info("**How it works:** The app will first detect a face in your image, then predict its shape, and finally recommend spectacle styles that compliment it.")

# === Upload or Camera input ===
upload_option = st.radio("Choose input method:", ["Upload Image", "Use Camera"], horizontal=True)

image_to_display = None
processed_image = None

if upload_option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image_to_display, processed_image = preprocess_image(uploaded_file)

elif upload_option == "Use Camera":
    captured_image = st.camera_input("Take a picture")
    if captured_image:
        image_to_display, processed_image = preprocess_image(captured_image)


# === Display results if image is processed successfully ===
if image_to_display is not None:
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_to_display, caption="Input Image with Detected Face", use_container_width=True)

    if processed_image is not None:
        predicted_label, confidence = make_prediction(processed_image)

        with col2:
            st.markdown(f"### 🧠 Predicted Face Shape:")
            st.markdown(f"## **{predicted_label.upper()}**")
            st.progress(float(confidence))
            st.markdown(f"**Confidence:** {confidence:.2%}")

            st.markdown("---")
            
            suggestions = spectacle_suggestions.get(predicted_label, [])
            if suggestions:
                st.markdown("### 👓 Recommended Spectacle Styles:")
                for style in suggestions:
                    st.markdown(f"- **{style}**")

                st.markdown("---")
                amazon_url = f"https://www.amazon.in/s?k=glasses+frames+for+{predicted_label}+face+shape"
                st.markdown(f"### 🛍️ [Find best frames on Amazon]({amazon_url})")
            else:
                st.warning("No spectacle suggestions found for this face shape.")
else:
    st.info("Upload an image or use your camera to get started.")
