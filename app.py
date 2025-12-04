import streamlit as st
import os

from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

llm = ChatGroq(groq_api_key=groq_api_key, model="llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions on basis of provided context only.
    please provide only most accurate response based on the question
    <context>
    {context}
    <context>
    Question: {input}
    """
)

def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        loader = PyPDFDirectoryLoader("research_papers")  # data ingestion step
        docs = loader.load()  # Document loading

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        final_documents = text_splitter.split_documents(docs[:50])

        # save if you want later
        st.session_state.final_documents = final_documents

        st.session_state.vectors = FAISS.from_documents(
            final_documents,
            st.session_state.embeddings
        )

st.markdown("## **📄 PaperMind — Research Q&A Assistant**")
st.write("""
**How to use this app:**

1. Place your PDF research papers inside the `research_papers` folder.
2. Click **Document Embedding** to create a vector database.
3. Type your question in the input box.
4. Click **ANSWER** to get responses based only on your uploaded papers.
5. Expand **Document similarity Search** to see which chunks were used.
""")


user_prompt = st.text_input("Enter your query from paper here")

if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Vector DB is created")

if user_prompt:
    if "vectors" not in st.session_state:
        st.error("Please click 'Document Embedding' first to create the vector DB.")
    else:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        
        response = retrieval_chain.invoke({"input": user_prompt})

if st.button("ANSWER"):
            st.write(response["answer"])
#Show similar document chunks like in the screenshot
            with st.expander("Document similarity Search"):
                for i, doc in enumerate(response["context"]):
                    st.markdown(f"**Chunk {i+1}**")
                    st.write(doc.page_content)
                    
                    st.write("---")

