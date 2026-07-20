import streamlit as st
import pandas as pd
import pdfplumber
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


def extract_text_from_pdf(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text

def rank_resumes(job_description, resumes):

    documents = [job_description] + resumes

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

    return similarity.flatten()

st.set_page_config(
    page_title="AI Resume Screening System",
    layout="wide"
)

st.title("AI-Powered Resume Screening and Candidate Ranking System")

st.write("Upload Resume PDFs and compare them with the Job Description.")

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

job_description = st.text_area(
    "Paste Job Description Here",
    height=250
)

if st.button("Rank Candidates"):

    if uploaded_files and job_description:

        processed_job = preprocess_text(job_description)

        resume_names = []
        processed_resumes = []

        progress = st.progress(0)

        for i, file in enumerate(uploaded_files):

            text = extract_text_from_pdf(file)

            cleaned = preprocess_text(text)

            processed_resumes.append(cleaned)

            resume_names.append(file.name)

            progress.progress((i + 1) / len(uploaded_files))

        scores = rank_resumes(processed_job, processed_resumes)

        results = pd.DataFrame({
            "Candidate": resume_names,
            "Matching Score (%)": (scores * 100).round(2)
        })

        results = results.sort_values(
            by="Matching Score (%)",
            ascending=False
        ).reset_index(drop=True)

        st.success("Candidate Ranking Completed Successfully!")

        st.dataframe(results, use_container_width=True)

        st.subheader("Top Candidate")

        st.write(
            f"**{results.iloc[0]['Candidate']}** "
            f"matched with a score of "
            f"**{results.iloc[0]['Matching Score (%)']}%**"
        )

        csv = results.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Ranking as CSV",
            data=csv,
            file_name="candidate_ranking.csv",
            mime="text/csv"
        )

    else:

        st.warning("Please upload at least one resume and enter a job description.")

st.markdown("---")
st.markdown("### Technologies Used")
st.write("""
- Python
- Streamlit
- Pandas
- Scikit-learn
- pdfplumber
- NLTK
- TF-IDF
- Cosine Similarity
""")