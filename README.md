# 🧠 Mental Health Prediction System
# 🌐 Live Demo

🚀 **Try the Application Here**

https://mentalhealthproject-vggmug4wh94z3zqj8mgyyp.streamlit.app/
---

# 🚀 Project Overview

The Mental Health Prediction System is a Natural Language Processing (NLP) and Machine Learning project developed to classify mental health conditions based on textual user inputs.

The system analyzes text written by individuals and predicts the likely mental health category associated with the content. By learning patterns from real-world mental health discussions, the model can identify emotional and psychological indicators present in the text.

This project demonstrates the complete NLP workflow including text preprocessing, feature extraction, model training, evaluation, and prediction.

---

# 🎯 Problem Statement

Mental health challenges such as anxiety, depression, stress, and other emotional conditions are increasingly discussed through online platforms and social communities.

Manually analyzing large amounts of text data is difficult and time-consuming.

The objective of this project is to build an intelligent text classification system capable of identifying mental health categories from user-written text using Natural Language Processing and Machine Learning techniques.

---

# 📊 Dataset Information

Dataset Name: Mental Health Text Dataset

Total Records: 992

Total Features: 2

### Features

| Feature | Description                               |
| ------- | ----------------------------------------- |
| text    | User-generated mental health related text |
| status  | Mental health category (Target Variable)  |

---

# 🎯 Project Objectives

* Analyze mental health related text
* Classify mental health conditions
* Apply NLP techniques
* Build text classification models
* Extract meaningful insights from textual data
* Improve understanding of sentiment and psychological patterns

---

# ⚙️ How The System Works

```text
User Text Input
        │
        ▼
 Text Cleaning
        │
        ▼
 NLP Preprocessing
        │
        ▼
 Feature Extraction
        │
        ▼
 Trained ML Model
        │
        ▼
 Mental Health Prediction
        │
        ▼
 Final Result
```

---

# 📝 Input Example

```text
I feel stressed all the time and I cannot focus on anything. I feel tired and emotionally exhausted.
```

---

# 🎯 Output Example

```text
Predicted Status: Anxiety
```

or

```text
Predicted Status: Depression
```

depending on the learned patterns.

---

# 🔍 NLP Pipeline

### Step 1: Text Collection

Load mental health text data using Pandas.

---

### Step 2: Text Preprocessing

Text cleaning operations:

* Lowercasing
* Removing punctuation
* Removing special characters
* Removing extra spaces
* Tokenization
* Stopword removal

---

### Step 3: Feature Extraction

Convert text into numerical vectors using:

* Count Vectorizer
* TF-IDF Vectorizer

---

### Step 4: Model Training

Train machine learning algorithms on processed text.

Possible algorithms:

* Naive Bayes
* Logistic Regression
* Random Forest
* Support Vector Machine (SVM)

---

### Step 5: Model Evaluation

Evaluate performance using:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

### Step 6: Prediction

The trained model predicts the most likely mental health category based on user input text.

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

✅ Text Preprocessing

✅ Feature Extraction

✅ Machine Learning Prediction

✅ Real-Time User Input Prediction

✅ Data Visualization

✅ Interactive Prediction System

---

# 📈 Analysis Performed

### Text Distribution Analysis

Analyze the distribution of mental health categories.

---

### Word Frequency Analysis

Identify commonly used words across categories.

---

### Category Comparison

Compare textual patterns among mental health conditions.

---

### NLP Feature Analysis

Study important predictive words and phrases.

---

# 🎓 Learning Outcomes

Through this project, the following skills were developed:

* Natural Language Processing
* Text Cleaning
* Feature Extraction
* Text Classification
* Machine Learning
* Model Evaluation
* Data Visualization
* Python Programming

---

# 💡 Applications

This project can be useful for:

* Mental Health Analytics
* Research Studies
* Educational NLP Projects
* Social Media Text Analysis
* Sentiment and Emotion Analysis
* Healthcare Data Science

---

# 🚀 Future Improvements

* Deep Learning Models (LSTM, GRU)
* Transformer Models (BERT)
* Multi-label Classification
* Mental Health Dashboard
* Streamlit Web Application
* Real-Time Chat Analysis
* Explainable AI Integration

---

# 👨‍💻 Author

**Rishu Gurjar**

Python Developer | Machine Learning Enthusiast | NLP Learner

---

# ⚠️ Disclaimer

This project is developed for educational and research purposes only.

The predictions generated by the model should not be considered professional psychological or medical advice. For mental health concerns, please consult qualified healthcare professionals.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
