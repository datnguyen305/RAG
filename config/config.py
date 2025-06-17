LLM_CONFIG = {
    "model_name": "gpt-4o-mini",
    "temperature": 0.1,
    "streaming": True,
}

TEXTSPLIT_CONFIG = {
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "add_start_index": True,
}

EMBEDDING_CONFIG = {
    "model_name": "text-embedding-3-small",
    "batch_size": 100,
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "add_start_index": True,
}