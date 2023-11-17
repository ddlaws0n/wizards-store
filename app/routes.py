from flask import Blueprint, render_template, request, flash, jsonify
import boto3
from botocore.exceptions import NoCredentialsError

main_blueprint = Blueprint('main', __name__)
register_blueprint = Blueprint('register', __name__)

def upload_to_s3(first_name, last_name):
    s3 = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'
    file_name = 'registrations.txt'
    content = f"{first_name}, {last_name}\n"

    try:
        # Attempt to download the existing file from S3
        s3.download_file(bucket_name, file_name, file_name)
    except:
        # If the file does not exist, create it
        open(file_name, 'w').close()

    # Append the new record to the file
    with open(file_name, 'a') as file:
        file.write(content)

    try:
        # Upload the updated file to S3
        s3.upload_file(file_name, bucket_name, file_name)
    except NoCredentialsError:
        return "Credentials not available for S3 upload."

    return "Uploaded to S3 successfully."

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@register_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        # Process data and upload to S3
        response_message = upload_to_s3(first_name, last_name)

        # Check if request is from HTMX
        if 'HX-Request' in request.headers:
            # Return a different response for HTMX request
            return jsonify({'message': response_message})

        return response_message
    return render_template('register.html')