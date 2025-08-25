from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Color+Emoji&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <style>
    .noto-color-emoji-regular {
  font-family: "Noto Color Emoji", serif;
  font-weight: 400;
  font-style: normal;
}
        body {
            font-family: "Noto Color Emoji", sans-serif;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <p>🔷 💎 ♦️ This is a test with colored emojis!</p>
</body>
</html>
"""

HTML(string=html_content).write_pdf("output.pdf")
