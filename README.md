# Cognitive Services and Optical Character Recognition (OCR) Analytics

## Description
This project is a web application that allows users to upload images, extract text from them using Azure's OCR (Optical Character Recognition) service, and display both the image and the extracted text on the same page.

## Technologies Used
- **Flask**: A lightweight Python web framework used to build the web application.
- **HTML/CSS**: For the front-end user interface design.
- **Azure Cognitive Services**: Specifically, the Azure OCR API for text extraction from images.
- **Requests Library**: To handle HTTP requests to the Azure API.


## Key Features
- **Image Upload**:  
  Users can upload images in various formats using an HTML form.

- **Text Extraction**:  
  Uploaded images are processed using Azure's OCR API, which detects and extracts text.

- **Dynamic Display**:  
  The application displays the uploaded image alongside the extracted text on the same page.

- **Responsive Design**:  
  The interface is styled with CSS to be user-friendly and visually appealing.

## Functionality Breakdown
### `app.py`:
- Contains the Flask application logic.
- Handles routes for rendering the index page and processing image uploads.
- Interacts with Azure's OCR API to perform text extraction.

### `index.html`:
- The main template for the user interface.
- Includes a form for image uploads and sections to display the uploaded image and OCR results.

## Conclusion
This project provides a practical application of Flask and Azure Cognitive Services, demonstrating how to build a user-friendly web interface for text extraction from images. The application can be expanded further with additional features for enhanced functionality.
