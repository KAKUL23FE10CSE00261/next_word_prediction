# 🧠 Next Word Prediction using LSTM

A Deep Learning project that predicts the next word in a sentence using an LSTM (Long Short-Term Memory) neural network. The application is built using TensorFlow/Keras and deployed with Streamlit.

---

## 🚀 Features

- Predicts the next word from a given sentence
- Built using LSTM Neural Network
- Interactive Streamlit web application
- Pre-trained model included
- Easy to use interface

---

## 🛠 Tech Stack

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pickle

---

## 📂 Project Structure

```
next_word_prediction/
│
├── app.py
├── lstm_model.h5
├── tokenizer.pkl
├── max_len.pkl
├── qoute_dataset.csv
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/KAKUL23FE10CSE00261//next-word-prediction.git
```

Move into the project

```bash
cd next-word-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Application

1. Enter a sentence.
2. Click **Predict Next Word**.
3. The model predicts the most probable next word.

Example

Input

```
What are you
```

Output

```
doing
```

---

## 🧠 Model

- Embedding Layer
- LSTM Layer
- Dense Output Layer (Softmax)

Loss Function

```
Sparse Categorical Crossentropy
```

Optimizer

```
Adam
```

---

## 📊 Dataset

The model is trained on a custom quotes dataset (`qoute_dataset.csv`) containing thousands of English sentences.

---

## Future Improvements

- Predict multiple words
- Beam Search prediction
- Transformer-based language model
- Better UI
- Deploy on Streamlit Community Cloud

---

## Author

**Kakul Barsaiya**

B.Tech CSE Student

Machine Learning & Data Science Enthusiast

---

## License

This project is licensed under the MIT License.
