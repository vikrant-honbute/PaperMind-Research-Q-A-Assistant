📄 PaperMind — Research Paper Q&A Assistant

A lightweight RAG (Retrieval-Augmented Generation) application built with Streamlit, LangChain, FAISS, HuggingFace Embeddings, and Groq LLM.
This tool allows you to upload research papers (PDFs) and ask natural-language questions. The app retrieves the most relevant text chunks and generates highly accurate answers based only on your documents.

🚀 Features

📂 Upload or add PDFs to the research_papers/ folder

🧩 Automatic text splitting using RecursiveCharacterTextSplitter

🎯 Vector embeddings using HuggingFace sentence-transformers

📘 Fast vector search powered by FAISS

🤖 Natural-language answers from Groq LLM (Gemma 7B)

🔍 “Document Similarity Search” section to show retrieved chunks

🧠 Clean Streamlit UI for asking questions interactively

📁 Project Structure
PaperMind/
│
├── research_papers/          # Add your PDF files here
├── app.py                    # Main Streamlit application
├── requirements.txt          # Project dependencies
├── .env                      # Contains GROQ_API_KEY
└── README.md                 # Project documentation

🔧 Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/PaperMind.git
cd PaperMind

2️⃣ Create & activate a virtual environment
python -m venv venv


Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

🔐 Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here


You can get your Groq API key from:
🔗 https://console.groq.com

📘 How to Use
1️⃣ Add PDFs

Place your research papers inside:

research_papers/

2️⃣ Start the Streamlit app
streamlit run app.py

3️⃣ Create Vector Database

Click:

➡️ Document Embedding

This processes your PDFs and builds a FAISS vector store.

4️⃣ Ask Your Question

Type a question such as:

“What is a Transformer model?”

Click:

➡️ ANSWER

5️⃣ View Retrieved Document Chunks

Expand:

➡️ Document similarity Search

This shows the exact text chunks used to generate the answer.

🛠️ Tech Stack

Python 3.10+

Streamlit — UI

LangChain — RAG pipeline

FAISS — Vector storage

HuggingFace Sentence Transformers — Embeddings

Groq LLM (Gemma 7B) — Answer generation

PyPDF — PDF ingestion

✨ Why PaperMind?

Lightweight and fast

100% local vector search (FAISS)

No dependency on OpenAI

Uses cutting-edge Groq inference for blazing-fast responses

Clean and simple UI

📌 Future Enhancements

🔧 Support for multi-PDF uploads

🧠 Conversation history (chat mode)

🏷 Document tagging & filtering

📊 PDF summarization

📥 Drag-and-drop file upload

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss your idea.

📜 License

This project is licensed under the MIT License.
