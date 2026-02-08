from fastapi import FastAPI
from api import upload, search, metadata

# Initialize FastAPI app
app = FastAPI(title="Docu-Mind PDF NLP Engine", version="1.0")

# Include route modules
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(search.router, prefix="/search", tags=["Search"])
app.include_router(metadata.router, prefix="/metadata", tags=["Metadata"])
