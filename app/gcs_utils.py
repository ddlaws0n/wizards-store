import os
from google.cloud import storage
from google.auth.exceptions import DefaultCredentialsError

def create_storage_client():
    try:
        # Try to create a storage client using default credentials
        storage_client = storage.Client()
    except DefaultCredentialsError:
        # If default credentials are not available, use the local key file
        service_account_path = '../argon-tuner-405813-e6403f4068a4.json'
        storage_client = storage.Client.from_service_account_json(service_account_path)
    
    return storage_client

# Use this client for GCS operations
storage_client = create_storage_client()
