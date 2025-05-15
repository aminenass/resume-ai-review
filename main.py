from langchain_openai import ChatOpenAI
import streamlit as st
import chardet
import os
import fitz # PyMuPDF for PDF
import docx  # python-docx for Word

llm = ChatOpenAI(model="", api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("OPENAI_ENDPOINT"),)


st.title("HI, I'M A RESUME ANALYSER")
st.divider()


def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.type
    file_name = uploaded_file.name.lower()

    # PDF
    if "pdf" in file_type or file_name.endswith(".pdf"):
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])

    # Word DOCX
    elif "word" in file_type or file_name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])

    # Plain Text
    elif "text" in file_type or file_name.endswith(".txt"):
        raw = uploaded_file.read()
        encoding = chardet.detect(raw)["encoding"] or "utf-8"
        return raw.decode(encoding, errors="ignore")

    else:
        return "Unsupported file type. Please upload a PDF, DOCX, or TXT file."

# Streamlit UI
uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    with st.spinner("Wait a minute"):

        resume_text = extract_text_from_file(uploaded_file)

        pre_prompt = f"""
             You are a professional resume reviewer.

                I will provide you with a resume or CV. Please analyze it and provide detailed feedback:

                1. Identify its strengths — e.g., structure, tone, accomplishments, keywords, formatting, etc.
                2. Identify its weaknesses or areas for improvement — e.g., vague phrasing, missing sections, poor formatting, lack of metrics, etc.
                3. Suggest specific improvements — how it could be made stronger, more impactful, or more tailored for a role in marketing, data science, or software engineering.
                4. Do not rewrite the resume — just provide a constructive and professional review.
            """
        
        prompt = pre_prompt + resume_text

        response = llm.invoke(prompt)  # or however you're calling your LLM
        st.write(response.content)


