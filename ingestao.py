from llama_index import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
import chromadb

def construir_indice():
    documentos = SimpleDirectoryReader("data").load_data()
    cliente = chromadb.HttpClient(host="chromadb", port=8000)
    store = ChromaVectorStore(chroma_collection=cliente.get_or_create_collection("docs"))
    contexto = StorageContext.from_defaults(vector_store=store)
    index = VectorStoreIndex.from_documents(documentos, storage_context=contexto)
    index.storage_context.persist()

if __name__ == "__main__":
    construir_indice()
