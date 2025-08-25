from flask import Flask, request, make_response, send_file
import pdfkit, io, os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Ensure wkhtmltopdf path is set correctly
WKHTMLTOPDF_PATH = "/usr/bin/wkhtmltopdf"  # Adjust this based on installation
CONFIG = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

@app.route('/htmltopdf', methods=['POST'])
def process():
    if request.method == "POST":
        content = request.form.get("html")  # Ensure the request sends "html" as form data
        if not content:
            return make_response("No HTML content provided", 400)
        try:
            pdf_buffer = pdfkit.from_string(content, False, configuration=CONFIG)
            pdf_stream = io.BytesIO(pdf_buffer)
            return send_file(pdf_stream, as_attachment=True, download_name="content.pdf", mimetype="application/pdf")
        except Exception as e:
            return make_response(f"Error generating PDF: {str(e)}", 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)