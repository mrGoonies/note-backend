from google.cloud import firestore
from app.config import settings

print(settings.GCP_PROJECT_ID)

project_id = settings.GCP_PROJECT_ID

database_id= settings.FIRESTORE_DATABASE_ID
print(database_id)

if not project_id:
    raise ValueError("GCP_PROJECT_ID Not found or not configured.")

if not database_id:
    raise ValueError("FIRESTORE_DATABASE_ID Not found or not configured.")


# We pass the credentials to the Firestore client
client = firestore.Client(project=project_id, database=database_id)

# After validation connection with Firestore. Return client for interact with DB
def get_firestore_client():
    return client