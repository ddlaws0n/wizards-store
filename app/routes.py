import os
from flask import Blueprint, render_template, request, flash, jsonify
from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.auth.exceptions import DefaultCredentialsError

main_blueprint = Blueprint('main', __name__)
register_blueprint = Blueprint('register', __name__)

def create_storage_client():
    try:
        # Try to create a storage client using default credentials
        storage_client = storage.Client()
    except DefaultCredentialsError:
        # If default credentials are not available, use the local key file
        service_account_path = '/app/argon-tuner-405813-e6403f4068a4.json'
        storage_client = storage.Client.from_service_account_json(service_account_path)
    
    return storage_client

def upload_to_gcs(first_name, last_name):
    storage_client = create_storage_client()
    bucket_name = 'wizard-bucket'
    file_name = 'registrations.txt'
    content = f"{first_name} {last_name}\n"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    try:
        # Attempt to download the existing file from GCS
        current_content = blob.download_as_text()
    except NotFound:
        # If the file does not exist, create it
        current_content = ''

    # Append the new record to the content
    updated_content = current_content + content

    # Upload the updated content to GCS
    blob.upload_from_string(updated_content)

    return "Hurray! Account created successfully. We promise to store your data safely in the cloud ☁️" 

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@register_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        # Process data and upload to S3
        response_message = upload_to_gcs(first_name, last_name)

        # Check if request is from HTMX
        if 'HX-Request' in request.headers:
            # Return a different response for HTMX request
            return jsonify({'message': response_message})

        return response_message
    return render_template('register.html')