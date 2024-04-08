from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_pdf(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    document = loader.load()

    return document

def text_splitter(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks

def download_huggingface_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    return embeddings