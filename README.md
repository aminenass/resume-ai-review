# 📄 Resume Analyzer

An AI-powered resume analyzer and enhancer built with **Streamlit** and **LLMs via OpenRouter**.  
This app helps users upload their CV or resume and receive a revised, improved version — professionally formatted and tailored to common roles like marketing, data science, or software engineering.

---

## 🚀 Features

- 📤 Upload resumes in **PDF**, **DOCX**, or **TXT** format  
- 🤖 Analyze content using an **LLM via OpenRouter**  
- 🧠 AI suggestions to:
  - Improve weak phrasing
  - Fill missing sections (skills, achievements, etc.)
  - Tailor the resume for professional roles

---

## 🛠 Built With

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenRouter.ai](https://openrouter.ai/) (LLM provider)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for PDF handling
- [python-docx](https://python-docx.readthedocs.io/en/latest/) for Word documents
- [chardet](https://github.com/chardet/chardet) for text encoding detection

---

## 📦 Setup

1. **Clone the repository**

```bash

git clone https://github.com/your-username/resume-ai-review.git
cd resume-ai-review

```
2. **Create a virtual environment and install dependencies**

```bash

Create a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

```

3. **Set up environment variables**
```bash

Create a .env file in the project root with the following content:

API_KEY=your_openrouter_api_key
ENDPOINT=https://openrouter.ai/api/v1

```

4. **Run the app**
```bash

streamlit run main.py

```