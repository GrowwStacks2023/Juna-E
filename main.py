import pdfkit

blog_post_html = """
<html>
  <head><title>My Blog Post</title></head>
  <body>
    <h1>How to Use Python for Web Development</h1>
    <p>Python is a versatile language...</p>
    <h2>Getting Started</h2>
    <p>To start developing web applications with Python...</p>
  </body>
</html>
"""

pdfkit.from_string(blog_post_html, 'C:\\Clients\\Oleksandr\\sample.pdf')