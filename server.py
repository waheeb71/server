from flask import Flask, request, send_file
from weasyprint import HTML
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # للسماح بالطلبات من React

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    try:
        data = request.json
        html_content = data.get('html', '<h1>Empty</h1>')

        # تحويل HTML إلى PDF بحجم A4
        pdf_file = io.BytesIO()
        HTML(string=html_content).write_pdf(pdf_file)
        pdf_file.seek(0)

        return send_file(
            pdf_file,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='quote.pdf'
        )
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
