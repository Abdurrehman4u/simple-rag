# Model names
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "gemini-2.5-flash"

# Text splitting
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval
TOP_K_RESULTS = 3

# Vector DB
COLLECTION_NAME = "my_docs"

# Supported file types
SUPPORTED_EXTENSIONS = [".pdf", ".txt"]

# Prompt template
SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer the question only from the provided context.
If the answer is not found in the context, clearly say so.
"""