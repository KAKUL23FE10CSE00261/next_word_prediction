import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ------------------------------
# Streamlit Config
# ------------------------------
st.set_page_config(
    page_title="Next Word Prediction",
    page_icon="🧠",
    layout="centered"
)

# ------------------------------
# Load Resources
# ------------------------------
@st.cache_resource
def load_resources():
    try:
        model = load_model("lstm_model.h5")

        with open("tokenizer.pkl", "rb") as f:
            tokenizer = pickle.load(f)

        with open("max_len.pkl", "rb") as f:
            max_len = pickle.load(f)

        index_to_word = {
            index: word
            for word, index in tokenizer.word_index.items()
        }

        return model, tokenizer, max_len, index_to_word

    except Exception as e:
        st.error(f"Error loading files:\n\n{e}")
        st.stop()


model, tokenizer, max_len, index_to_word = load_resources()

# ------------------------------
# Prediction Function
# ------------------------------
def predict_next_word(text):

    text = text.lower().strip()

    sequence = tokenizer.texts_to_sequences([text])[0]

    if len(sequence) == 0:
        return "Unknown"

    sequence = pad_sequences(
        [sequence],
        maxlen=max_len - 1,
        padding="pre"
    )

    prediction = model.predict(sequence, verbose=0)

    predicted_index = np.argmax(prediction)

    return index_to_word.get(predicted_index, "Unknown")


# ------------------------------
# UI
# ------------------------------
st.title("🧠 Next Word Prediction")
st.write("Enter a sentence and the LSTM model will predict the next word.")

user_input = st.text_input(
    "Enter a sentence",
    placeholder="Example: What are you"
)

if st.button("Predict"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        word = predict_next_word(user_input)

        st.success(f"### Predicted Word: **{word}**")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("Developed using TensorFlow, Keras and Streamlit")
