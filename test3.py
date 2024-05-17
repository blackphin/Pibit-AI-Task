from importlib import metadata
from pydoc import doc
import chromadb
# chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path="chroma.db")
# collection = chroma_client.create_collection(name="log_store")
collection = chroma_client.get_collection(name="log_store")

collection.delete(
    ids=["id1"]
)

# Add error log file to the collection documents
with open("log1.log", "r") as f:
    print(f.read())
    collection.add(documents=f.read(), metadatas={
                   "source": "log1.log"}, ids="log1")
with open("log2.log", "r") as f:
    print(f.read())
    collection.add(documents=f.read(), metadatas={
                   "source": "log2.log"}, ids="log2")

# print(collection.query(query_texts="Info for log 1"))
print(collection.get(where={"source": "log1.log"}))
