# 🤖 AI FAQ Chatbot

An intelligent FAQ Chatbot developed using **Python, Streamlit, NLTK, and Scikit-learn**. This chatbot answers user queries by finding the most relevant FAQ using **TF-IDF Vectorization** and **Cosine Similarity**.

Built as part of the **CodeAlpha Artificial Intelligence Internship - Task 2**.

---

## 🚀 Features

- 💬 Interactive Chat Interface
- 📚 FAQ-Based Question Answering
- 🔍 Intelligent Question Matching
- 🎯 Confidence Score Display
- 📂 Upload Custom FAQ JSON File
- 📥 Download Chat History
- 🗑️ Clear Chat Option
- 📊 Dashboard Metrics
- 🌙 Modern Dark UI
- ⚡ Fast Response System

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NLTK
- Scikit-learn
- JSON
- TF-IDF Vectorizer
- Cosine Similarity

---

## 📂 Project Structure

```text
Task2_Chatbot/
│
├── app.py
├── faq_data.json
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/balinenimounika/CodeAlpha_AI_Projects.git
```

### Move to Project Folder

```bash
cd Task2_Chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📄 FAQ JSON Format

```json
[
  {
    "question": "What is AI?",
    "answer": "Artificial Intelligence is the simulation of human intelligence by machines."
  },
  {
    "question": "What is Machine Learning?",
    "answer": "Machine Learning is a subset of Artificial Intelligence that enables systems to learn from data."
  }
]
```

---

## 🔍 How It Works

1. User enters a question.
2. Text is preprocessed using NLTK.
3. TF-IDF converts text into numerical vectors.
4. Cosine Similarity calculates similarity scores.
5. Best matching FAQ is identified.
6. Corresponding answer is displayed.
7. Confidence score is shown.

---

## 📊 Application Features

### Chat Interface
- User-friendly chatbot interface
- Real-time question answering
- Chat history support

### FAQ Search Engine
- TF-IDF based retrieval
- Intelligent text matching
- Fast response generation

### Dashboard
- Total FAQs Count
- Questions Asked Count
- Confidence Score Indicator

### Additional Features
- Upload Custom FAQ Files
- Download Chat History
- Clear Chat Functionality

---

## 🎯 Example Questions

- What is AI?
- What is Machine Learning?
- What is Deep Learning?
- What is NLP?
- What is Python?
- What is Java?
- What is SQL?
- What is Data Science?

---

## 📈 Future Enhancements

- Voice Input Support
- Text-to-Speech Responses
- Multi-language Support
- AI-Powered Responses
- Database Integration
- User Authentication
- Admin Dashboard

---

## 👨‍💻 Internship Information

**Internship:** CodeAlpha Artificial Intelligence Internship

**Task:** Task 2 - FAQ Chatbot

**Domain:** Artificial Intelligence

---

## 👩‍💻 Developed By

### Mounika Balineni

---

## ⭐ Acknowledgement

This project was successfully completed as part of the **CodeAlpha Artificial Intelligence Internship Program** and demonstrates the implementation of Natural Language Processing techniques for building an intelligent FAQ Chatbot.

---

### Thank You for Visiting This Project! 🚀