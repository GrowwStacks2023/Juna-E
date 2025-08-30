from flask import Flask, request, make_response, send_file
from weasyprint import HTML
import io

app = Flask(__name__)

@app.route('/htmltopdf', methods=['POST'])
def process():
    if request.method == "POST":
        content = request.form.get("html")
        if not content:
            return make_response("No HTML content provided", 400)

        try:
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Noto+Color+Emoji&display=swap" rel="stylesheet">
                <style>
                    body {{
                        font-family: "Noto Color Emoji", sans-serif !important;
                        font-size: 24px;
                    }}
                    .noto-color-emoji-regular {{
                        font-family: "Noto Color Emoji", serif;
                        font-weight: 400;
                        font-style: normal;
                    }}
                </style>
            </head>
            <body>
                {content}
            </body>
            </html>
            """

            pdf_stream = io.BytesIO()
            HTML(string=html_content).write_pdf(pdf_stream)
            pdf_stream.seek(0)

            return send_file(
                pdf_stream,
                as_attachment=True,
                download_name="output.pdf",
                mimetype="application/pdf"
            )
        except Exception as e:
            return make_response(f"Error generating PDF: {str(e)}", 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
