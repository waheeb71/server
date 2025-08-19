import pdfkit
from flask import Flask, request, send_file
import io

app = Flask(__name__)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    data = request.json
    html_content = data.get('html', '<h1>Empty</h1>')

    pdf_file = io.BytesIO()
    pdfkit.from_string(html_content, pdf_file)
    pdf_file.seek(0)
    return send_file(pdf_file, mimetype='application/pdf', as_attachment=True,
                     download_name='quote.pdf')
