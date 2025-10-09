from fastapi import FastAPI
from app.client.firestore import get_firestore_client
from typing import Dict, List

app = FastAPI()

@app.get('/')
def index() -> Dict[str, str]:
    """
    Simple JSON return for testing FastAPI.
    :return: Dictionary with string values with a message
    """
    return {"Message": "Hello, World with FastAPI"}


@app.get('/notes')
async def get_notes() -> Dict[str,List[str]]:
    """
    Get all notes stored in Firestore
    :return Dict[str,List[str]]: Dictionary of notes stored in Firestore
    """
    db = get_firestore_client()
    collection_ref = db.collection("test-notes")

    notes: list = list()

    # Extract all documents the database
    docs = collection_ref.stream()

    for doc in docs:
        note_data = doc.to_dict()
        notes.append(note_data)

    return {"Notes": notes}
