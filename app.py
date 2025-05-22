from fastapi import FastAPI
from pydantic import BaseModel
from llama_index import VectorStoreIndex, StorageContext
from llama_index.vector_stores import ChromaVectorStore
import chromadb
from ingestao import construir_indice

app = FastAPI()

construir_indice()

cliente = chromadb.HttpClient(host="chromadb", port=8000)
store = ChromaVectorStore(chroma_collection=cliente.get_or_create_collection("docs"))
storage_context = StorageContext.from_defaults(vector_store=store)
index = VectorStoreIndex.from_vector_store(vector_store=store)
engine = index.as_query_engine()

class Pergunta(BaseModel):
    pergunta: str

@app.post("/perguntar")
def perguntar(p: Pergunta):
    resposta = engine.query(p.pergunta)
    return {"resposta": str(resposta)}
