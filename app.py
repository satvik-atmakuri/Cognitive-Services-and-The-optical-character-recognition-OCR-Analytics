from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Azure OCR API credentials
AZURE_OCR_URL = 'https://satvik.cognitiveservices.azure.com/vision/v3.2/ocr'
SUBSCRIPTION_KEY = '6ec46e0be5e84179a6d7a5f015de482c'

@app.route('/')
def index():
    return render_template('index.html', ocr_result=None, image_path=None)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the image temporarily
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        # Perform OCR using Azure
        ocr_result = process_ocr(image_path)

        return render_template('index.html', ocr_result=ocr_result, image_path=image_path)

def process_ocr(image_path):
    # Read the image file as binary
    with open(image_path, 'rb') as image_file:
        headers = {
            'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
            'Content-Type': 'application/octet-stream'
        }
        params = {
            'language': 'unk',  # 'unk' for auto-detect language
            'detectOrientation': 'true'
        }

        # Send the image file to the Azure OCR API
        response = requests.post(AZURE_OCR_URL, headers=headers, params=params, data=image_file)

    # Handle the response
    if response.status_code == 200:
        ocr_data = response.json()
        # Extract the text from the OCR response
        extracted_text = ''
        for region in ocr_data.get('regions', []):
            for line in region.get('lines', []):
                for word in line.get('words', []):
                    extracted_text += word['text'] + ' '
        return extracted_text.strip()
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == '__main__':
    app.run(debug=True)
