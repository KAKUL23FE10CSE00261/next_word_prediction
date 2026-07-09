# 🧠 Next Word Prediction using LSTM

A Deep Learning web application that predicts the next word in a sentence using an LSTM (Long Short-Term Memory) neural network. The project is built with TensorFlow/Keras and deployed using Streamlit.

## 🚀 Live Demo

**Streamlit App:**  
https://kakul23fe10cse00261-sentence-completion-app-3mvahv.streamlit.app/

---

## 📌 Features

- Predicts the next word from a given sentence
- LSTM-based language model
- Interactive Streamlit web interface
- Fast and easy-to-use application
- Pre-trained model included

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pickle

---

## 📂 Project Structure

```
sentence-completion/
│── app.py
│── lstm_model.h5
│── tokenizer.pkl
│── max_len.pkl
│── requirements.txt
│── README.md
│── LICENSE
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/sentence-completion.git
```

### Navigate to the project

```bash
cd sentence-completion
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 🎯 How to Use

1. Open the web application.
2. Enter a sentence.
3. Click **Predict**.
4. The model predicts the most probable next word.

### Example

**Input**

```
What are you
```

**Output**

```
doing
```

---

## 🧠 Model Architecture

- Embedding Layer
- LSTM Layer (128 Units)
- Dense Output Layer with Softmax Activation

### Loss Function

- Sparse Categorical Crossentropy

### Optimizer

- Adam

---

## 📊 Dataset

The model is trained on a custom English quotes dataset containing thousands of sentences. The text is tokenized, converted into input-output sequences, and used to train the LSTM network for next-word prediction.

---

## 🔮 Future Improvements

- Predict multiple words instead of a single word
- Beam Search decoding
- Transformer-based language model
- Improved UI/UX
- Mobile-friendly interface

---

## 👨‍💻 Author

**Kakul Barsaiya**

B.Tech CSE Student  
Machine Learning & Data Science Enthusiast

---

## 📄 License

This project is licensed under the MIT License.
