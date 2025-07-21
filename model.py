import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Config
IMG_SIZE = (128, 128)
CLASS_NAMES = ['Oval', 'Round', 'Square', 'Heart','Long']

# Load images
def load_images(dataset_dir):
    images, labels = [], []
    for label in CLASS_NAMES:
        path = os.path.join(dataset_dir, label)
        if not os.path.exists(path):
            continue
        for img_name in os.listdir(path):
            if img_name.lower().endswith(('.jpg', '.png', '.jpeg')):
                img_path = os.path.join(path, img_name)
                img = cv2.imread(img_path)
                if img is not None:
                    img = cv2.resize(img, IMG_SIZE)
                    img = img.astype('float32') / 255.0
                    images.append(img)
                    labels.append(label)
    return np.array(images), np.array(labels)

# Build CNN model
def create_model():
    model = models.Sequential([
        layers.Input(shape=(128, 128, 3)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D(2),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(len(CLASS_NAMES), activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Train the model
def main():
    print("Loading images...")
    X, y = load_images("training_set")  # Update this if your folder name is different

    if len(X) == 0:
        print("No images found! Check your folder path and class folders.")
        return

    # Encode labels to numbers and one-hot
    le = LabelEncoder()
    y = le.fit_transform(y)
    y = tf.keras.utils.to_categorical(y, num_classes=len(CLASS_NAMES))

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train model
    model = create_model()
    model.fit(X_train, y_train, epochs=15, batch_size=32, validation_data=(X_test, y_test))

    # Save model
    model.save("simple_face_shape_model.h5")
    print("Model saved as simple_face_shape_model.h5")

if __name__ == "__main__":
    main()