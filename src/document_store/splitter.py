from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.config import TEXTSPLIT_CONFIG

def split_text(docs, DOCUMENT_SPLITTING_CONFIG=TEXTSPLIT_CONFIG):
    """
    Splits the provided documents into smaller chunks.
    
    :param documents: List of documents to be split.
    :return: List of split document chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=DOCUMENT_SPLITTING_CONFIG.get("chunk_size",1000), 
        chunk_overlap=DOCUMENT_SPLITTING_CONFIG.get("chunk_overlap", 200),
        add_start_index=DOCUMENT_SPLITTING_CONFIG.get("add_start_index", True)
    )

    all_splits = text_splitter.split_documents(docs)
    return all_splits