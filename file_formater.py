import os
from flask import Flask, request, jsonify, send_file
import pandas as pd
import yaml

app = Flask(__name__)

# Load YAML configuration
with open('config.yaml', 'r') as yaml_file:
    config = yaml.safe_load(yaml_file)

# Static folder to save modified files
UPLOAD_FOLDER = 'static'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    API to upload a CSV or TXT file, rename columns using YAML config, and return the modified file.
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: The CSV or TXT file to be uploaded
    responses:
      200:
        description: The modified CSV file
        content:
          application/csv:
            schema:
              type: string
              format: binary
    """
    # Check if a file is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Ensure the file is a CSV or TXT
    if not (file.filename.endswith('.csv') or file.filename.endswith('.txt')):
        return jsonify({"error": "Invalid file type. Only CSV or TXT allowed."}), 400

    # Read the file into a Pandas DataFrame
    try:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_csv(file, delimiter='\t')  # Assuming tab-delimited TXT file
    except Exception as e:
        return jsonify({"error": f"Error reading file: {str(e)}"}), 400

    # Rename the columns based on the YAML file
    column_mapping = config.get('column_mapping', {})
    df.rename(columns=column_mapping, inplace=True)

    # Save the modified file
    output_file_path = os.path.join(UPLOAD_FOLDER, f'modified_{file.filename}')
    df.to_csv(output_file_path, index=False)

    # Send the modified file as response
    return send_file(output_file_path, as_attachment=True, mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)
