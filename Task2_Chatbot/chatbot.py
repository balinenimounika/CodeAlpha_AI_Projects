import json
import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLP resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load FAQ data
with open('faq_data.json', 'r', encoding='utf-8') as file:
    faq_data = json.load(file)

questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]

# Text preprocessing function
def preprocess(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
    ]

    stop_words = set(stopwords.words('english'))

    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)

# Preprocess FAQ questions
processed_questions = [preprocess(q) for q in questions]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(processed_questions)

print("\n===================================")
print("      FAQ CHATBOT STARTED")
print("===================================")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    processed_input = preprocess(user_input)

    user_vector = vectorizer.transform([processed_input])

    similarity_scores = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match_index = similarity_scores.argmax()

    confidence = similarity_scores[0][best_match_index]

    if confidence > 0.25:
        print("\nBot:", answers[best_match_index])
        print(f"(Confidence: {confidence:.2f})\n")
    else:
        print("\nBot: Sorry, I couldn't find a relevant answer.\n")