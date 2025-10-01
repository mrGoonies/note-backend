from fastapi import FastAPI
from app.client.firestore import get_firestore_client

app = FastAPI()

@app.get('/')
def index():
    return {"Message": "Hello, World with FastAPI"}


@app.get('/notes')
async def get_notes():
    db = get_firestore_client()
    collection_ref = db.collection("test-notes")

    notes: list = list()

    # Extract all documents the database
    docs = collection_ref.stream()

    for doc in docs:
        note_data = doc.to_dict()
        notes.append(note_data)

    return {"Notes": notes}
