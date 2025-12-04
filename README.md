# 📄 PaperMind — Research Paper Q&A (RAG App)

PaperMind is a lightweight **RAG (Retrieval-Augmented Generation)** app built using **FAISS**, **LangChain**, **HuggingFace Embeddings**, and **Groq LLM**.  
It allows you to load research papers and ask questions — the answers come strictly from your documents.

---

## 🚀 Features

- PDF ingestion from `research_papers/`  
- Text chunking via RecursiveCharacterTextSplitter  
- Embeddings using Sentence-Transformers  
- Fast vector search with FAISS  
- Answer generation using Groq (Gemma 7B)  
- Shows retrieved document chunks for transparency  
- Clean and simple Streamlit interface  

---

## 📦 Installation

### 1. Clone the project
```bash
git clone https://github.com/yourusername/PaperMind.git
cd PaperMind
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root:

```
GROQ_API_KEY=your_groq_api_key
```

Get your API key here: https://console.groq.com

---

## 📘 How to Use

1. Add your PDF files to the `research_papers/` folder.  
2. Run the app:

```bash
streamlit run app.py
```

3. Click **Document Embedding** to build the FAISS vector database.  
4. Ask any question related to your uploaded papers.  
5. Expand **Document similarity Search** to see which chunks were used to answer your question.

---

## 🧱 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **LangChain-Classic (for chains)**
- **FAISS**
- **HuggingFace Sentence Transformers**
- **Groq LLM (Gemma)**  
- **PyPDF**

---

## 📁 Project Structure

```
PaperMind/
│
├── research_papers/       # Place PDFs here
├── app.py                 # Main application
├── requirements.txt
├── .env
└── README.md
```

---

## 💡 Future Improvements
- File upload support  
- Multi-model LLM comparison  
- Summary generation  
- Chat mode with history  

---

## 📝 License
MIT License — free to use and modify.

---

## 🙌 Credits
Built by **Vikrant** using LangChain, FAISS, HuggingFace, and Groq.
