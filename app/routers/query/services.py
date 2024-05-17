import os
from datetime import datetime
import chromadb


# Initialize the chroma client and get the collection
def get_chroma_collection():
    try:
        chroma_client = chromadb.PersistentClient(path="chroma.db")
    except:
        chroma_client = chromadb.Client()

    collection = chroma_client.get_or_create_collection(name="log_store")

    return collection


# Update Error Log
def update_error_log(error_log_path):
    collection = get_chroma_collection()

    # Delete existing error log
    try:
        collection.delete(ids=[error_log_path])
    except:
        pass

    # Current Time
    current_time = datetime.timestamp(datetime.now())

    # Add error log file to the collection documents
    with open(f"error_logs/{error_log_path}", "r", encoding="utf-8") as f:
        collection.add(
            documents=f.read(),
            metadatas={
                "source": error_log_path,
                "timestamp": current_time
            },
            ids=error_log_path
        )
