from flask import Flask, request, make_response, send_file
from weasyprint import HTML, CSS
import io
import re

app = Flask(__name__)

@app.route('/htmltopdf', methods=['POST'])
def process():
    if request.method == "POST":
        content = request.form.get("html")
        if not content:
            return make_response("No HTML content provided", 400)

        try:
            # Clean up the HTML content - remove excessive whitespace but preserve structure
            content = re.sub(r'\n\s*\n', '\n', content)  # Remove multiple newlines
            content = re.sub(r'>\s+<', '><', content)     # Remove whitespace between tags
            content = content.strip()
            
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Noto+Color+Emoji&display=swap" rel="stylesheet">
            </head>
            <body>
                {content}
            </body>
            </html>
            """

            # WeasyPrint-specific CSS to match browser rendering exactly
            css_content = CSS(string='''
                @page {
                    margin: 0.5in;
                    size: A4;
                }
                
                body {
                    font-family: "Noto Color Emoji", Arial, sans-serif;
                    font-size: 12px;
                    line-height: 1.4;
                    margin: 0;
                    padding: 20px;
                }
                
                /* Reset all margins and paddings for consistent spacing */
                * {
                    box-sizing: border-box;
                }
                
                /* Table styling to match browser exactly */
                table {
                    border-collapse: collapse;
                    border-spacing: 0;
                    width: 100%;
                    margin: 0;
                }
                
                td, th {
                    padding: 8px;
                    text-align: left;
                    border: 1px solid #ddd;
                    vertical-align: top;
                }
                
                /* Preserve div spacing as in browser */
                div {
                    margin: 0;
                    padding: 0;
                }
                
                /* Headers and paragraphs */
                h1, h2, h3, h4, h5, h6 {
                    margin: 10px 0 5px 0;
                    padding: 0;
                }
                
                p {
                    margin: 5px 0;
                    padding: 0;
                }
                
                /* Specific styling for invoice elements */
                .invoice-header {
                    margin-bottom: 20px;
                }
                
                .invoice-table {
                    margin: 20px 0;
                }
                
                .footer-section {
                    margin-top: 20px;
                }
                
                /* Remove default browser margins that WeasyPrint adds */
                body, html {
                    margin: 0 !important;
                    padding: 0 !important;
                }
                
                /* Ensure proper text rendering */
                .noto-color-emoji-regular {
                    font-family: "Noto Color Emoji", serif;
                    font-weight: 400;
                    font-style: normal;
                }
                
                /* Style for colored elements (like red squares in your invoice) */
                .item-icon {
                    display: inline-block;
                    width: 12px;
                    height: 12px;
                    margin-right: 5px;
                }
            ''')

            pdf_stream = io.BytesIO()
            HTML(string=html_content).write_pdf(
                pdf_stream,
                stylesheets=[css_content],
                presentational_hints=True,
                optimize_size=('fonts', 'images')
            )
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
