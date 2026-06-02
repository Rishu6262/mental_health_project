# 🧠 Mental Health Prediction System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![NLP](https://img.shields.io/badge/NLP-Text%20Classification-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 🌐 Live Application

🚀 Live Demo:

https://mentalhealthproject-vggmug4wh94z3zqj8mgyyp.streamlit.app/

---

# 📌 Project Description

The Mental Health Prediction System is a Natural Language Processing (NLP) and Machine Learning based application that predicts mental health conditions from user-written text.

The system analyzes textual statements, emotions, and language patterns expressed by users and classifies them into predefined mental health categories.

By applying NLP preprocessing techniques and machine learning classification algorithms, the system learns patterns from mental health-related text data and predicts the most likely mental health status associated with a given input.

This project demonstrates how machine learning can be used to analyze human language and support mental health research through automated text classification.

---

# 🎯 Problem Statement

Mental health conditions such as depression, anxiety, stress, and emotional disorders are often reflected through written communication.

Large amounts of mental health-related content are generated daily on social media platforms, forums, blogs, and support communities.

Manually analyzing such data is time-consuming and difficult.

The objective of this project is to develop an automated text classification system that can identify mental health categories based on textual input using NLP and Machine Learning techniques.

---

# 🎯 Project Objectives

The main goals of this project are:

* Analyze mental health related text
* Apply Natural Language Processing techniques
* Perform text preprocessing and feature extraction
* Train machine learning classification models
* Predict mental health categories
* Understand patterns in mental health discussions
* Build an end-to-end NLP application
* Deploy the model using Streamlit

---

# 📊 Dataset Information

Dataset Name: Mental Health Text Dataset

Total Records: 992

Features:

### Input Feature

* Text

### Target Feature

* Status

The dataset contains mental health-related textual statements and their corresponding mental health labels.

---

# 🧠 How the System Works

### Step 1: User Input

The user enters a sentence, paragraph, or statement.

Example:

"I feel stressed every day and struggle to focus on my work."

---

### Step 2: Text Preprocessing

The input text is cleaned and prepared.

Operations include:

* Convert text to lowercase
* Remove punctuation
* Remove special characters
* Remove unnecessary spaces
* Tokenization
* Stopword removal

---

### Step 3: Feature Extraction

The cleaned text is converted into numerical vectors using NLP techniques.

Methods:

* Count Vectorizer
* TF-IDF Vectorizer

This allows machine learning algorithms to understand textual data.

---

### Step 4: Prediction

The trained machine learning model analyzes the extracted features and predicts the most appropriate mental health category.

---

### Step 5: Result Display

The predicted mental health status is displayed to the user through the Streamlit interface.

---

# 🔄 System Workflow

```text
User Text
    │
    ▼
Text Cleaning
    │
    ▼
Tokenization
    │
    ▼
Feature Extraction (TF-IDF)
    │
    ▼
Machine Learning Model
    │
    ▼
Mental Health Prediction
    │
    ▼
Final Result
```

---

# 🛠️ Technologies Used

## Programming Language

* Python

## NLP Libraries

* NLTK
* Scikit-Learn

## Data Analysis

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn

## Deployment

* Streamlit

---

# 📂 Project Structure

```bash
Mental_Health_Prediction/
│
├── mental_health_dataset.csv
├── app.py
├── model.pkl
├── vectorizer.pkl
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

# ✨ Features

✅ Mental Health Text Classification

✅ Natural Language Processing

✅ Text Cleaning

✅ Feature Extraction

✅ Machine Learning Prediction

✅ Real-Time User Input

✅ Interactive Streamlit Interface

✅ End-to-End NLP Pipeline

---

# 📈 Machine Learning Pipeline

1. Dataset Collection
2. Data Cleaning
3. Text Preprocessing
4. Feature Extraction
5. Model Training
6. Model Evaluation
7. Prediction
8. Deployment

---

# 🎓 Learning Outcomes

This project helped in understanding:

* Natural Language Processing
* Text Classification
* Machine Learning Workflow
* Feature Engineering
* Data Preprocessing
* Model Evaluation
* Streamlit Deployment
* Real-World NLP Applications

---

# 💡 Real World Applications

This project can be applied in:

* Mental Health Research
* Social Media Analysis
* Healthcare Analytics
* Emotional Text Analysis
* Sentiment Monitoring Systems
* Educational NLP Projects

---

# 🚀 Future Enhancements

Future improvements may include:

* Deep Learning Models (LSTM, GRU)
* Transformer Models (BERT)
* Multi-Class Classification Improvements
* Emotion Detection System
* Mental Health Chatbot Integration
* Explainable AI Features
* Cloud Deployment

---

# ⚠️ Disclaimer

This project is intended for educational and research purposes only.

The predictions generated by the system should not be considered medical diagnoses or professional mental health advice.

Users experiencing mental health concerns should consult qualified healthcare professionals.

---

# 👨‍💻 Author

Rishu Gurjar

Python Developer | Machine Learning Enthusiast | NLP Learner

---

# ⭐ Support

If you found this project helpful, please consider giving it a star on GitHub.
