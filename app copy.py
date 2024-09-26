import os
from flask import Flask, request, jsonify, send_file
from flasgger import Swagger
from flask_restful import Api
from book_controller import BookList
import pandas as pd
from gevent.pywsgi import WSGIServer

app=Flask(__name__)
swagger=Swagger(app)

output_folder = os.path.join(app.root_path, 'static')


api = Api(app)
api.add_resource(BookList, '/books')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    """
    Upload a CSV file and get a modified CSV as output hello
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: The CSV file to be uploaded
    responses:
      200:
        description: The modified CSV file will be returned
        content:
          application/csv:
            schema:
              type: string
              format: binary
      400:
        description: Error processing the file
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and file.filename.endswith('.csv'):
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file)

        # Example modification: add a new column with row numbers
        df['RowNumber'] = range(1, len(df) + 1)

        # Save the modified CSV to the output folder
        output_path = os.path.join(output_folder, 'output.csv')
        df.to_csv(output_path, index=False)

        # Send the modified CSV file as the response
        return send_file(output_path, as_attachment=True, mimetype='text/csv', download_name='modified_output.csv')

    return jsonify({"error": "Invalid file type, only CSV is allowed"}), 400


if __name__ == '__main__':
    # app.run(debug=True)
    http_server=WSGIServer(('',8000),app)
    http_server.serve_forever()
    
