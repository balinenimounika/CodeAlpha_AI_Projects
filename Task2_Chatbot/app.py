import json
import string
import nltk
import streamlit as st

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# PAGE CONFIG

st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)
# SESSION STATE INITIALIZATION
if "messages" not in st.session_state:
    st.session_state.messages = []

if "score" not in st.session_state:
    st.session_state.score = 0

# CUSTOM CSS

st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#0f172a,
#1e293b,
#312e81
);
}

.main-title{
text-align:center;
font-size:55px;
font-weight:bold;
color:white;
margin-bottom:10px;
}

.subtitle{
text-align:center;
color:#cbd5e1;
font-size:18px;
margin-bottom:25px;
}

.footer{
text-align:center;
margin-top:40px;
color:#cbd5e1;
font-size:15px;
}

[data-testid="stMetric"]{
background-color: rgba(255,255,255,0.08);
padding:15px;
border-radius:12px;
}

</style>
""", unsafe_allow_html=True)


# SIDEBAR


with st.sidebar:

    st.title("📚 FAQ Categories")

    st.markdown("""
- Python
- Artificial Intelligence
- Machine Learning
- Deep Learning
- NLP
- Data Science
- SQL
- Java
- JavaScript
- Web Development
""")
    st.success("CodeAlpha Internship Project")

    st.subheader("📂 Upload Custom FAQ")

    uploaded_file = st.file_uploader(
        "Upload FAQ JSON File",
        type=["json"]
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.session_state.score = 0
        st.rerun()

    chat_text = ""

for msg in st.session_state.messages:
    chat_text += (
        f"{msg['role'].upper()}: "
        f"{msg['content']}\n\n"
    )

st.download_button(
    "📥 Download Chat",
    data=chat_text,
    file_name="chat_history.txt",
    mime="text/plain"
)

# NLTK DOWNLOADS

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


# LOAD FAQ DATA


if uploaded_file is not None:

    faq_data = json.load(uploaded_file)

else:

    with open(
        "faq_data.json",
        "r",
        encoding="utf-8"
    ) as file:

        faq_data = json.load(file)

questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]


# PREPROCESSING


def preprocess(text):

    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
    ]

    stop_words = set(stopwords.words("english"))

    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)

processed_questions = [
    preprocess(q)
    for q in questions
]


# TF-IDF

vectorizer = TfidfVectorizer(
    ngram_range=(1,2),
    stop_words="english"
)

faq_vectors = vectorizer.fit_transform(
    processed_questions
)


# Welcome Message
if len(st.session_state.messages) == 0:
    st.info(
        "👋 Welcome! Ask me anything about AI, Python, Machine Learning, NLP, Java, SQL, and more."
    )

# Title
st.markdown(
"""
<div class='main-title'>
🤖 AI FAQ Chatbot
</div>
""",
unsafe_allow_html=True
)


# USER INPUT

user_question = st.text_input(
    "💬 Ask your question..."
)
submit = st.button("🚀 Get Answer")

if  submit and user_question:

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    processed_input = preprocess(
        user_question
    )

    user_vector = vectorizer.transform(
        [processed_input]
    )

    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match = similarities.argmax()

    score = similarities[0][best_match]

    st.session_state.score = score

    if score > 0.25:

        answer = answers[best_match]

    else:

        answer = "❌ Sorry, no matching FAQ found."

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()


# CHAT HISTORY


st.divider()

for msg in st.session_state.messages:

    if msg["role"] == "user":

        with st.chat_message("user", avatar="👤"):
            st.write(msg["content"])

    else:

        with st.chat_message("assistant", avatar="🤖"):
            st.write(msg["content"])


# CONFIDENCE SCORE


if st.session_state.score > 0:

    st.progress(float(st.session_state.score))

    st.success(
        f"🎯 Confidence Score: {st.session_state.score:.2f}"
    )

# DASHBOARD


st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "📚 Total FAQs",
        len(faq_data)
    )

with col2:

    total_questions = len([
        msg
        for msg in st.session_state.messages
        if msg["role"] == "user"
    ])

    st.metric(
        "💬 Questions Asked",
        total_questions
    )

# FOOTER


st.markdown(
"""
---
<center>
<b>Developed by Mounika Balineni</b><br>
CodeAlpha Internship | Task 2 - FAQ Chatbot
</center>
""",
unsafe_allow_html=True
)